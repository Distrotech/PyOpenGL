'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLX import _types as _cs
# End users want this...
from OpenGL.raw.GLX._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GLX_SGI_cushion'
def _f( function ):
    return _p.createFunction( function,_p.GLX,'GLX_SGI_cushion')

@_f
@_p.types(None,ctypes.POINTER(_cs.Display),_cs.Window,_cs.float)
def glXCushionSGI(dpy,window,cushion):pass
