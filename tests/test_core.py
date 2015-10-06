#! /usr/bin/env python
from __future__ import print_function
import unittest, pygame, pygame.display, time, traceback, os, sys
import logging 
logging.basicConfig(level=logging.INFO)
HERE = os.path.dirname( __file__ )
import pickle
try:
    import cPickle
except ImportError as err:
    cPickle = pickle

try:
    from numpy import *
except ImportError as err:
    array = None

pygame.display.init()
import OpenGL 
if os.environ.get( 'TEST_NO_ACCELERATE' ):
    OpenGL.USE_ACCELERATE = False
OpenGL.CONTEXT_CHECKING = True
OpenGL.FORWARD_COMPATIBLE_ONLY = False
OpenGL.UNSIGNED_BYTE_IMAGES_AS_STRING = True

from OpenGL._bytes import bytes, _NULL_8_BYTE, unicode, as_8_bit
from OpenGL.GL import *
try:
    glGetError()
except error.NoContext as err:
    # good, should have got this error 
    pass
else:
    print( 'WARNING: Failed to catch invalid context' )
    #raise RuntimeError( """Did not catch invalid context!""" )
from OpenGL import error
from OpenGL.GLU import *
from OpenGL.arrays import arraydatatype
import OpenGL
from OpenGL.extensions import alternate
import ctypes
from OpenGL.GL.framebufferobjects import *
from OpenGL.GL.EXT.multi_draw_arrays import *
from OpenGL.GL.ARB.imaging import *

glMultiDrawElements = alternate( 
    glMultiDrawElementsEXT, glMultiDrawElements, 
)


class Tests( unittest.TestCase ):
    evaluator_ctrlpoints = [[[ -1.5, -1.5, 4.0], [-0.5, -1.5, 2.0], [0.5, -1.5,
        -1.0], [1.5, -1.5, 2.0]], [[-1.5, -0.5, 1.0], [-0.5, -0.5, 3.0], [0.5, -0.5,
        0.0], [1.5, -0.5, -1.0]], [[-1.5, 0.5, 4.0], [-0.5, 0.5, 0.0], [0.5, 0.5,
        3.0], [1.5, 0.5, 4.0]], [[-1.5, 1.5, -2.0], [-0.5, 1.5, -2.0], [0.5, 1.5,
        0.0], [1.5, 1.5, -1.0]]]
    width = height = 300
    def setUp( self ):
        """Set up the operation"""
        
        self.screen = pygame.display.set_mode(
            (self.width,self.height),
            pygame.OPENGL | pygame.DOUBLEBUF,
        )
        
        pygame.display.set_caption('Testing system')
        pygame.key.set_repeat(500,30)
        glMatrixMode (GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(40.0, 300/300., 1.0, 20.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(
            -2,0,3, # eyepoint
            0,0,0, # center-of-view
            0,1,0, # up-vector
        )
        glClearColor( 0,0,.25, 0 )
        glClear( GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT )
    
    def tearDown( self ):
        glFlush()
        pygame.display.flip()
        time.sleep( .25 )
        #raw_input( 'Okay? ' )
    def test_arrayPointer( self ):
        dt = arraydatatype.GLuintArray
        d = dt.zeros( (3,))
        dp = dt.typedPointer( d )
        assert dp[0] == 0 
        assert dp[1] == 0
        assert dp[2] == 0
        dp[1] = 1
        assert dp[1] == 1
        assert d[1] == 1
    def test_ctypes_array( self ):
        color = (GLfloat * 3)( 0,1,0 )
        glColor3fv( color )
    if (not OpenGL.ERROR_ON_COPY) or array:	
        def test_evaluator( self ):
            """Test whether the evaluator functions work"""
            glDisable(GL_CULL_FACE)
            glEnable(GL_MAP2_VERTEX_3)
            glEnable(GL_DEPTH_TEST)
            glEnable(GL_NORMALIZE)
            if array:
                ctrl_points = array( self.evaluator_ctrlpoints,'f')
            else:
                ctrl_points = self.evaluator_ctrlpoints
            glMap2f(GL_MAP2_VERTEX_3, 0, 1, 0, 1, ctrl_points)
            glMapGrid2f(20, 0.0, 1.0, 20, 0.0, 1.0)
            glShadeModel(GL_FLAT)
            glEvalMesh2(GL_FILL, 0, 20, 0, 20)
            glTranslatef( 0,0.001, 0 )
            glEvalMesh2(GL_POINT, 0, 20, 0, 20)
    def test_nurbs_raw( self ):
        """Test nurbs rendering using raw API calls"""
        from OpenGL.raw import GLU 
        knots = (GLfloat* 8) ( 0,0,0,0,1,1,1,1 )
        ctlpoints = (GLfloat*(3*4*4))( -3., -3., -3.,
            -3., -1., -3.,
            -3.,  1., -3.,
            -3.,  3., -3.,

        -1., -3., -3.,
            -1., -1.,  3.,
            -1.,  1.,  3.,
            -1.,  3., -3.,

        1., -3., -3.,
             1., -1.,  3.,
             1.,  1.,  3.,
             1.,  3., -3.,

        3., -3., -3.,
            3., -1., -3.,
             3.,  1., -3.,
             3.,  3., -3. )
        theNurb = gluNewNurbsRenderer()
        GLU.gluBeginSurface(theNurb)
        GLU.gluNurbsSurface(
            theNurb, 
            8, ctypes.byref(knots), 8, ctypes.byref(knots),
            4 * 3, 3, ctypes.byref( ctlpoints ),
            4, 4, GL_MAP2_VERTEX_3
        )
        GLU.gluEndSurface(theNurb)
    if array:
        def test_nurbs_raw_arrays( self ):
            """Test nurbs rendering using raw API calls with arrays"""
            from OpenGL.raw import GLU 
            knots = array( ( 0,0,0,0,1,1,1,1 ), 'f' )
            ctlpoints = array( [[[-3., -3., -3.],
                [-3., -1., -3.],
                [-3.,  1., -3.],
                [-3.,  3., -3.]],

            [[-1., -3., -3.],
                [-1., -1.,  3.],
                [-1.,  1.,  3.],
                [-1.,  3., -3.]],

            [[ 1., -3., -3.],
                [ 1., -1.,  3.],
                [ 1.,  1.,  3.],
                [ 1.,  3., -3.]],

            [[ 3., -3., -3.],
                [ 3., -1., -3.],
                [ 3.,  1., -3.],
                [ 3.,  3., -3.]]], 'f' )
            theNurb = GLU.gluNewNurbsRenderer()
            GLU.gluBeginSurface(theNurb)
            GLU.gluNurbsSurface(
                theNurb, 
                8, knots, 8, knots,
                4 * 3, 3, ctlpoints ,
                4, 4, GL_MAP2_VERTEX_3
            )
            GLU.gluEndSurface(theNurb)
        def test_nurbs( self ):
            """Test nurbs rendering"""
            from OpenGL.raw import GLU 
            def buildControlPoints( ):
                ctlpoints = zeros( (4,4,3), 'f')
                for u in range( 4 ):
                    for v in range( 4):
                        ctlpoints[u][v][0] = 2.0*(u - 1.5)
                        ctlpoints[u][v][1] = 2.0*(v - 1.5);
                        if (u == 1 or u ==2) and (v == 1 or v == 2):
                            ctlpoints[u][v][2] = 3.0;
                        else:
                            ctlpoints[u][v][2] = -3.0;
                return ctlpoints
            controlPoints = buildControlPoints()
            theNurb = GLU.gluNewNurbsRenderer()[0]
            #theNurb = gluNewNurbsRenderer();
            gluNurbsProperty(theNurb, GLU_SAMPLING_TOLERANCE, 25.0);
            gluNurbsProperty(theNurb, GLU_DISPLAY_MODE, GLU_FILL);
            knots= array ([0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0], "f")
            glPushMatrix();
            try:
                glRotatef(330.0, 1.,0.,0.);
                glScalef (0.5, 0.5, 0.5);

                gluBeginSurface(theNurb);
                try:
                    gluNurbsSurface(
                        theNurb,
                        knots, knots,
                        controlPoints,
                        GL_MAP2_VERTEX_3
                    );
                finally:
                    gluEndSurface(theNurb);
            finally:
                glPopMatrix();
    def test_errors( self ):
        """Test for error catching/checking"""
        try:
            glClear( GL_INVALID_VALUE )
        except Exception as err:
            assert err.err == 1281, ("""Expected invalid value (1281)""", err.err)
        else:
            assert not OpenGL.ERROR_CHECKING, """No error on invalid glClear"""
        try:
            glColorPointer(GL_INVALID_VALUE,GL_BYTE,0,None)
        except Exception as err:
            assert err.err == 1281, ("""Expected invalid value (1281)""", err.err)
            assert err.baseOperation, err.baseOperation
            assert err.pyArgs == (GL_INVALID_VALUE, GL_BYTE, 0, None), err.pyArgs
            assert err.cArgs == (GL_INVALID_VALUE, GL_BYTE, 0, None), err.cArgs
        else:
            assert not OpenGL.ERROR_CHECKING, """No error on invalid glColorPointer"""
        try:
            glBitmap(-1,-1,0,0,0,0,as_8_bit(""))
        except Exception as err:
            assert err.err in (1281,1282), ("""Expected invalid value (1281) or invalid operation (1282)""", err.err)
        else:
            assert not OpenGL.ERROR_CHECKING, """No error on invalid glBitmap"""
    def test_quadrics( self ):
        """Test for rendering quadric objects"""
        quad = gluNewQuadric()
        glColor3f( 1,0, 0 )
        gluSphere( quad, 1.0, 16, 16 )
    if not OpenGL.ERROR_ON_COPY:
        def test_simple( self ):
            """Test for simple vertex-based drawing"""
            glDisable( GL_LIGHTING )
            glBegin( GL_TRIANGLES )
            try:
                try:
                    glVertex3f( 0.,1.,0. )
                except Exception:
                    traceback.print_exc()
                glVertex3fv( [-1,0,0] )
                glVertex3dv( [1,0,0] )
                try:
                    glVertex3dv( [1,0,4,5] )
                except ValueError:
                    #Got expected value error (good)
                    assert OpenGL.ARRAY_SIZE_CHECKING, """Should have raised ValueError when doing array size checking"""
                else:
                    assert not OpenGL.ARRAY_SIZE_CHECKING, """Should not have raised ValueError when not doing array size checking"""
            finally:
                glEnd()
            a = glGenTextures( 1 )
            assert a
            b = glGenTextures( 2 )
            assert len(b) == 2
    def test_arbwindowpos( self ):
        """Test the ARB window_pos extension will load if available"""
        from OpenGL.GL.ARB.window_pos import glWindowPos2dARB
        if glWindowPos2dARB:
            glWindowPos2dARB( 0.0, 3.0 )
    def test_getstring( self ):
        assert glGetString( GL_EXTENSIONS )
    if not OpenGL.ERROR_ON_COPY:
        def test_pointers( self ):
            """Test that basic pointer functions work"""
            vertex = GLdouble * 3
            vArray =  vertex * 2
            glVertexPointerd( [[2,3,4,5],[2,3,4,5]] )
            glVertexPointeri( ([2,3,4,5],[2,3,4,5]) )
            glVertexPointers( [[2,3,4,5],[2,3,4,5]] )
            glVertexPointerd( vArray( vertex(2,3,4),vertex(2,3,4) ) )
            myVector = vArray( vertex(2,3,4),vertex(2,3,4) )
            glVertexPointer(
                3,
                GL_DOUBLE,
                0,
                ctypes.cast( myVector, ctypes.POINTER(GLdouble)) 
            )
            
            repr(glVertexPointerb( [[2,3],[4,5]] ))
            glVertexPointerf( [[2,3],[4,5]] )
            assert arrays.ArrayDatatype.dataPointer( None ) == None
            glVertexPointerf( None )
            
            glNormalPointerd( [[2,3,4],[2,3,4]] )
            glNormalPointerd( None )
        
            glTexCoordPointerd( [[2,3,4],[2,3,4]] )
            glTexCoordPointerd( None )
        
            glColorPointerd( [[2,3,4],[2,3,4]] )
            glColorPointerd( None )
        
            glEdgeFlagPointerb( [0,1,0,0,1,0] )
            glEdgeFlagPointerb( None )
        
            glIndexPointerd( [0,1,0,0,1,0] )
            glIndexPointerd( None )
            
            glColor4fv( [0,0,0,1] )
            
            # string data-types...
            import struct
            s = struct.pack( '>iiii', 2,3,4,5 ) * 2
            glVertexPointer( 4,GL_INT,0,s )
        TESS_TEST_SHAPE = [
                [191,   0],
                [ 191, 1480],
                [ 191, 1480],
                [ 401, 1480],
                [ 401, 1480],
                [401,   856],
                [401,   856],
                [1105,  856],
                [1105,  856],
                [1105, 1480],
                [1105, 1480],
                [1315, 1480],
                [1315, 1480],
                [1315,    0],
                [1315,    0],
                [1105,    0],
                [1105,    0],
                [1105,  699],
                [1105,  699],
                [401,   699],
                [401,   699],
                [401,     0],
                [401,     0],
                [191,     0],
                [191,     0],
                [191,     0],
            ]
        def test_tess(self ):
            """Test that tessellation works"""
            glDisable( GL_LIGHTING )
            glColor3f( 1,1,1 )
            glNormal3f( 0,0,1 )
            def begin( *args ):
                return glBegin( *args )
            def vertex( *args ):
                return glVertex3dv( *args )
            def end( *args ):
                return glEnd( *args )
            def combine( coords, vertex_data, weight):
                return coords
            tobj = gluNewTess()
            gluTessCallback(tobj, GLU_TESS_BEGIN, begin);
            gluTessCallback(tobj, GLU_TESS_VERTEX, vertex); 
            gluTessCallback(tobj, GLU_TESS_END, end); 
            gluTessCallback(tobj, GLU_TESS_COMBINE, combine); 
            gluTessBeginPolygon(tobj, None); 
            gluTessBeginContour(tobj);
            for (x,y) in self.TESS_TEST_SHAPE:
                vert = (x,y,0.0)
                gluTessVertex(tobj, vert, vert);
            gluTessEndContour(tobj); 
            gluTessEndPolygon(tobj);
        def test_texture( self ):
            """Test texture (requires OpenGLContext and PIL)"""
            try:
                from OpenGLContext import texture
                import Image 
                from OpenGL.GLUT import glutSolidTeapot
            except ImportError:
                pass
            else:
                assert glutSolidTeapot
                glEnable( GL_TEXTURE_2D )
                ourTexture = texture.Texture(
                    Image.open( os.path.join( HERE, 'yingyang.png') )
                )
                ourTexture()
                
                result = glGetTexImageub( GL_TEXTURE_2D,0,GL_RGBA )
                assert isinstance( result, bytes ), type(result)
                result = glGetTexImage( GL_TEXTURE_2D,0,GL_RGBA, GL_UNSIGNED_BYTE )
                assert isinstance( result, bytes ), type(result)
                
                glEnable( GL_LIGHTING )
                glEnable( GL_LIGHT0 )
                glBegin( GL_TRIANGLES )
                try:
                    try:
                        glTexCoord2f( .5, 1 )
                        glVertex3f( 0.,1.,0. )
                    except Exception:
                        traceback.print_exc()
                    glTexCoord2f( 0, 0 )
                    glVertex3fv( [-1,0,0] )
                    glTexCoord2f( 1, 0 )
                    glVertex3dv( [1,0,0] )
                    try:
                        glVertex3dv( [1,0] )
                    except ValueError:
                        assert OpenGL.ARRAY_SIZE_CHECKING, """Should have raised ValueError when doing array size checking"""
                    else:
                        assert not OpenGL.ARRAY_SIZE_CHECKING, """Should not have raised ValueError when not doing array size checking"""
                finally:
                    glEnd()
    if array:
        def test_numpyConversion( self ):
            """Test that we can run a numpy conversion from double to float for glColorArray"""
            a = arange( 0,1.2, .1, 'd' ).reshape( (-1,3 ))
            glEnableClientState(GL_VERTEX_ARRAY)
            try:
                glColorPointerf( a )
                glColorPointerd( a )
            finally:
                glDisableClientState( GL_VERTEX_ARRAY )
    def test_constantPickle( self ):
        """Test that our constants can be pickled/unpickled properly"""
        for p in pickle,cPickle:
            v = p.loads( p.dumps( GL_VERTEX_ARRAY ))
            assert v == GL_VERTEX_ARRAY, (v,GL_VERTEX_ARRAY)
            assert v.name == GL_VERTEX_ARRAY.name, v.name 
    
    if array and not OpenGL.ERROR_ON_COPY:
        def test_copyNonContiguous( self ):
            """Test that a non-contiguous (transposed) array gets applied as a copy"""
            glMatrixMode(GL_MODELVIEW)
            glPushMatrix( )
            try:
                transf = identity(4, dtype=float32)
                # some arbitrary transformation...
                transf[0,3] = 2.5
                transf[2,3] = -80
                
                # what do we get with the un-transposed version...
                glMatrixMode(GL_MODELVIEW)
                glLoadIdentity()
                glMultMatrixf(transf)
                untransposed = glGetFloatv(GL_MODELVIEW_MATRIX)
                # now transposed...

                # with a copy it works...
                t2 = transf.transpose().copy()
                # This doesn't work:
                glLoadIdentity()
                glMultMatrixf(t2)
                # This does work:
                #glMultMatrixf(transf.transpose().copy())
                transposed = glGetFloatv(GL_MODELVIEW_MATRIX)

                assert not allclose( transposed, untransposed ), (transposed, untransposed)
                
                t2 = transf.transpose()
                # This doesn't work:
                glLoadIdentity()
                glMultMatrixf(t2)
                # This does work:
                #glMultMatrixf(transf.transpose().copy())
                transposed = glGetFloatv(GL_MODELVIEW_MATRIX)
                
                assert not allclose( transposed, untransposed ), (transposed, untransposed)
            finally:
                glMatrixMode(GL_MODELVIEW)
                glPopMatrix()
    def test_nullTexture( self ):
        """Test that we can create null textures"""
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB8, 512, 512, 0, GL_RGB, GL_INT, None)
    
    def test_nonFloatColor( self ):
        """Test that we handle non-floating-point colour inputs"""
        for notFloat,shouldWork in ((0,True), (object(),False), (object,False)):
            try:
                glColor4f( 0,1,1,notFloat )
            except Exception:
                if shouldWork:
                    raise 
            else:
                if not shouldWork:
                    raise RuntimeError( """Expected failure for non-float value %s, succeeded"""%( notFloat, ))
    someData = [ (0,255,0)]
    def test_passBackResults( self ):
        """Test ALLOW_NUMPY_SCALARS to allow numpy scalars to be passed in"""
        textures = glGenTextures(2)
        glBindTexture( GL_TEXTURE_2D, textures[0] )
    if array:
        def test_arrayTranspose( self ):
            m = glGetFloatv( GL_MODELVIEW_MATRIX )
            glMatrixMode( GL_MODELVIEW )
            glLoadIdentity()

            t = eye(4)
            t[3,0] = 20.0

            # the following glMultMatrixf call ignored this transpose
            t = t.T
            if OpenGL.ERROR_ON_COPY:
                t = ascontiguousarray( t )
            
            glMultMatrixd( t )

            m = glGetFloatv( GL_MODELVIEW_MATRIX )
            assert allclose( m[-1], [0,0,0,1] ), m
        def test_glAreTexturesResident( self ):
            """Test that PyOpenGL api for glAreTexturesResident is working
            
            Note: not currently working on AMD64 Linux for some reason
            """
            textures = glGenTextures(2)
            residents = []
            data = array( self.someData,'i' )
            for texture in textures:
                glBindTexture( GL_TEXTURE_2D,int(texture) )
                glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB8, 1, 1, 0, GL_RGB, GL_INT, data)
                residents.append(
                    glGetTexParameteriv(GL_TEXTURE_2D, GL_TEXTURE_RESIDENT )
                )
            glGetError()
            result = glAreTexturesResident( textures)
            assert len(result) == 2
            for (tex,expected,found) in zip( textures, residents, result ):
                if expected != found:
                    print(('Warning: texture %s residence expected %s got %s'%( tex, expected, found )))
    def test_glreadpixelsf( self ):
        """Issue #1979002 crash due to mis-calculation of resulting array size"""
        width,height = self.width, self.height
        readback_image1 = glReadPixelsub(0,0,width,height,GL_RGB)
        assert readback_image1 is not None
        readback_image2 = glReadPixelsf(0,0,width,height,GL_RGB)
        assert readback_image2 is not None
    def test_glreadpixels_is_string( self ):
        """Issue #1959860 incompatable change to returning arrays reversed"""
        width,height = self.width, self.height
        readback_image1 = glReadPixels(0,0,width,height,GL_RGB, GL_UNSIGNED_BYTE)
        assert isinstance( readback_image1, bytes ), type( readback_image1 )
        readback_image1 = glReadPixels(0,0,width,height,GL_RGB, GL_BYTE)
        assert not isinstance( readback_image1, bytes ), type(readback_image2)
    
    if array:
        def test_glreadpixels_warray( self ):
            """SF#1311265 allow passing in the array object"""
            width,height = self.width, self.height
            data = zeros( (width,height,3), 'B' )
            image1 = glReadPixelsub(0,0,width,height,GL_RGB,array=data)
            assert image1 is not None
        
        # currently crashes in py_buffer operation, so reverted to raw numpy 
        # api
        def test_mmap_data( self ):
            """Test that we can use mmap data array
            
            If we had a reasonable lib that dumped raw image data to a shared-mem file
            we might be able to use this for movie display :) 
            """
            fh = open( 'mmap-test-data.dat', 'wb+' )
            fh.write( _NULL_8_BYTE*(32*32*3+1))
            fh.flush()
            fh.close()
            # using memmap here...
            data = memmap( 'mmap-test-data.dat' )
            for i in range( 0,255,2 ):
                glDrawPixels( 32,32, GL_RGB, GL_UNSIGNED_BYTE, data, )
                glFlush()
                pygame.display.flip()
                data[::2] = i
                time.sleep( 0.001 )
    
    if array:
        def test_vbo( self ):
            """Test utility vbo wrapper"""
            from OpenGL.arrays import vbo
            assert vbo.get_implementation()
            points = array( [
                [0,0,0],
                [0,1,0],
                [1,.5,0],
                [1,0,0],
                [1.5,.5,0],
                [1.5,0,0],
            ], dtype='d')
            indices = array(
                range(len(points)),
                ['i','I'][bool(OpenGL.ERROR_ON_COPY)], # test coercion if we can
            )
            d = vbo.VBO(points)
            glDisable( GL_CULL_FACE )
            glNormal3f( 0,0,1 )
            glColor3f( 1,1,1 )
            glEnableClientState(GL_VERTEX_ARRAY)
            try:
                for x in range( 1, 255, 10 ):
                    d.bind()
                    try:
                        glVertexPointerd( d )
                        glDrawElements( GL_LINE_LOOP, len(indices), GL_UNSIGNED_INT, indices )
                    finally:
                        d.unbind()
                    lastPoint = array( [[1.5,(1/255.) * float(x),0]] )
                    d[-2:-1] = lastPoint
                    glFlush()
                    pygame.display.flip()
                    glClear( GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT )
                    time.sleep( 0.001 )
            finally:
                glDisableClientState( GL_VERTEX_ARRAY )
            # bug report from Dan Helfman, delete shouldn't cause 
            # errors if called explicitly
            d.delete()
    def test_fbo( self ):
        """Test that we support framebuffer objects
        
        http://www.gamedev.net/reference/articles/article2331.asp
        """
        if not glGenFramebuffers:
            print( 'No Frame Buffer Support!' )
            return False
        width = height = 128
        fbo = glGenFramebuffers(1)
        glBindFramebuffer(GL_FRAMEBUFFER, fbo)
        depthbuffer = glGenRenderbuffers(1 )
        glBindRenderbuffer(GL_RENDERBUFFER, depthbuffer)
        glRenderbufferStorage(GL_RENDERBUFFER, GL_DEPTH_COMPONENT24, width, height)
        glFramebufferRenderbuffer(
            GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, GL_RENDERBUFFER, 
            depthbuffer
        )
        img = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, img)
        # NOTE: these lines are *key*, without them you'll likely get an unsupported format error,
        # ie. GL_FRAMEBUFFER_UNSUPPORTED
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST);
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST);
        glTexImage2D(
            GL_TEXTURE_2D, 0, GL_RGB8,  
            width, height, 0, GL_RGB, 
            GL_INT, 
            None # no data transferred
        ) 
        glFramebufferTexture2D(
            GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, 
            img, 
            0 # mipmap level, normally 0
        )
        status = glCheckFramebufferStatus(GL_FRAMEBUFFER)
        assert status == GL_FRAMEBUFFER_COMPLETE, status
        glBindFramebuffer(GL_FRAMEBUFFER, fbo)
        glPushAttrib(GL_VIEWPORT_BIT) # viewport is shared with the main context
        try:
            glViewport(0,0,width, height)
            
            # rendering to the texture here...
            glColor3f( 1,0,0 )
            glNormal3f( 0,0,1 )
            glBegin( GL_QUADS )
            for v in [[0,0,0],[0,1,0],[1,1,0],[1,0,0]]:
                glColor3f( *v )
                glVertex3d( *v )
            glEnd()
        finally:
            glPopAttrib(); # restore viewport
        glBindFramebuffer(GL_FRAMEBUFFER, 0) # unbind
        
        glBindTexture(GL_TEXTURE_2D, img)
        
        glEnable( GL_TEXTURE_2D )
        
        # rendering with the texture here...
        glColor3f( 1,1,1 )
        glNormal3f( 0,0,1 )
        glDisable( GL_LIGHTING )
        glBegin( GL_QUADS )
        try:
            for v in [[0,0,0],[0,1,0],[1,1,0],[1,0,0]]:
                glTexCoord2f( *v[:2] )
                glVertex3d( *v )
        finally:
            glEnd()
    def test_gl_1_2_support( self ):
        if glBlendColor:
            glBlendColor( .3, .4, 1.0, .3 )
            print('OpenGL 1.2 support')
    if array:
        def test_glmultidraw( self ):
            """Test that glMultiDrawElements works, uses glDrawElements"""
            if glMultiDrawElements:
                points = array([
                    (i,0,0) for i in range( 8 )
                ] + [
                    (i,1,0) for i in range( 8 )
                ], 'd')
                indices = array([
                    [0,8,9,1, 2,10,11,3,],
                    [4,12,13,5,6,14,15,7],
                ],'B')
                index_pointers = arrays.GLvoidpArray.zeros( (2,))
                index_pointers[0] = arrays.GLbyteArray.dataPointer( indices )
                index_pointers[1] = arrays.GLbyteArray.dataPointer( indices[1] )
                counts = [ len(x) for x in indices ]
                if OpenGL.ERROR_ON_COPY:
                    counts = (GLuint*len(counts))(*counts)
                glEnableClientState( GL_VERTEX_ARRAY )
                glDisableClientState( GL_COLOR_ARRAY )
                glDisableClientState( GL_NORMAL_ARRAY )
                try:
                    glVertexPointerd( points )
                    glDisable( GL_LIGHTING )
                    try:
                        glMultiDrawElements(GL_QUAD_STRIP, counts, GL_UNSIGNED_BYTE, index_pointers, 2)
                    finally:
                        glEnable( GL_LIGHTING )
                finally:
                    glDisableClientState( GL_VERTEX_ARRAY )
            else:
                print('No multi_draw_arrays support')
    def test_glDrawBuffers_list( self ):
        """Test that glDrawBuffers with list argument doesn't crash"""
        a_type = GLenum*2
        args = a_type(
            GL_COLOR_ATTACHMENT0,
            GL_COLOR_ATTACHMENT1,
        )
        try:
            glDrawBuffers( 2, args )
        except GLError as err:
            assert err.err == GL_INVALID_OPERATION, err
    def test_glDrawBuffers_list_valid( self ):
        """Test that glDrawBuffers with list argument where value is set"""
        previous = glGetIntegerv( GL_READ_BUFFER )
        fbo = glGenFramebuffers(1)
        glBindFramebuffer(GL_FRAMEBUFFER, fbo)
        try:
            img1,img2 = glGenTextures(2)
            for img in img1,img2:
                glBindTexture( GL_TEXTURE_2D, img )
                glTexImage2D(
                    GL_TEXTURE_2D, 0, GL_RGB8,  
                    300, 300, 0, GL_RGB, 
                    GL_INT, 
                    None # no data transferred
                ) 
            

            glFramebufferTexture2D(
                GL_FRAMEBUFFER, 
                GL_COLOR_ATTACHMENT0, 
                GL_TEXTURE_2D, img1, 0
            )
            glFramebufferTexture2D(
                GL_FRAMEBUFFER, 
                GL_COLOR_ATTACHMENT1, 
                GL_TEXTURE_2D, img2, 0
            )
            a_type = GLenum*2
            drawingBuffers = a_type(
                GL_COLOR_ATTACHMENT0, 
                GL_COLOR_ATTACHMENT1,
            )
            glDrawBuffers(2, drawingBuffers )
            try:
                checkFramebufferStatus()
            except error.GLError:
                pass
            else:
                glReadBuffer( GL_COLOR_ATTACHMENT1 )
                pixels = glReadPixels( 0,0, 10,10, GL_RGB, GL_UNSIGNED_BYTE )
                assert len(pixels) == 300, len(pixels)
        finally:
            glBindFramebuffer( GL_FRAMEBUFFER, 0 )
        
        glReadBuffer( previous )
        
    def test_enable_histogram( self ):
        if glInitImagingARB():
            glHistogram(GL_HISTOGRAM, 256, GL_LUMINANCE, GL_FALSE)
            glEnable( GL_HISTOGRAM )
            glDisable( GL_HISTOGRAM )
        else:
            print('No ARB imaging extension')
    if not OpenGL.ERROR_ON_COPY:
        def test_gluNurbsCurve( self ):
            """Test that gluNurbsCurve raises error on invalid arguments"""
            nurb = gluNewNurbsRenderer()
            gluBeginCurve( nurb )
            if OpenGL.ERROR_CHECKING:
                self.assertRaises( error.GLUerror,
                    gluNurbsCurve,
                        nurb, 
                        [0, 1.0],
                        [[0,0,0],[1,0,0],[1,1,0]],
                        GL_MAP1_VERTEX_3,
                )
                self.assertRaises( error.GLUerror,
                    gluNurbsCurve,
                        nurb, 
                        [],
                        [[0,0,0],[1,0,0],[1,1,0]],
                        GL_MAP1_VERTEX_3,
                )
                self.assertRaises( error.GLUerror,
                    gluNurbsCurve,
                        nurb, 
                        [],
                        [],
                        GL_MAP1_VERTEX_3,
                )
    def test_get_version( self ):
        from OpenGL.extensions import hasGLExtension
        if hasGLExtension( 'GL_VERSION_GL_2_0' ):
            assert glShaderSource
            assert glUniform1f
        else:
            assert not glShaderSource
            assert not glUniform1f
    
    def test_lookupint( self ):
        from OpenGL.raw.GL import _lookupint 
        l = _lookupint.LookupInt( GL_NUM_COMPRESSED_TEXTURE_FORMATS, GLint )
        result = int(l)
        assert result, "No compressed textures on this platform? that seems unlikely"
    
    def test_glget( self ):
        """Test that we can run glGet... on registered constants without crashing..."""
        from OpenGL.raw.GL import _glgets
        for key,value in _glgets._glget_size_mapping.items():
            print( 'Trying glGetFloatv( 0x%x )'%(key,))
            if key == 0x92c1: # GL_ATOMIC_COUNTER_BUFFER_BINDING crashes intel hardware... sigh...
                continue
            try:
                result = glGetFloatv( key )
            except error.GLError as err:
                if err.err == GL_INVALID_ENUM:
                    pass
                elif err.err == GL_INVALID_OPERATION:
                    if key == 0x882d: # gl draw buffer 
                        pass
                else:
                    raise 
            else:
                if value == (1,) and OpenGL.SIZE_1_ARRAY_UNPACK:
                    result = float(result)
                else:
                    assert ArrayDatatype.dimensions( result ) == value, result
    def test_max_compute_work_group_invocations(self):
        from OpenGL.extensions import hasGLExtension
        if hasGLExtension( 'GL_ARB_compute_shader' ):
            assert glGetIntegerv( GL_MAX_COMPUTE_WORK_GROUP_INVOCATIONS )
    
    def test_tess_collection( self ):
        """SF#2354596 tessellation combine results collected"""
        all_vertices = []
        combinations = []
        def start(*args):
            pass
        def stop(*args):
            pass
        def tessvertex(vertex_data, polygon_data=None):
            # polygon data *should* be collected here
            #assert polygon_data is all_vertices, polygon_data
            all_vertices.append(vertex_data)
            #collected.append( vertex_data )
            return polygon_data
        def tesscombine(coords, vertex_data, weights,_=None):
            new = (True,coords)
            combinations.append( coords )
            return new

        def tessedge(flag,*args,**named):
            pass	# dummy
        def tesserr( enum ):
            raise RuntimeError( gluErrorString( enum ) )

        # set up tessellator in CSG intersection mode
        tess=gluNewTess()
        gluTessProperty(tess, GLU_TESS_WINDING_RULE, GLU_TESS_WINDING_ABS_GEQ_TWO)
        gluTessCallback(tess, GLU_TESS_BEGIN, start)
        gluTessCallback(tess, GLU_TESS_END, stop)
        gluTessCallback(tess, GLU_TESS_EDGE_FLAG, tessedge)	# no strips
        gluTessCallback(tess, GLU_TESS_VERTEX, tessvertex)
        gluTessCallback(tess, GLU_TESS_ERROR, tesserr )
        gluTessCallback(tess, GLU_TESS_COMBINE, tesscombine)

        gluTessBeginPolygon(tess, all_vertices)
        try:
            for contour in [
                # first square
                [(-1,0,-1),(1,0,-1),(1,0,1),(-1,0,1)],
                # second intersects the first
                [(.5,0,-.5),(1.5,0,-.5),(1.5,0,.5),(.5,0,.5)],
            ]:
                
                gluTessBeginContour(tess)
                try:
                    for point in contour:
                        if array:
                            if OpenGL.ERROR_ON_COPY:
                                point = array( point, 'd' )
                            else:
                                point = array( point, 'f' )
                        else: 
                            point = (GLdouble*3)(*point)
                        gluTessVertex( tess, point, (False,point))
                finally:
                    gluTessEndContour(tess)
        finally:
            gluTessEndPolygon(tess)

        # Show collected triangle vertices :-
        # Original input vertices are marked as False.
        # Vertices generated in combine callback are marked as True.
        assert all_vertices, "Nothing collected"
        combined,original = [x for x in all_vertices if x[0]], [x for x in all_vertices if not x[0]]
        
        assert combined, ("No combined vertices", all_vertices )
        assert original, ("No original vertices", all_vertices )
        assert len(combinations) == 2, combinations
    
    def test_tess_cb_traditional( self ):
        outline = [
            [191,   0],
            [ 191, 1480],
            [ 191, 1480],
            [ 401, 1480],
            [ 401, 1480],
            [401,   856],
            [401,   856],
            [1105,  856],
            [1105,  856],
            [1105, 1480],
            [1105, 1480],
            [1315, 1480],
            [1315, 1480],
            [1315,    0],
            [1315,    0],
            [1105,    0],
            [1105,    0],
            [1105,  699],
            [1105,  699],
            [401,   699],
            [401,   699],
            [401,     0],
            [401,     0],
            [191,     0],
            [191,     0],
            [191,     0],
        ]
        scale = 1200.
        self.tess = gluNewTess()
        gluTessCallback(self.tess, GLU_TESS_BEGIN, glBegin)
        def test( t, polyData=None ):
            glNormal( 0,0, -1 )
            glColor3f( t[0],t[1],t[2] )
            return glVertex3f( t[0],t[1],t[2])
        gluTessCallback(self.tess, GLU_TESS_VERTEX_DATA, test)
        gluTessCallback(self.tess, GLU_TESS_END, glEnd);
        combined = []
        def combine( points, vertices, weights ):
            #print 'combine called', points, vertices, weights
            combined.append( points )
            return points
        gluTessCallback(self.tess, GLU_TESS_COMBINE, combine)
        gluTessBeginPolygon( self.tess, None )
        try:
            gluTessBeginContour( self.tess )
            try:
                for (x,y) in outline:
                    if array:
                        vertex = array((x/scale,y/scale,0.0),'d')
                    else:
                        vertex = (GLdouble*3)(x/scale,y/scale,0.0)
                    gluTessVertex(self.tess, vertex, vertex)
            finally:
                gluTessEndContour( self.tess )
        finally:
            gluTessEndPolygon(self.tess)
        
    
    def test_get_boolean_bitmap( self ):
        # should not raise error
        glGetBoolean(GL_TEXTURE_2D)
    if array:
        def test_draw_bitmap_pixels( self ):
            """SF#2152623 Drawing pixels as bitmaps (bits)"""
            # this core-dumps on Mesa Intel on Ubuntu 15.04 :(
            # nosetest skip would be more appropriate
            return False
            pixels = array([0,0,0,0,0,0,0,0],'B')
            glDrawPixels( 8,8, GL_COLOR_INDEX, GL_BITMAP, pixels )
    
    def test_glCallLists_twice2( self ):
        """SF#2829309 report that glCallLists doubles operation"""
        glRenderMode (GL_RENDER)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(40.0, 1.0, 1.0, 10.0)
        glMatrixMode (GL_MODELVIEW)
        glLoadIdentity ()
        glTranslatef (0, 0, -3)
        first = glGenLists( 2 )
        second = first+1

        glNewList(first, GL_COMPILE_AND_EXECUTE)
        glInitNames ()
        if not OpenGL.ERROR_ON_COPY:
            glCallLists([second]) # replace with gCallList(2)
        else:
            lists = (GLuint * 1)()
            lists[0] = second
            glCallLists(lists)
        #glCallList(second)
        glEndList ()

        glNewList(second, GL_COMPILE)
        glPushName (1)
        glBegin (GL_POINTS)
        glVertex3f (0, 0, 0)
        glEnd ()
        glEndList ()
        glCallList( second )
        glPopName()
        depth = glGetIntegerv( GL_NAME_STACK_DEPTH )
        assert depth in (0,(0,)), depth # have popped, but even then, were' not in the mode...

        glSelectBuffer (100)
        glRenderMode (GL_SELECT)
        glCallList(1)
        depth = glGetIntegerv( GL_NAME_STACK_DEPTH )
        assert depth in (1,(1,)), depth # should have a single record
        glPopName()
        records = glRenderMode (GL_RENDER)
        # reporter says sees two records, Linux sees none, Win32 sees 1 :(
        assert len(records) == 1, records
    
    def test_get_max_tex_units( self ):
        """SF#2895081 glGetIntegerv( GL_MAX_TEXTURE_IMAGE_UNITS )"""
        units = glGetIntegerv( GL_MAX_TEXTURE_IMAGE_UNITS )
        assert units
    
    def test_bytes_array_support( self ):
        color = b'\000'*12
        glColor3fv( color )
    if (OpenGL.USE_ACCELERATE) or (sys.version_info[:2] < (3,0)):
        # ctypes based buffer api does not work on Python 3.x
        def test_bytearray_support( self ):
            import struct 
            data = struct.pack( 'fff', .5, .4, .3 )
            color = bytearray( data )
            glColor3fv( color )
        if sys.version_info[:2] > (2,6):
            # no memory view object...
            def test_memoryview_support( self ):
                color = bytearray( b'\000'*12 )
                mem = memoryview( color )
                glColor3fv( mem )
        def test_buffer_api_basic(self):
            import array as silly_array
            structures = [
                (b'this and that',13,1,True,1,b'B',[13],[1]),
            ]
            if sys.version_info[:2] >= (2,7):
                structures.append(
                    # on Python 3.4 we do *not* get the (3) prefix :(
                    ((GLint * 3)( 1,2,3 ),12,4,False,1,[b'(3)<i',b'(3)<l',b'<i'],[3],None),
                )
            
            if sys.version_info[:2] >= (3,0):
                # only supports buffer protocol in 3.x
                structures.extend([
                    (silly_array.array('I',[1,2,3]),12,4,False,1,b'I',[3],[4]),
                ])
            try:
                structures.append( (memoryview(b'this'),4,1,True,1,b'B',[4],[1]) )
            except NameError:
                # Python 2.6 doesn't have memory view 
                pass
            try:
                if array:
                    structures.extend( [
                        (arange(0,9,dtype='I').reshape((3,3)),36,4,False,2,b'I',[3,3],[12,4]),
                        (arange(0,9,dtype='I').reshape((3,3))[:,1],12,4,False,1,b'I',[3],[12]),
                    ])
            except NameError:
                # Don't have numpy installed...
                pass
            
            from OpenGL.arrays import _buffers
            for object,length,itemsize,readonly,ndim,format,shape,strides in structures:
                buf = _buffers.Py_buffer.from_object( object, _buffers.PyBUF_STRIDES|_buffers.PyBUF_FORMAT )
                with buf:
                    assert buf.len == length, (object,length,buf.len)
                    assert buf.itemsize == itemsize, (object,itemsize,buf.itemsize)
                    assert buf.readonly == readonly, (object,readonly,buf.readonly)
                    assert buf.ndim == ndim, (object,ndim,buf.ndim)
                    if isinstance( format, list):
                        assert buf.format in format, (object,format,buf.format)
                    else:
                        assert buf.format == format, (object,format,buf.format)
                    assert buf.shape[:buf.ndim] == shape, (object, shape, buf.shape[:buf.ndim])
                    assert buf.dims == shape, (object, shape, buf.dims )
                    assert buf.buf 
                    if strides is None:
                        assert not buf.strides 
                    else:
                        assert buf.strides[:buf.ndim] == strides, (object, strides, buf.strides[:buf.ndim])
                assert buf.obj == None, buf.obj
                del buf
    
    def test_glGenTextures( self ):
        texture = glGenTextures(1)
        assert texture
    
    def test_void_dp_for_void_dp_is_self( self ):
        array = ctypes.c_voidp( 12 )
        translated = ArrayDatatype.voidDataPointer( array )
        assert translated.value == array.value, translated
    
    def test_orinput_handling( self ):
        x = glGenVertexArrays(1)
        x = int(x) # check that we got x as an integer-compatible value
        x2 = GLuint()
        r_value = glGenVertexArrays( 1, x2 )
        assert x2.value, x2.value
        assert r_value
        
        color = glGetFloatv( GL_FOG_COLOR )
        color2 = (GLfloat *4)()
        glGetFloatv( GL_FOG_COLOR, color2 )
        for a,b in zip( color,color2 ):
            assert a==b, (color,color2)
    
    def test_params_python3_strings( self ):
        try:
            glGetUniformBlockIndex( 0, unicode("Moo") )
        except ArgumentError:
            assert OpenGL.ERROR_ON_COPY, """Shouldn't have raised error on copy for unicode"""
        except TypeError:
            raise
        except GLError:
            # expected error, as we don't have a shader there...
            pass
    
    def test_get_read_fb_binding( self ):
        glGetInteger(GL_READ_FRAMEBUFFER_BINDING)
    
    def test_shader_compile_string( self ):
        shader = glCreateShader(GL_VERTEX_SHADER)
        
        def glsl_version():
            """Parse GL_SHADING_LANGUAGE_VERSION into [int(major),int(minor)]"""
            version = glGetString( GL_SHADING_LANGUAGE_VERSION )
            version = [int(x) for x in version.split(as_8_bit('.'))[:2]]
            return version 
        if glsl_version() < [3,3]:
            return
        SAMPLE_SHADER = '''#version 330
        void main() { gl_Position = vec4(0,0,0,0);}'''
        if OpenGL.ERROR_ON_COPY:
            SAMPLE_SHADER = as_8_bit( SAMPLE_SHADER )
        glShaderSource(shader, SAMPLE_SHADER)
        glCompileShader(shader)
        if not bool(glGetShaderiv(shader, GL_COMPILE_STATUS)) == True:
            print('Info log:')
            print(glGetShaderInfoLog(shader))
            assert False, """Failed to compile"""
    
    def test_gen_framebuffers_twice( self ):
        glGenFramebuffersEXT(1)
        f1 = glGenFramebuffersEXT(1)
        f2 = glGenFramebuffersEXT(1)
        assert f1 != f2, (f1,f2)
        glBindFramebufferEXT(GL_FRAMEBUFFER_EXT, f2)
        glBindFramebufferEXT(GL_FRAMEBUFFER_EXT, 0)
    
    def test_compressed_data(self):
        from OpenGL.extensions import hasGLExtension
        if hasGLExtension( 'GL_EXT_texture_compression_s3tc' ):
            from OpenGL.GL.EXT import texture_compression_s3tc as s3tc
            texture = glGenTextures(1)
            glEnable( GL_TEXTURE_2D )
            image_type = GLubyte *256*256
            image = image_type()
            glCompressedTexImage2D(
                GL_TEXTURE_2D, 0, 
                s3tc.GL_COMPRESSED_RGBA_S3TC_DXT5_EXT, 
                256, 256, 0, 
                image
            )
            assert texture
        
        
if __name__ == "__main__":
    logging.basicConfig( level=logging.INFO )
    unittest.main()
    pygame.display.quit()
    pygame.quit()
