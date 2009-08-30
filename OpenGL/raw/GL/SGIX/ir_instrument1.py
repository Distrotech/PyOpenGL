'''OpenGL extension SGIX.ir_instrument1

Overview (from the spec)


The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/SGIX/ir_instrument1.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SGIX_ir_instrument1'
_DEPRECATED = False
GL_IR_INSTRUMENT1_SGIX = constant.Constant( 'GL_IR_INSTRUMENT1_SGIX', 0x817F )


def glInitIrInstrument1SGIX():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
