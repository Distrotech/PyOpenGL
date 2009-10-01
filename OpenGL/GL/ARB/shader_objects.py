'''OpenGL extension ARB.shader_objects

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.shader_objects to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.ARB.shader_objects import *
### END AUTOGENERATED SECTION
EXTENSION_NAME = 'GL_ARB_shader_objects'
import OpenGL
from OpenGL.lazywrapper import lazy
from OpenGL import converters, error
GL_INFO_LOG_LENGTH_ARB = constant.Constant( 'GL_INFO_LOG_LENGTH_ARB', 0x8B84 )

glShaderSourceARB = platform.createExtensionFunction( 
    'glShaderSourceARB', dll=platform.GL,
    resultType=None, 
    argTypes=(constants.GLhandleARB, constants.GLsizei, ctypes.POINTER(ctypes.c_char_p), arrays.GLintArray,),
    doc = 'glShaderSourceARB( GLhandleARB(shaderObj), [str(string),...] ) -> None',
    argNames = ('shaderObj', 'count', 'string', 'length',),
    extension = EXTENSION_NAME,
)
conv = converters.StringLengths( name='string' )
glShaderSourceARB = wrapper.wrapper(
    glShaderSourceARB
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
del conv

for size in (1,2,3,4):
    for format,arrayType in (
        ('f',arrays.GLfloatArray),
        ('i',arrays.GLintArray),
    ):
        name = 'glUniform%(size)s%(format)svARB'%globals()
        globals()[name] = arrays.setInputArraySizeType(
            globals()[name],
            None, # don't want to enforce size...
            arrayType, 
            'value',
        )
        del format, arrayType
    del size

@lazy( glGetObjectParameterivARB )
def glGetObjectParameterivARB( baseOperation, shader, pname ):
    """Retrieve the integer parameter for the given shader"""
    status = arrays.GLintArray.zeros( (1,))
    status[0] = 1 
    baseOperation(
        shader, pname, status
    )
    return status[0]

@lazy( glGetObjectParameterfvARB )
def glGetObjectParameterfvARB( baseOperation, shader, pname ):
    """Retrieve the float parameter for the given shader"""
    status = arrays.GLfloatArray.zeros( (1,))
    status[0] = 1.0
    baseOperation(shader, pname,status)
    return status[0]

def _afterCheck( key ):
    """Generate an error-checking function for compilation operations"""
    def GLSLCheckError( 
        result,
        baseOperation=None,
        cArguments=None,
        *args
    ):
        result = error.glCheckError( result, baseOperation, cArguments, *args )
        status = glGetObjectParameterivARB(
            cArguments[0], key
        )
        if not status:
            raise error.GLError( 
                result = result,
                baseOperation = baseOperation,
                cArguments = cArguments,
                description= glGetInfoLogARB( cArguments[0] )
            )
        return result
    return GLSLCheckError

if OpenGL.ERROR_CHECKING:
    glCompileShaderARB.errcheck = _afterCheck( GL_OBJECT_COMPILE_STATUS_ARB )
if OpenGL.ERROR_CHECKING:
    glLinkProgramARB.errcheck = _afterCheck( GL_OBJECT_LINK_STATUS_ARB )
## Not sure why, but these give invalid operation :(
##if glValidateProgramARB and OpenGL.ERROR_CHECKING:
##	glValidateProgramARB.errcheck = _afterCheck( GL_OBJECT_VALIDATE_STATUS_ARB )

@lazy( glGetInfoLogARB )
def glGetInfoLogARB( baseOperation, obj ):
    """Retrieve the program/shader's error messages as a Python string
    
    returns string which is '' if no message
    """
    length = int(glGetObjectParameterivARB(obj, GL_INFO_LOG_LENGTH_ARB))
    if length > 0:
        log = ctypes.create_string_buffer(length)
        baseOperation(obj, length, None, log)
        return log.value.strip('\000') # null-termination
    return ''

@lazy( glGetAttachedObjectsARB )
def glGetAttachedObjectsARB( baseOperation, obj ):
    """Retrieve the attached objects as an array of GLhandleARB instances"""
    length= glGetObjectParameterivARB( obj, GL_OBJECT_ATTACHED_OBJECTS_ARB )
    if length > 0:
        storage = arrays.GLuintArray.zeros( (length,))
        baseOperation( obj, length, None, storage )
        return storage
    return arrays.GLuintArray.zeros( (0,))

@lazy( glGetShaderSourceARB )
def glGetShaderSourceARB( baseOperation, obj ):
    """Retrieve the program/shader's source code as a Python string
    
    returns string which is '' if no source code
    """
    length = int(glGetObjectParameterivARB(obj, GL_OBJECT_SHADER_SOURCE_LENGTH_ARB))
    if length > 0:
        source = ctypes.create_string_buffer(length)
        baseOperation(obj, length, None, source)
        return source.value.strip('\000') # null-termination
    return ''

@lazy( glGetActiveUniformARB )
def glGetActiveUniformARB(baseOperation, program, index):
    """Retrieve the name, size and type of the uniform of the index in the program"""
    max_index = int(glGetObjectParameterivARB( program, GL_OBJECT_ACTIVE_UNIFORMS_ARB ))
    length = int(glGetObjectParameterivARB( program, GL_OBJECT_ACTIVE_UNIFORM_MAX_LENGTH_ARB))
    if index < max_index and index >= 0:
        if length > 0:
            name = ctypes.create_string_buffer(length)
            size = arrays.GLintArray.zeros( (1,))
            gl_type = arrays.GLuintArray.zeros( (1,))
            baseOperation(program, index, length, None, size, gl_type, name)
            return name.value, size[0], gl_type[0]
        raise ValueError( """No currently specified uniform names""" )
    raise IndexError, 'Index %s out of range 0 to %i' % (index, max_index - 1, )

@lazy( glGetUniformLocationARB )
def glGetUniformLocationARB( baseOperation, program, name ):
    """Check that name is a string with a null byte at the end of it"""
    if not name:
        raise ValueError( """Non-null name required""" )
    elif name[-1] != '\000':
        name = name + '\000'
    return baseOperation( program, name )
