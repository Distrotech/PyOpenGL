'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_AMD_compressed_ATC_texture'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_AMD_compressed_ATC_texture')
GL_ATC_RGBA_EXPLICIT_ALPHA_AMD=_C('GL_ATC_RGBA_EXPLICIT_ALPHA_AMD',0x8C93)
GL_ATC_RGBA_INTERPOLATED_ALPHA_AMD=_C('GL_ATC_RGBA_INTERPOLATED_ALPHA_AMD',0x87EE)
GL_ATC_RGB_AMD=_C('GL_ATC_RGB_AMD',0x8C92)

