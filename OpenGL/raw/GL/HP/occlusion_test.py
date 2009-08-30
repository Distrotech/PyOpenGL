'''OpenGL extension HP.occlusion_test

Overview (from the spec)


The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/HP/occlusion_test.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_HP_occlusion_test'
_DEPRECATED = False
GL_OCCLUSION_TEST_HP = constant.Constant( 'GL_OCCLUSION_TEST_HP', 0x8165 )
glget.addGLGetConstant( GL_OCCLUSION_TEST_HP, (1,) )
GL_OCCLUSION_TEST_RESULT_HP = constant.Constant( 'GL_OCCLUSION_TEST_RESULT_HP', 0x8166 )
glget.addGLGetConstant( GL_OCCLUSION_TEST_RESULT_HP, (1,) )


def glInitOcclusionTestHP():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
