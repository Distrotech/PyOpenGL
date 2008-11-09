'''OpenGL extension VERSION.GL_1_5

This module customises the behaviour of the 
OpenGL.raw.GL.VERSION.GL_1_5 to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.VERSION.GL_1_5 import *
### END AUTOGENERATED SECTION
from OpenGL.lazywrapper import lazy

glDeleteBuffers = arrays.setInputArraySizeType(
	glDeleteBuffers,
	None,
	arrays.GLuintArray,
	'buffers',
)

glGenBuffers = wrapper.wrapper( glGenBuffers ).setOutput(
	'buffers', lambda n: (n,), 'n',
)

def _sizeOfArrayInput( pyArgs, index, wrapper ):
	return (
		arrays.ArrayDatatype.arrayByteCount( pyArgs[index] )
	)

glBufferData = wrapper.wrapper( glBufferData ).setPyConverter(
	'data', arrays.asVoidArray(),
).setPyConverter( 'size' ).setCResolver( 
	'data', arrays.ArrayDatatype.voidDataPointer ,
).setCConverter(
	'size', _sizeOfArrayInput,
).setReturnValues( 
	wrapper.returnPyArgument( 'data' ) 
)

glBufferSubData = wrapper.wrapper( glBufferSubData ).setPyConverter(
	'data', arrays.asVoidArray(),
).setPyConverter( 'size' ).setCResolver( 
	'data', arrays.ArrayDatatype.voidDataPointer ,
).setCConverter(
	'size', _sizeOfArrayInput,
).setReturnValues( 
	wrapper.returnPyArgument( 'data' ) 
)

glGetBufferParameteriv = wrapper.wrapper(glGetBufferParameteriv).setOutput(
	"params",(1,),
)
@lazy( glGetBufferPointerv )
def glGetBufferPointerv( baseOperation, target, pname, params=None ):
	"""Retrieve a ctypes pointer to buffer's data"""
	if params is None:
		size = glGetBufferParameteriv( target, GL_BUFFER_SIZE )
		data = arrays.ArrayDatatype.zeros( (size,), GL_UNSIGNED_BYTE )
		result = baseOperation( target, pname, ctypes.byref( data ) )
		return data
	else:
		return baseOperation( target, pname, params )

for func in ('glGenQueries','glDeleteQueries'):
	globals()[func] = wrapper.wrapper( 
		globals()[func],
	).setPyConverter('n').setCConverter(
		'n', arrays.AsArrayTypedSize( 'ids', arrays.GLuintArray ),
	).setCConverter(
		'ids', arrays.asArrayType(arrays.GLuintArray),
	).setReturnValues(
		wrapper.returnPyArgument( 'ids' )
	)

for func in (
	'glGetQueryiv','glGetQueryObjectiv','glGetQueryObjectuiv',
):
	globals()[func] = wrapper.wrapper(globals()[func]).setOutput(
		"params", (1,)
	)
del func, glget

