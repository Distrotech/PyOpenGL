'''OpenGL extension EXT.cmyka

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.cmyka to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/cmyka.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.EXT.cmyka import *

def glInitCmykaEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION
from OpenGL import images as _i

_i.COMPONENT_COUNTS[ GL_CMYK_EXT ] = 4
_i.COMPONENT_COUNTS[ GL_CMYKA_EXT ] = 5
