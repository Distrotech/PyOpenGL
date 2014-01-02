'''OpenGL extension ARM.mali_shader_binary

This module customises the behaviour of the 
OpenGL.raw.GL.ARM.mali_shader_binary to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARM/mali_shader_binary.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.ARM.mali_shader_binary import *

def glInitMaliShaderBinaryARM():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION