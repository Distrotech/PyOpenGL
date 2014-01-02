'''OpenGL extension HP.occlusion_test

This module customises the behaviour of the 
OpenGL.raw.GL.HP.occlusion_test to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/HP/occlusion_test.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.HP.occlusion_test import *

def glInitOcclusionTestHP():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION