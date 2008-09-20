'''OpenGL extension NV.texture_shader3

This module customises the behaviour of the 
OpenGL.raw.GL.NV.texture_shader3 to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.NV.texture_shader3 import *
### END AUTOGENERATED SECTION