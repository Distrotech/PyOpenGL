'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_AMD_name_gen_delete'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_AMD_name_gen_delete')
GL_DATA_BUFFER_AMD=_C('GL_DATA_BUFFER_AMD',0x9151)
GL_PERFORMANCE_MONITOR_AMD=_C('GL_PERFORMANCE_MONITOR_AMD',0x9152)
GL_QUERY_OBJECT_AMD=_C('GL_QUERY_OBJECT_AMD',0x9153)
GL_SAMPLER_OBJECT_AMD=_C('GL_SAMPLER_OBJECT_AMD',0x9155)
GL_VERTEX_ARRAY_OBJECT_AMD=_C('GL_VERTEX_ARRAY_OBJECT_AMD',0x9154)
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,arrays.GLuintArray)
def glDeleteNamesAMD(identifier,num,names):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,arrays.GLuintArray)
def glGenNamesAMD(identifier,num,names):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLenum,_cs.GLuint)
def glIsNameAMD(identifier,name):pass
