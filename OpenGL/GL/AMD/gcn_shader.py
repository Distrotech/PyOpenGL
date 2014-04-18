'''OpenGL extension AMD.gcn_shader

This module customises the behaviour of the 
OpenGL.raw.GL.AMD.gcn_shader to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/AMD/gcn_shader.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.AMD.gcn_shader import *
from OpenGL.raw.GL.AMD.gcn_shader import _EXTENSION_NAME

def glInitGcnShaderAMD():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION