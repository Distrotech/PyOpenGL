"""FreeGLUT extensions to the GLUT API

This module will provide the FreeGLUT extensions if they are available
from the GLUT module.  Note that any other implementation that also provides
these entry points will also retrieve the entry points with this module.
"""
# flags 'freeglut_ext.xml -l /usr/lib64/libglut.so -o freeglut_ext.py -v -kf'
from OpenGL import platform, arrays
from OpenGL.constants import *
from OpenGL import constant
FUNCTION_TYPE = platform.PLATFORM.functionTypeFor( platform.GLUT )
from OpenGL.GLUT import special

import ctypes
c_int = ctypes.c_int 
c_char_p = ctypes.c_char_p
c_ubyte = ctypes.c_ubyte
c_void_p = ctypes.c_void_p

GLUT_DEBUG = constant.Constant( 'GLUT_DEBUG', 0x0001 )
GLUT_FORWARD_COMPATIBLE = constant.Constant( 'GLUT_FORWARD_COMPATIBLE',  0x0002)

GLUT_ACTION_EXIT = constant.Constant( 'GLUT_ACTION_EXIT', 0 )
GLUT_ACTION_GLUTMAINLOOP_RETURNS = constant.Constant( 'GLUT_ACTION_GLUTMAINLOOP_RETURNS', 1 )
GLUT_ACTION_CONTINUE_EXECUTION = constant.Constant( 'GLUT_ACTION_CONTINUE_EXECUTION', 2 )

GLUT_INIT_MAJOR_VERSION = constant.Constant( 'GLUT_INIT_MAJOR_VERSION', 0x0200 )
GLUT_INIT_MINOR_VERSION = constant.Constant( 'GLUT_INIT_MINOR_VERSION', 0x0201 )
GLUT_INIT_FLAGS = constant.Constant( 'GLUT_INIT_FLAGS', 0x0202 )

GLUT_CREATE_NEW_CONTEXT = constant.Constant( 'GLUT_CREATE_NEW_CONTEXT', 0 )
GLUT_USE_CURRENT_CONTEXT = constant.Constant( 'GLUT_USE_CURRENT_CONTEXT', 1 )

GLUT_ACTION_ON_WINDOW_CLOSE = constant.Constant( 'GLUT_ACTION_ON_WINDOW_CLOSE', 0x01F9 )
GLUT_WINDOW_BORDER_WIDTH = constant.Constant( 'GLUT_WINDOW_BORDER_WIDTH', 0x01FA )
GLUT_WINDOW_HEADER_HEIGHT = constant.Constant( 'GLUT_USE_CURRENT_CONTEXT', 0x01FB )
#GLUT_VERSION = constant.Constant( 'GLUT_VERSION', 0x01FC )
GLUT_RENDERING_CONTEXT = constant.Constant( 'GLUT_RENDERING_CONTEXT', 0x01FD )

# /usr/include/GL/freeglut_ext.h 63
glutMainLoopEvent = platform.createBaseFunction( 
	'glutMainLoopEvent', dll=platform.GLUT, resultType=None, 
	argTypes=[],
	doc='glutMainLoopEvent(  ) -> None', 
	argNames=(),
)
# /usr/include/GL/freeglut_ext.h 64
glutLeaveMainLoop = platform.createBaseFunction( 
	'glutLeaveMainLoop', dll=platform.GLUT, resultType=None, 
	argTypes=[],
	doc='glutLeaveMainLoop(  ) -> None', 
	argNames=(),
)

# /usr/include/GL/freeglut_ext.h 69
##glutMouseWheelFunc = platform.createBaseFunction( 
##	'glutMouseWheelFunc', dll=platform.GLUT, resultType=None, 
##	argTypes=[FUNCTION_TYPE(None, c_int, c_int, c_int, c_int)],
##	doc='glutMouseWheelFunc( FUNCTION_TYPE(None, c_int, c_int, c_int, c_int)(callback) ) -> None', 
##	argNames=('callback',),
##)
glutMouseWheelFunc = special.GLUTCallback(
	'MouseWheel', (c_int, c_int, c_int, c_int,), ('wheel','direction','x','y'),
)


# /usr/include/GL/freeglut_ext.h 70
##glutCloseFunc = platform.createBaseFunction( 
##	'glutCloseFunc', dll=platform.GLUT, resultType=None, 
##	argTypes=[FUNCTION_TYPE(None)],
##	doc='glutCloseFunc( FUNCTION_TYPE(None)(callback) ) -> None', 
##	argNames=('callback',),
##)
glutCloseFunc = special.GLUTCallback(
	'Close', (), (),
)

# /usr/include/GL/freeglut_ext.h 71
##glutWMCloseFunc = platform.createBaseFunction( 
##	'glutWMCloseFunc', dll=platform.GLUT, resultType=None, 
##	argTypes=[FUNCTION_TYPE(None)],
##	doc='glutWMCloseFunc( FUNCTION_TYPE(None)(callback) ) -> None', 
##	argNames=('callback',),
##)
glutWMCloseFunc = special.GLUTCallback(
	'WMClose', (), (),
)

# /usr/include/GL/freeglut_ext.h 73
##glutMenuDestroyFunc = platform.createBaseFunction( 
##	'glutMenuDestroyFunc', dll=platform.GLUT, resultType=None, 
##	argTypes=[FUNCTION_TYPE(None)],
##	doc='glutMenuDestroyFunc( FUNCTION_TYPE(None)(callback) ) -> None', 
##	argNames=('callback',),
##)
glutMenuDestroyFunc = special.GLUTCallback(
	'MenuDestroy', (), (),
)

# /usr/include/GL/freeglut_ext.h 78
glutSetOption = platform.createBaseFunction( 
	'glutSetOption', dll=platform.GLUT, resultType=None, 
	argTypes=[GLenum, c_int],
	doc='glutSetOption( GLenum(option_flag), c_int(value) ) -> None', 
	argNames=('option_flag', 'value'),
)

# /usr/include/GL/freeglut_ext.h 80
glutGetWindowData = platform.createBaseFunction( 
	'glutGetWindowData', dll=platform.GLUT, resultType=c_void_p, 
	argTypes=[],
	doc='glutGetWindowData(  ) -> c_void_p', 
	argNames=(),
)

# /usr/include/GL/freeglut_ext.h 81
glutSetWindowData = platform.createBaseFunction( 
	'glutSetWindowData', dll=platform.GLUT, resultType=None, 
	argTypes=[c_void_p],
	doc='glutSetWindowData( c_void_p(data) ) -> None', 
	argNames=('data',),
)

# /usr/include/GL/freeglut_ext.h 82
glutGetMenuData = platform.createBaseFunction( 
	'glutGetMenuData', dll=platform.GLUT, resultType=c_void_p, 
	argTypes=[],
	doc='glutGetMenuData(  ) -> c_void_p', 
	argNames=(),
)

# /usr/include/GL/freeglut_ext.h 83
glutSetMenuData = platform.createBaseFunction( 
	'glutSetMenuData', dll=platform.GLUT, resultType=None, 
	argTypes=[c_void_p],
	doc='glutSetMenuData( c_void_p(data) ) -> None', 
	argNames=('data',),
)

# /usr/include/GL/freeglut_ext.h 88
glutBitmapHeight = platform.createBaseFunction( 
	'glutBitmapHeight', dll=platform.GLUT, resultType=c_int, 
	argTypes=[c_void_p],
	doc='glutBitmapHeight( c_void_p(font) ) -> c_int', 
	argNames=('font',),
)

# /usr/include/GL/freeglut_ext.h 89
glutStrokeHeight = platform.createBaseFunction( 
	'glutStrokeHeight', dll=platform.GLUT, resultType=GLfloat, 
	argTypes=[c_void_p],
	doc='glutStrokeHeight( c_void_p(font) ) -> GLfloat', 
	argNames=('font',),
)

# /usr/include/GL/freeglut_ext.h 90
glutBitmapString = platform.createBaseFunction( 
	'glutBitmapString', dll=platform.GLUT, resultType=None, 
	argTypes=[c_void_p, c_char_p],
	doc='glutBitmapString( c_void_p(font), POINTER(c_ubyte)(string) ) -> None', 
	argNames=('font', 'string'),
)
##glutBitmapString = platform.createBaseFunction( 
##	'glutBitmapString', dll=platform.GLUT, resultType=None, 
##	argTypes=[c_void_p, arrays.GLubyteArray],
##	doc='glutBitmapString( c_void_p(font), POINTER(c_ubyte)(string) ) -> None', 
##	argNames=('font', 'string'),
##)
##glutBitmapString = arrays.setInputArraySizeType(
##	glutBitmapString,
##	None, 
##	arrays.GLubyteArray, 
##	'string',
##)

# /usr/include/GL/freeglut_ext.h 91
glutStrokeString = platform.createBaseFunction( 
	'glutStrokeString', dll=platform.GLUT, resultType=None, 
	argTypes=[c_void_p, c_char_p],
	doc='glutStrokeString( c_void_p(font), POINTER(c_ubyte)(string) ) -> None', 
	argNames=('font', 'string'),
)
##glutStrokeString = platform.createBaseFunction( 
##	'glutStrokeString', dll=platform.GLUT, resultType=None, 
##	argTypes=[c_void_p, arrays.GLubyteArray],
##	doc='glutStrokeString( c_void_p(font), POINTER(c_ubyte)(string) ) -> None', 
##	argNames=('font', 'string'),
##)
##glutStrokeString = arrays.setInputArraySizeType(
##	glutStrokeString,
##	None, 
##	arrays.GLubyteArray, 
##	'string',
##)

# /usr/include/GL/freeglut_ext.h 96
glutWireRhombicDodecahedron = platform.createBaseFunction( 
	'glutWireRhombicDodecahedron', dll=platform.GLUT, resultType=None, 
	argTypes=[],
	doc='glutWireRhombicDodecahedron(  ) -> None', 
	argNames=(),
)

# /usr/include/GL/freeglut_ext.h 97
glutSolidRhombicDodecahedron = platform.createBaseFunction( 
	'glutSolidRhombicDodecahedron', dll=platform.GLUT, resultType=None, 
	argTypes=[],
	doc='glutSolidRhombicDodecahedron(  ) -> None', 
	argNames=(),
)

# /usr/include/GL/freeglut_ext.h 98
glutWireSierpinskiSponge = platform.createBaseFunction( 
	'glutWireSierpinskiSponge', dll=platform.GLUT, resultType=None, 
	argTypes=[c_int, arrays.GLdoubleArray, GLdouble],
	doc='glutWireSierpinskiSponge( c_int(num_levels), arrays.GLdoubleArray(offset), GLdouble(scale) ) -> None', 
	argNames=('num_levels', 'offset', 'scale'),
)

glutWireSierpinskiSponge = arrays.setInputArraySizeType(
	glutWireSierpinskiSponge,
	None, # XXX Could not determine size of argument offset for glutWireSierpinskiSponge arrays.GLdoubleArray
	arrays.GLdoubleArray, 
	'offset',
)

# /usr/include/GL/freeglut_ext.h 99
glutSolidSierpinskiSponge = platform.createBaseFunction( 
	'glutSolidSierpinskiSponge', dll=platform.GLUT, resultType=None, 
	argTypes=[c_int, arrays.GLdoubleArray, GLdouble],
	doc='glutSolidSierpinskiSponge( c_int(num_levels), arrays.GLdoubleArray(offset), GLdouble(scale) ) -> None', 
	argNames=('num_levels', 'offset', 'scale'),
)

glutSolidSierpinskiSponge = arrays.setInputArraySizeType(
	glutSolidSierpinskiSponge,
	None, # XXX Could not determine size of argument offset for glutSolidSierpinskiSponge arrays.GLdoubleArray
	arrays.GLdoubleArray, 
	'offset',
)

# /usr/include/GL/freeglut_ext.h 100
glutWireCylinder = platform.createBaseFunction( 
	'glutWireCylinder', dll=platform.GLUT, resultType=None, 
	argTypes=[GLdouble, GLdouble, GLint, GLint],
	doc='glutWireCylinder( GLdouble(radius), GLdouble(height), GLint(slices), GLint(stacks) ) -> None', 
	argNames=('radius', 'height', 'slices', 'stacks'),
)

# /usr/include/GL/freeglut_ext.h 101
glutSolidCylinder = platform.createBaseFunction( 
	'glutSolidCylinder', dll=platform.GLUT, resultType=None, 
	argTypes=[GLdouble, GLdouble, GLint, GLint],
	doc='glutSolidCylinder( GLdouble(radius), GLdouble(height), GLint(slices), GLint(stacks) ) -> None', 
	argNames=('radius', 'height', 'slices', 'stacks'),
)

# /usr/include/GL/freeglut_ext.h 106
glutGetProcAddress = platform.createBaseFunction( 
	'glutGetProcAddress', dll=platform.GLUT, resultType=c_void_p, 
	argTypes=[c_char_p],
	doc='glutGetProcAddress( STRING(procName) ) -> c_void_p', 
	argNames=('procName',),
)
