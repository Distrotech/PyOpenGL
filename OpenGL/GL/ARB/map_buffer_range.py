'''OpenGL extension ARB.map_buffer_range

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.map_buffer_range to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.ARB.map_buffer_range import *
### END AUTOGENERATED SECTION