'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.WGL import _types as _cs
# End users want this...
from OpenGL.raw.WGL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'WGL_EXT_pixel_format_packed_float'
def _f( function ):
    return _p.createFunction( function,_p.WGL,'WGL_EXT_pixel_format_packed_float')
WGL_TYPE_RGBA_UNSIGNED_FLOAT_EXT=_C('WGL_TYPE_RGBA_UNSIGNED_FLOAT_EXT',0x20A8)

