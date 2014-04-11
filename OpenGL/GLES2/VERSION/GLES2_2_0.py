'''OpenGL extension VERSION.GLES2_2_0

This module customises the behaviour of the 
OpenGL.raw.GLES2.VERSION.GLES2_2_0 to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/VERSION/GLES2_2_0.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.VERSION.GLES2_2_0 import *
from OpenGL.raw.GLES2.VERSION.GLES2_2_0 import _EXTENSION_NAME

def glInitGles220VERSION():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

glGenBuffers=wrapper.wrapper(glGenBuffers).setOutput(#
    'buffers',size=lambda x:(x,),pnameArg='n',orPassIn=True
)
glGenFramebuffers=wrapper.wrapper(glGenFramebuffers).setOutput(#
    'framebuffers',size=lambda x:(x,),pnameArg='n',orPassIn=True
)
glGenRenderbuffers=wrapper.wrapper(glGenRenderbuffers).setOutput(#
    'renderbuffers',size=lambda x:(x,),pnameArg='n',orPassIn=True
)
glGenTextures=wrapper.wrapper(glGenTextures).setOutput(#
    'textures',size=lambda x:(x,),pnameArg='n',orPassIn=True
)
# OUTPUT MULTIPLE glGetActiveAttrib
# OUTPUT MULTIPLE glGetActiveAttrib
# OUTPUT MULTIPLE glGetActiveAttrib
# OUTPUT MULTIPLE glGetActiveAttrib
# OUTPUT MULTIPLE glGetActiveUniform
# OUTPUT MULTIPLE glGetActiveUniform
# OUTPUT MULTIPLE glGetActiveUniform
# OUTPUT MULTIPLE glGetActiveUniform
# OUTPUT MULTIPLE glGetAttachedShaders
# OUTPUT MULTIPLE glGetAttachedShaders
glGetBooleanv=wrapper.wrapper(glGetBooleanv).setOutput(#
    'data',size=_glgets._glget_size_mapping,pnameArg='pname',orPassIn=True
)
glGetBufferParameteriv=wrapper.wrapper(glGetBufferParameteriv).setOutput(#
    'params',size=_glgets._glget_size_mapping,pnameArg='pname',orPassIn=True
)
glGetFloatv=wrapper.wrapper(glGetFloatv).setOutput(#
    'data',size=_glgets._glget_size_mapping,pnameArg='pname',orPassIn=True
)
glGetFramebufferAttachmentParameteriv=wrapper.wrapper(glGetFramebufferAttachmentParameteriv).setOutput(#
    'params',size=_glgets._glget_size_mapping,pnameArg='pname',orPassIn=True
)
glGetIntegerv=wrapper.wrapper(glGetIntegerv).setOutput(#
    'data',size=_glgets._glget_size_mapping,pnameArg='pname',orPassIn=True
)
glGetProgramiv=wrapper.wrapper(glGetProgramiv).setOutput(#
    'params',size=_glgets._glget_size_mapping,pnameArg='pname',orPassIn=True
)
# OUTPUT MULTIPLE glGetProgramInfoLog
# OUTPUT MULTIPLE glGetProgramInfoLog
glGetRenderbufferParameteriv=wrapper.wrapper(glGetRenderbufferParameteriv).setOutput(#
    'params',size=_glgets._glget_size_mapping,pnameArg='pname',orPassIn=True
)
glGetShaderiv=wrapper.wrapper(glGetShaderiv).setOutput(#
    'params',size=_glgets._glget_size_mapping,pnameArg='pname',orPassIn=True
)
# OUTPUT MULTIPLE glGetShaderInfoLog
# OUTPUT MULTIPLE glGetShaderInfoLog
# OUTPUT MULTIPLE glGetShaderPrecisionFormat
# OUTPUT MULTIPLE glGetShaderPrecisionFormat
# OUTPUT MULTIPLE glGetShaderSource
# OUTPUT MULTIPLE glGetShaderSource
glGetTexParameterfv=wrapper.wrapper(glGetTexParameterfv).setOutput(#
    'params',size=_glgets._glget_size_mapping,pnameArg='pname',orPassIn=True
)
glGetTexParameteriv=wrapper.wrapper(glGetTexParameteriv).setOutput(#
    'params',size=_glgets._glget_size_mapping,pnameArg='pname',orPassIn=True
)
# OUTPUT glGetUniformfv=wrapper.wrapper(glGetUniformfv)
# OUTPUT glGetUniformiv=wrapper.wrapper(glGetUniformiv)
glGetVertexAttribfv=wrapper.wrapper(glGetVertexAttribfv).setOutput(#
    'params',size=(4,),orPassIn=True
)
glGetVertexAttribiv=wrapper.wrapper(glGetVertexAttribiv).setOutput(#
    'params',size=(4,),orPassIn=True
)
glGetVertexAttribPointerv=wrapper.wrapper(glGetVertexAttribPointerv).setOutput(#
    'pointer',size=(1,),orPassIn=True
)
# COMPSIZE(format,type,width,height) glReadPixels=wrapper.wrapper(glReadPixels)
### END AUTOGENERATED SECTION
from OpenGL import converters
from OpenGL.lazywrapper import lazy as _lazy

glShaderSource = platform.createExtensionFunction(
    'glShaderSource', dll=platform.PLATFORM.GLES2,
    resultType=None,
    argTypes=(_types.GLhandle, _types.GLsizei, ctypes.POINTER(ctypes.c_char_p), arrays.GLintArray,),
    doc = 'glShaderSource( GLhandle(shaderObj),[bytes(string),...]) -> None',
    argNames = ('shaderObj', 'count', 'string', 'length',),
    extension = _EXTENSION_NAME,
)

conv = converters.StringLengths( name='string' )
glShaderSource = wrapper.wrapper(
    glShaderSource
).setPyConverter(
    'count' # number of strings
).setPyConverter(
    'length' # lengths of strings
).setPyConverter(
    'string', conv.stringArray
).setCResolver(
    'string', conv.stringArrayForC,
).setCConverter(
    'length', conv,
).setCConverter(
    'count', conv.totalCount,
)
try:
    del conv
except NameError as err:
    pass

glGetShaderiv = wrapper.wrapper( glGetShaderiv ).setOutput(
    'params',
    size=(1,), 
    arrayType=arrays.GLintArray,
    orPassIn = True,
)


@_lazy( glGetShaderInfoLog )
def glGetShaderInfoLog( baseOperation, obj ):
    """Retrieve the shader's error messages as a Python string

    returns string which is '' if no message
    """
    length = int(glGetShaderiv(obj, GL_INFO_LOG_LENGTH))
    if length > 0:
        log = ctypes.create_string_buffer(length)
        baseOperation(obj, length, None, log)
        return log.value.strip(_NULL_8_BYTE) # null-termination
    return ''
@_lazy( glGetProgramInfoLog )
def glGetProgramInfoLog( baseOperation, obj ):
    """Retrieve the shader program's error messages as a Python string

    returns string which is '' if no message
    """
    length = int(glGetProgramiv(obj, GL_INFO_LOG_LENGTH))
    if length > 0:
        log = ctypes.create_string_buffer(length)
        baseOperation(obj, length, None, log)
        return log.value.strip(_NULL_8_BYTE) # null-termination
    return ''

@_lazy( glGetAttachedShaders )
def glGetAttachedShaders( baseOperation, obj ):
    """Retrieve the attached objects as an array of GLhandle instances"""
    length= glGetProgramiv( obj, GL_ATTACHED_SHADERS )
    if length > 0:
        storage = arrays.GLuintArray.zeros( (length,))
        baseOperation( obj, length, None, storage )
        return storage
    return arrays.GLuintArray.zeros( (0,))


@_lazy( glGetShaderSource )
def glGetShaderSource( baseOperation, obj ):
    """Retrieve the program/shader's source code as a Python string

    returns string which is '' if no source code
    """
    length = int(glGetShaderiv(obj, GL_OBJECT_SHADER_SOURCE_LENGTH))
    if length > 0:
        source = ctypes.create_string_buffer(length)
        baseOperation(obj, length, None, source)
        return source.value.strip(_NULL_8_BYTE) # null-termination
    return ''

@_lazy( glGetActiveUniform )
def glGetActiveUniform(baseOperation,program, index):
    """Retrieve the name, size and type of the uniform of the index in the program"""
    max_index = int(glGetProgramiv( program, GL_OBJECT_ACTIVE_UNIFORMS ))
    length = int(glGetProgramiv( program, GL_OBJECT_ACTIVE_UNIFORM_MAX_LENGTH))
    if index < max_index and index >= 0:
        if length > 0:
            name = ctypes.create_string_buffer(length)
            size = arrays.GLintArray.zeros( (1,))
            gl_type = arrays.GLenumArray.zeros( (1,))
            namelen = arrays.GLsizeiArray.zeros( (1,))
            baseOperation(program, index, length, namelen, size, gl_type, name)
            return name.value[:int(namelen[0])], size[0], gl_type[0]
        raise ValueError( """No currently specified uniform names""" )
    raise IndexError( 'Index %s out of range 0 to %i' % (index, max_index - 1, ) )

@_lazy( glGetUniformLocation )
def glGetUniformLocation( baseOperation, program, name ):
    """Check that name is a string with a null byte at the end of it"""
    if not name:
        raise ValueError( """Non-null name required""" )
    name = as_8_bit( name )
    if name[-1] != _NULL_8_BYTE:
        name = name + _NULL_8_BYTE
    return baseOperation( program, name )
@_lazy( glGetAttribLocation )
def glGetAttribLocation( baseOperation, program, name ):
    """Check that name is a string with a null byte at the end of it"""
    if not name:
        raise ValueError( """Non-null name required""" )
    
    name = as_8_bit( name )
    if name[-1] != _NULL_8_BYTE:
        name = name + _NULL_8_BYTE
    return baseOperation( program, name )

@_lazy( glVertexAttribPointer )
def glVertexAttribPointer(
    baseOperation, index, size, type,
    normalized, stride, pointer,
):
    """Set an attribute pointer for a given shader (index)

    index -- the index of the generic vertex to bind, see
        glGetAttribLocation for retrieval of the value,
        note that index is a global variable, not per-shader
    size -- number of basic elements per record, 1,2,3, or 4
    type -- enum constant for data-type
    normalized -- whether to perform int to float
        normalization on integer-type values
    stride -- stride in machine units (bytes) between
        consecutive records, normally used to create
        "interleaved" arrays
    pointer -- data-pointer which provides the data-values,
        normally a vertex-buffer-object or offset into the
        same.

    This implementation stores a copy of the data-pointer
    in the contextdata structure in order to prevent null-
    reference errors in the renderer.
    """
    array = ArrayDatatype.asArray( pointer, type )
    key = ('vertex-attrib',index)
    contextdata.setValue( key, array )
    return baseOperation(
        index, size, type,
        normalized, stride,
        ArrayDatatype.voidDataPointer( array )
    )

