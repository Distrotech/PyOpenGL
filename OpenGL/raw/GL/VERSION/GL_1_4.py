'''OpenGL extension VERSION.GL_1_4

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/VERSION/GL_1_4.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_VERSION_GL_1_4'
GL_BLEND_DST_RGB = constant.Constant( 'GL_BLEND_DST_RGB', 0x80C8 )
GL_BLEND_SRC_RGB = constant.Constant( 'GL_BLEND_SRC_RGB', 0x80C9 )
GL_BLEND_DST_ALPHA = constant.Constant( 'GL_BLEND_DST_ALPHA', 0x80CA )
GL_BLEND_SRC_ALPHA = constant.Constant( 'GL_BLEND_SRC_ALPHA', 0x80CB )
GL_POINT_SIZE_MIN = constant.Constant( 'GL_POINT_SIZE_MIN', 0x8126 )
GL_POINT_SIZE_MAX = constant.Constant( 'GL_POINT_SIZE_MAX', 0x8127 )
GL_POINT_FADE_THRESHOLD_SIZE = constant.Constant( 'GL_POINT_FADE_THRESHOLD_SIZE', 0x8128 )
GL_POINT_DISTANCE_ATTENUATION = constant.Constant( 'GL_POINT_DISTANCE_ATTENUATION', 0x8129 )
GL_GENERATE_MIPMAP = constant.Constant( 'GL_GENERATE_MIPMAP', 0x8191 )
GL_GENERATE_MIPMAP_HINT = constant.Constant( 'GL_GENERATE_MIPMAP_HINT', 0x8192 )
GL_DEPTH_COMPONENT16 = constant.Constant( 'GL_DEPTH_COMPONENT16', 0x81A5 )
GL_DEPTH_COMPONENT24 = constant.Constant( 'GL_DEPTH_COMPONENT24', 0x81A6 )
GL_DEPTH_COMPONENT32 = constant.Constant( 'GL_DEPTH_COMPONENT32', 0x81A7 )
GL_MIRRORED_REPEAT = constant.Constant( 'GL_MIRRORED_REPEAT', 0x8370 )
GL_FOG_COORDINATE_SOURCE = constant.Constant( 'GL_FOG_COORDINATE_SOURCE', 0x8450 )
GL_FOG_COORDINATE = constant.Constant( 'GL_FOG_COORDINATE', 0x8451 )
GL_FRAGMENT_DEPTH = constant.Constant( 'GL_FRAGMENT_DEPTH', 0x8452 )
GL_CURRENT_FOG_COORDINATE = constant.Constant( 'GL_CURRENT_FOG_COORDINATE', 0x8453 )
GL_FOG_COORDINATE_ARRAY_TYPE = constant.Constant( 'GL_FOG_COORDINATE_ARRAY_TYPE', 0x8454 )
GL_FOG_COORDINATE_ARRAY_STRIDE = constant.Constant( 'GL_FOG_COORDINATE_ARRAY_STRIDE', 0x8455 )
GL_FOG_COORDINATE_ARRAY_POINTER = constant.Constant( 'GL_FOG_COORDINATE_ARRAY_POINTER', 0x8456 )
GL_FOG_COORDINATE_ARRAY = constant.Constant( 'GL_FOG_COORDINATE_ARRAY', 0x8457 )
GL_COLOR_SUM = constant.Constant( 'GL_COLOR_SUM', 0x8458 )
GL_CURRENT_SECONDARY_COLOR = constant.Constant( 'GL_CURRENT_SECONDARY_COLOR', 0x8459 )
GL_SECONDARY_COLOR_ARRAY_SIZE = constant.Constant( 'GL_SECONDARY_COLOR_ARRAY_SIZE', 0x845A )
GL_SECONDARY_COLOR_ARRAY_TYPE = constant.Constant( 'GL_SECONDARY_COLOR_ARRAY_TYPE', 0x845B )
GL_SECONDARY_COLOR_ARRAY_STRIDE = constant.Constant( 'GL_SECONDARY_COLOR_ARRAY_STRIDE', 0x845C )
GL_SECONDARY_COLOR_ARRAY_POINTER = constant.Constant( 'GL_SECONDARY_COLOR_ARRAY_POINTER', 0x845D )
GL_SECONDARY_COLOR_ARRAY = constant.Constant( 'GL_SECONDARY_COLOR_ARRAY', 0x845E )
GL_MAX_TEXTURE_LOD_BIAS = constant.Constant( 'GL_MAX_TEXTURE_LOD_BIAS', 0x84FD )
GL_TEXTURE_FILTER_CONTROL = constant.Constant( 'GL_TEXTURE_FILTER_CONTROL', 0x8500 )
GL_TEXTURE_LOD_BIAS = constant.Constant( 'GL_TEXTURE_LOD_BIAS', 0x8501 )
GL_INCR_WRAP = constant.Constant( 'GL_INCR_WRAP', 0x8507 )
GL_DECR_WRAP = constant.Constant( 'GL_DECR_WRAP', 0x8508 )
GL_TEXTURE_DEPTH_SIZE = constant.Constant( 'GL_TEXTURE_DEPTH_SIZE', 0x884A )
GL_DEPTH_TEXTURE_MODE = constant.Constant( 'GL_DEPTH_TEXTURE_MODE', 0x884B )
GL_TEXTURE_COMPARE_MODE = constant.Constant( 'GL_TEXTURE_COMPARE_MODE', 0x884C )
GL_TEXTURE_COMPARE_FUNC = constant.Constant( 'GL_TEXTURE_COMPARE_FUNC', 0x884D )
GL_COMPARE_R_TO_TEXTURE = constant.Constant( 'GL_COMPARE_R_TO_TEXTURE', 0x884E )
glBlendFuncSeparate = platform.createExtensionFunction( 
	'glBlendFuncSeparate', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLenum, constants.GLenum, constants.GLenum,),
	doc = 'glBlendFuncSeparate( GLenum(sfactorRGB), GLenum(dfactorRGB), GLenum(sfactorAlpha), GLenum(dfactorAlpha) ) -> None',
	argNames = ('sfactorRGB', 'dfactorRGB', 'sfactorAlpha', 'dfactorAlpha',),
)

glFogCoordf = platform.createExtensionFunction( 
	'glFogCoordf', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLfloat,),
	doc = 'glFogCoordf( GLfloat(coord) ) -> None',
	argNames = ('coord',),
)

glFogCoordfv = platform.createExtensionFunction( 
	'glFogCoordfv', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(arrays.GLfloatArray,),
	doc = 'glFogCoordfv( GLfloatArray(coord) ) -> None',
	argNames = ('coord',),
)

glFogCoordd = platform.createExtensionFunction( 
	'glFogCoordd', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLdouble,),
	doc = 'glFogCoordd( GLdouble(coord) ) -> None',
	argNames = ('coord',),
)

glFogCoorddv = platform.createExtensionFunction( 
	'glFogCoorddv', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(arrays.GLdoubleArray,),
	doc = 'glFogCoorddv( GLdoubleArray(coord) ) -> None',
	argNames = ('coord',),
)

glFogCoordPointer = platform.createExtensionFunction( 
	'glFogCoordPointer', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLsizei, ctypes.c_void_p,),
	doc = 'glFogCoordPointer( GLenum(type), GLsizei(stride), c_void_p(pointer) ) -> None',
	argNames = ('type', 'stride', 'pointer',),
)

glMultiDrawArrays = platform.createExtensionFunction( 
	'glMultiDrawArrays', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, arrays.GLintArray, arrays.GLsizeiArray, constants.GLsizei,),
	doc = 'glMultiDrawArrays( GLenum(mode), GLintArray(first), GLsizeiArray(count), GLsizei(primcount) ) -> None',
	argNames = ('mode', 'first', 'count', 'primcount',),
)

glMultiDrawElements = platform.createExtensionFunction( 
	'glMultiDrawElements', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, arrays.GLsizeiArray, constants.GLenum, ctypes.POINTER(ctypes.c_void_p), constants.GLsizei,),
	doc = 'glMultiDrawElements( GLenum(mode), GLsizeiArray(count), GLenum(type), POINTER(ctypes.c_void_p)(indices), GLsizei(primcount) ) -> None',
	argNames = ('mode', 'count', 'type', 'indices', 'primcount',),
)

glPointParameterf = platform.createExtensionFunction( 
	'glPointParameterf', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLfloat,),
	doc = 'glPointParameterf( GLenum(pname), GLfloat(param) ) -> None',
	argNames = ('pname', 'param',),
)

glPointParameterfv = platform.createExtensionFunction( 
	'glPointParameterfv', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, arrays.GLfloatArray,),
	doc = 'glPointParameterfv( GLenum(pname), GLfloatArray(params) ) -> None',
	argNames = ('pname', 'params',),
)

glPointParameteri = platform.createExtensionFunction( 
	'glPointParameteri', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLint,),
	doc = 'glPointParameteri( GLenum(pname), GLint(param) ) -> None',
	argNames = ('pname', 'param',),
)

glPointParameteriv = platform.createExtensionFunction( 
	'glPointParameteriv', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, arrays.GLintArray,),
	doc = 'glPointParameteriv( GLenum(pname), GLintArray(params) ) -> None',
	argNames = ('pname', 'params',),
)

glSecondaryColor3b = platform.createExtensionFunction( 
	'glSecondaryColor3b', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLbyte, constants.GLbyte, constants.GLbyte,),
	doc = 'glSecondaryColor3b( GLbyte(red), GLbyte(green), GLbyte(blue) ) -> None',
	argNames = ('red', 'green', 'blue',),
)

glSecondaryColor3bv = platform.createExtensionFunction( 
	'glSecondaryColor3bv', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(arrays.GLbyteArray,),
	doc = 'glSecondaryColor3bv( GLbyteArray(v) ) -> None',
	argNames = ('v',),
)

glSecondaryColor3d = platform.createExtensionFunction( 
	'glSecondaryColor3d', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLdouble, constants.GLdouble, constants.GLdouble,),
	doc = 'glSecondaryColor3d( GLdouble(red), GLdouble(green), GLdouble(blue) ) -> None',
	argNames = ('red', 'green', 'blue',),
)

glSecondaryColor3dv = platform.createExtensionFunction( 
	'glSecondaryColor3dv', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(arrays.GLdoubleArray,),
	doc = 'glSecondaryColor3dv( GLdoubleArray(v) ) -> None',
	argNames = ('v',),
)

glSecondaryColor3f = platform.createExtensionFunction( 
	'glSecondaryColor3f', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLfloat, constants.GLfloat, constants.GLfloat,),
	doc = 'glSecondaryColor3f( GLfloat(red), GLfloat(green), GLfloat(blue) ) -> None',
	argNames = ('red', 'green', 'blue',),
)

glSecondaryColor3fv = platform.createExtensionFunction( 
	'glSecondaryColor3fv', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(arrays.GLfloatArray,),
	doc = 'glSecondaryColor3fv( GLfloatArray(v) ) -> None',
	argNames = ('v',),
)

glSecondaryColor3i = platform.createExtensionFunction( 
	'glSecondaryColor3i', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLint, constants.GLint,),
	doc = 'glSecondaryColor3i( GLint(red), GLint(green), GLint(blue) ) -> None',
	argNames = ('red', 'green', 'blue',),
)

glSecondaryColor3iv = platform.createExtensionFunction( 
	'glSecondaryColor3iv', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(arrays.GLintArray,),
	doc = 'glSecondaryColor3iv( GLintArray(v) ) -> None',
	argNames = ('v',),
)

glSecondaryColor3s = platform.createExtensionFunction( 
	'glSecondaryColor3s', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLshort, constants.GLshort, constants.GLshort,),
	doc = 'glSecondaryColor3s( GLshort(red), GLshort(green), GLshort(blue) ) -> None',
	argNames = ('red', 'green', 'blue',),
)

glSecondaryColor3sv = platform.createExtensionFunction( 
	'glSecondaryColor3sv', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(arrays.GLshortArray,),
	doc = 'glSecondaryColor3sv( GLshortArray(v) ) -> None',
	argNames = ('v',),
)

glSecondaryColor3ub = platform.createExtensionFunction( 
	'glSecondaryColor3ub', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLubyte, constants.GLubyte, constants.GLubyte,),
	doc = 'glSecondaryColor3ub( GLubyte(red), GLubyte(green), GLubyte(blue) ) -> None',
	argNames = ('red', 'green', 'blue',),
)

glSecondaryColor3ubv = platform.createExtensionFunction( 
	'glSecondaryColor3ubv', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(arrays.GLubyteArray,),
	doc = 'glSecondaryColor3ubv( GLubyteArray(v) ) -> None',
	argNames = ('v',),
)

glSecondaryColor3ui = platform.createExtensionFunction( 
	'glSecondaryColor3ui', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLuint, constants.GLuint,),
	doc = 'glSecondaryColor3ui( GLuint(red), GLuint(green), GLuint(blue) ) -> None',
	argNames = ('red', 'green', 'blue',),
)

glSecondaryColor3uiv = platform.createExtensionFunction( 
	'glSecondaryColor3uiv', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(arrays.GLuintArray,),
	doc = 'glSecondaryColor3uiv( GLuintArray(v) ) -> None',
	argNames = ('v',),
)

glSecondaryColor3us = platform.createExtensionFunction( 
	'glSecondaryColor3us', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLushort, constants.GLushort, constants.GLushort,),
	doc = 'glSecondaryColor3us( GLushort(red), GLushort(green), GLushort(blue) ) -> None',
	argNames = ('red', 'green', 'blue',),
)

glSecondaryColor3usv = platform.createExtensionFunction( 
	'glSecondaryColor3usv', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(arrays.GLushortArray,),
	doc = 'glSecondaryColor3usv( GLushortArray(v) ) -> None',
	argNames = ('v',),
)

glSecondaryColorPointer = platform.createExtensionFunction( 
	'glSecondaryColorPointer', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLenum, constants.GLsizei, ctypes.c_void_p,),
	doc = 'glSecondaryColorPointer( GLint(size), GLenum(type), GLsizei(stride), c_void_p(pointer) ) -> None',
	argNames = ('size', 'type', 'stride', 'pointer',),
)

glWindowPos2d = platform.createExtensionFunction( 
	'glWindowPos2d', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLdouble, constants.GLdouble,),
	doc = 'glWindowPos2d( GLdouble(x), GLdouble(y) ) -> None',
	argNames = ('x', 'y',),
)

glWindowPos2dv = platform.createExtensionFunction( 
	'glWindowPos2dv', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(arrays.GLdoubleArray,),
	doc = 'glWindowPos2dv( GLdoubleArray(v) ) -> None',
	argNames = ('v',),
)

glWindowPos2f = platform.createExtensionFunction( 
	'glWindowPos2f', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLfloat, constants.GLfloat,),
	doc = 'glWindowPos2f( GLfloat(x), GLfloat(y) ) -> None',
	argNames = ('x', 'y',),
)

glWindowPos2fv = platform.createExtensionFunction( 
	'glWindowPos2fv', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(arrays.GLfloatArray,),
	doc = 'glWindowPos2fv( GLfloatArray(v) ) -> None',
	argNames = ('v',),
)

glWindowPos2i = platform.createExtensionFunction( 
	'glWindowPos2i', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLint,),
	doc = 'glWindowPos2i( GLint(x), GLint(y) ) -> None',
	argNames = ('x', 'y',),
)

glWindowPos2iv = platform.createExtensionFunction( 
	'glWindowPos2iv', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(arrays.GLintArray,),
	doc = 'glWindowPos2iv( GLintArray(v) ) -> None',
	argNames = ('v',),
)

glWindowPos2s = platform.createExtensionFunction( 
	'glWindowPos2s', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLshort, constants.GLshort,),
	doc = 'glWindowPos2s( GLshort(x), GLshort(y) ) -> None',
	argNames = ('x', 'y',),
)

glWindowPos2sv = platform.createExtensionFunction( 
	'glWindowPos2sv', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(arrays.GLshortArray,),
	doc = 'glWindowPos2sv( GLshortArray(v) ) -> None',
	argNames = ('v',),
)

glWindowPos3d = platform.createExtensionFunction( 
	'glWindowPos3d', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLdouble, constants.GLdouble, constants.GLdouble,),
	doc = 'glWindowPos3d( GLdouble(x), GLdouble(y), GLdouble(z) ) -> None',
	argNames = ('x', 'y', 'z',),
)

glWindowPos3dv = platform.createExtensionFunction( 
	'glWindowPos3dv', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(arrays.GLdoubleArray,),
	doc = 'glWindowPos3dv( GLdoubleArray(v) ) -> None',
	argNames = ('v',),
)

glWindowPos3f = platform.createExtensionFunction( 
	'glWindowPos3f', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLfloat, constants.GLfloat, constants.GLfloat,),
	doc = 'glWindowPos3f( GLfloat(x), GLfloat(y), GLfloat(z) ) -> None',
	argNames = ('x', 'y', 'z',),
)

glWindowPos3fv = platform.createExtensionFunction( 
	'glWindowPos3fv', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(arrays.GLfloatArray,),
	doc = 'glWindowPos3fv( GLfloatArray(v) ) -> None',
	argNames = ('v',),
)

glWindowPos3i = platform.createExtensionFunction( 
	'glWindowPos3i', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLint, constants.GLint,),
	doc = 'glWindowPos3i( GLint(x), GLint(y), GLint(z) ) -> None',
	argNames = ('x', 'y', 'z',),
)

glWindowPos3iv = platform.createExtensionFunction( 
	'glWindowPos3iv', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(arrays.GLintArray,),
	doc = 'glWindowPos3iv( GLintArray(v) ) -> None',
	argNames = ('v',),
)

glWindowPos3s = platform.createExtensionFunction( 
	'glWindowPos3s', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLshort, constants.GLshort, constants.GLshort,),
	doc = 'glWindowPos3s( GLshort(x), GLshort(y), GLshort(z) ) -> None',
	argNames = ('x', 'y', 'z',),
)

glWindowPos3sv = platform.createExtensionFunction( 
	'glWindowPos3sv', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(arrays.GLshortArray,),
	doc = 'glWindowPos3sv( GLshortArray(v) ) -> None',
	argNames = ('v',),
)

