'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_SGIX_shadow_ambient'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_SGIX_shadow_ambient')
GL_SHADOW_AMBIENT_SGIX=_C('GL_SHADOW_AMBIENT_SGIX',0x80BF)

