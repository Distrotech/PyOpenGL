'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_NV_vertex_program2_option'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_NV_vertex_program2_option')
GL_MAX_PROGRAM_CALL_DEPTH_NV=_C('GL_MAX_PROGRAM_CALL_DEPTH_NV',0x88F5)
GL_MAX_PROGRAM_EXEC_INSTRUCTIONS_NV=_C('GL_MAX_PROGRAM_EXEC_INSTRUCTIONS_NV',0x88F4)

