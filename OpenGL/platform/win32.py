"""Windows-specific platform features"""
import ctypes
import platform
from OpenGL.platform import ctypesloader, baseplatform
import sys

if sys.hexversion < 0x2070000:
    vc = 'vc7'
# TODO: add Python 3.x compiler compatibility...
else:
    vc = 'vc9'

def _size():
    return platform.architecture()[0].strip( 'bits' )
size = _size()

class Win32Platform( baseplatform.BasePlatform ):
    """Win32-specific platform implementation"""

    GLUT_GUARD_CALLBACKS = True
    try:
        GL = OpenGL = ctypesloader.loadLibrary(
            ctypes.windll, 'opengl32', mode = ctypes.RTLD_GLOBAL
        )
    except OSError as err:
        raise ImportError("Unable to load OpenGL library", *err.args)

    try:
        GLU = ctypesloader.loadLibrary(
            ctypes.windll, 'glu32', mode = ctypes.RTLD_GLOBAL
        )
    except OSError as err:
        GLU = None

    GLUT = None
    for possible in ('freeglut%s'%(size,),'freeglut', 'glut%s'%(size,)):
        # Prefer FreeGLUT if the user has installed it, fallback to the included 
        # GLUT if it is installed
        try:
            GLUT = ctypesloader.loadLibrary(
                ctypes.windll, possible, mode = ctypes.RTLD_GLOBAL
            )
        except WindowsError as err:
            GLUT = None
        else:
            break
    try:
        del possible
    except NameError as err:
        pass

    GLE = None
    for libName in ('opengle%s.%s'%(size,vc,),'gle%s'%(size,)):
        try:
            GLE = ctypesloader.loadLibrary( ctypes.cdll, libName )
            GLE.FunctionType = ctypes.CFUNCTYPE
        except WindowsError as err:
            pass
        else:
            break

    DEFAULT_FUNCTION_TYPE = staticmethod( ctypes.WINFUNCTYPE )
    # Win32 GLUT uses different types for callbacks and functions...
    GLUT_CALLBACK_TYPE = staticmethod( ctypes.CFUNCTYPE )
    WGL = ctypes.windll.gdi32
    wglGetProcAddress = OpenGL.wglGetProcAddress
    wglGetProcAddress.restype = ctypes.c_void_p
    getExtensionProcedure = staticmethod( wglGetProcAddress )

    GLUT_FONT_CONSTANTS = {
        'GLUT_STROKE_ROMAN': ctypes.c_void_p( 0),
        'GLUT_STROKE_MONO_ROMAN': ctypes.c_void_p( 1),
        'GLUT_BITMAP_9_BY_15': ctypes.c_void_p( 2),
        'GLUT_BITMAP_8_BY_13': ctypes.c_void_p( 3),
        'GLUT_BITMAP_TIMES_ROMAN_10': ctypes.c_void_p( 4),
        'GLUT_BITMAP_TIMES_ROMAN_24': ctypes.c_void_p( 5),
        'GLUT_BITMAP_HELVETICA_10': ctypes.c_void_p( 6),
        'GLUT_BITMAP_HELVETICA_12': ctypes.c_void_p( 7),
        'GLUT_BITMAP_HELVETICA_18': ctypes.c_void_p( 8),
    }


    def getGLUTFontPointer( self,constant ):
        """Platform specific function to retrieve a GLUT font pointer

        GLUTAPI void *glutBitmap9By15;
        #define GLUT_BITMAP_9_BY_15		(&glutBitmap9By15)

        Key here is that we want the addressof the pointer in the DLL,
        not the pointer in the DLL.  That is, our pointer is to the
        pointer defined in the DLL, we don't want the *value* stored in
        that pointer.
        """
        return self.GLUT_FONT_CONSTANTS[ constant ]

    wglGetCurrentContext = GL.wglGetCurrentContext
    wglGetCurrentContext.restype = ctypes.c_void_p
    GetCurrentContext = CurrentContextIsValid = staticmethod(
        wglGetCurrentContext
    )


    def safeGetError( self ):
        """Provide context-not-present-safe error-checking

        Under OS-X an attempt to retrieve error without checking
        context will bus-error.  Likely Windows will see the same.
        This function checks for a valid context before running
        glGetError

        Note:
            This is a likely candidate for rewriting in C, as it
            is called for every almost function in the system!
        """
        if self.CurrentContextIsValid():
            return glGetError()
        return None

glGetError = Win32Platform.OpenGL.glGetError
