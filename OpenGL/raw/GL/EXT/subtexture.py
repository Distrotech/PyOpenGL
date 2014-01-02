'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_EXT_subtexture'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_subtexture')

@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTexSubImage1DEXT(target,level,xoffset,width,format,type,pixels):pass
# Calculate length of pixels from format:PixelFormat, type:PixelType
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTexSubImage2DEXT(target,level,xoffset,yoffset,width,height,format,type,pixels):pass
# Calculate length of pixels from format:PixelFormat, type:PixelType
