'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_EXT_packed_float'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_packed_float')
GL_R11F_G11F_B10F_EXT=_C('GL_R11F_G11F_B10F_EXT',0x8C3A)
GL_RGBA_SIGNED_COMPONENTS_EXT=_C('GL_RGBA_SIGNED_COMPONENTS_EXT',0x8C3C)
GL_UNSIGNED_INT_10F_11F_11F_REV_EXT=_C('GL_UNSIGNED_INT_10F_11F_11F_REV_EXT',0x8C3B)

