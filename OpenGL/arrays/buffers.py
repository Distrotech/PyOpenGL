#! /usr/bin/env python
"""Test for a buffer-protocol-based access mechanism

Will *only* work for Python 2.6+, and pretty much just works for strings
under 2.6 (in terms of the common object types).
"""
import ctypes,sys
from OpenGL._bytes import bytes
from OpenGL.arrays import _buffers
from OpenGL import constants
from OpenGL.arrays import formathandler
try:
    reduce 
except NameError as err:
    from functools import reduce
HANDLED_TYPES = [bytes,bytearray]
if sys.version_info[:2] >= (3,0):
    import array as silly_array
    HANDLED_TYPES.append( silly_array )
try:
    import numpy
    HANDLED_TYPES.append( numpy.ndarray )
except ImportError as err:
    pass
try:
    HANDLED_TYPES.append( memoryview )
except NameError:
    pass 

class BufferHandler( formathandler.FormatHandler ):
    """Buffer-protocol data-type handler for OpenGL"""
    HANDLED_TYPES = tuple( HANDLED_TYPES )
    @classmethod
    def from_param( cls, value, typeCode=None ):
        if not isinstance( value, _buffers.Py_buffer ):
            raise TypeError( """Can't convert value to py-buffer in from_param""" )
        return value.buf
    def dataPointer( value ):
        if not isinstance( value, _buffers.Py_buffer ):
            value = _buffers.Py_buffer.from_object( value )
        return ctypes.c_void_p(value.internal)
    dataPointer = staticmethod( dataPointer )
    def zeros( self, dims, typeCode=None ):
        """Currently don't allow strings as output types!"""
        return self.asArray( bytearray( b'\000'*reduce(operator.mul,dims)*BYTE_SIZES[typeCode] ) )
    def ones( self, dims, typeCode=None ):
        """Currently don't allow strings as output types!"""
        raise NotImplemented( """Have not implemented ones for buffer type""" )
    def arrayToGLType( self, value ):
        """Given a value, guess OpenGL type of the corresponding pointer"""
        format = value.format 
        if format in ARRAY_TO_GL_TYPE_MAPPING:
            return ARRAY_TO_GL_TYPE_MAPPING[format]
        raise TypeError( 'Unknown format: %r'%(format,))
    def arraySize( self, value, typeCode = None ):
        """Given a data-value, calculate ravelled size for the array"""
        return value.len // value.itemsize
    def arrayByteCount( self, value, typeCode = None ):
        """Given a data-value, calculate number of bytes required to represent"""
        return value.len
    def asArray( self, value, typeCode=None ):
        """Convert given value to an array value of given typeCode"""
        return _buffers.Py_buffer.from_object( value )
    def dimensions( self, value, typeCode=None ):
        """Determine dimensions of the passed array value (if possible)"""
        return value.dims

BYTE_SIZES = {
    constants.GL_DOUBLE: ctypes.sizeof( constants.GLdouble ),
    constants.GL_FLOAT: ctypes.sizeof( constants.GLfloat ),
    constants.GL_INT: ctypes.sizeof( constants.GLint ),
    constants.GL_SHORT: ctypes.sizeof( constants.GLshort ),
    constants.GL_UNSIGNED_BYTE: ctypes.sizeof( constants.GLubyte ),
    constants.GL_UNSIGNED_SHORT: ctypes.sizeof( constants.GLshort ),
    constants.GL_BYTE: ctypes.sizeof( constants.GLbyte ),
    constants.GL_UNSIGNED_INT: ctypes.sizeof( constants.GLuint ),
}
ARRAY_TO_GL_TYPE_MAPPING = {
    'd': constants.GL_DOUBLE,
    'f': constants.GL_FLOAT,
    'i': constants.GL_INT,
    'h': constants.GL_SHORT,
    'H': constants.GL_UNSIGNED_SHORT,
    'B': constants.GL_UNSIGNED_BYTE,
    'c': constants.GL_UNSIGNED_BYTE,
    'b': constants.GL_BYTE,
    'I': constants.GL_UNSIGNED_INT,
    None: None,
}
