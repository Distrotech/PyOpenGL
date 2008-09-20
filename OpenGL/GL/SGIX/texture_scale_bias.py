'''OpenGL extension SGIX.texture_scale_bias

This module customises the behaviour of the 
OpenGL.raw.GL.SGIX.texture_scale_bias to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.SGIX.texture_scale_bias import *
### END AUTOGENERATED SECTION