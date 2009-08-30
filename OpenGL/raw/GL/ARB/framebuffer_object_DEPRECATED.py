'''OpenGL extension ARB.framebuffer_object_DEPRECATED

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/ARB/framebuffer_object_DEPRECATED.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_framebuffer_object'
_DEPRECATED = True
GL_INDEX = constant.Constant( 'GL_INDEX', 0x8222 )
GL_TEXTURE_LUMINANCE_TYPE = constant.Constant( 'GL_TEXTURE_LUMINANCE_TYPE', 0x8C14 )
GL_TEXTURE_INTENSITY_TYPE = constant.Constant( 'GL_TEXTURE_INTENSITY_TYPE', 0x8C15 )


def glInitFramebufferObjectDeprecatedARB():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
