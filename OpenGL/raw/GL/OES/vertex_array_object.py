'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_OES_vertex_array_object'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_OES_vertex_array_object')
GL_VERTEX_ARRAY_BINDING_OES=_C('GL_VERTEX_ARRAY_BINDING_OES',0x85B5)
@_f
@_p.types(None,_cs.GLuint)
def glBindVertexArrayOES(array):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeleteVertexArraysOES(n,arrays):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenVertexArraysOES(n,arrays):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsVertexArrayOES(array):pass
