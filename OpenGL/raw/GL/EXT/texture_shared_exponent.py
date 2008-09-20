'''OpenGL extension EXT.texture_shared_exponent

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/EXT/texture_shared_exponent.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_texture_shared_exponent'
GL_RGB9_E5_EXT = constant.Constant( 'GL_RGB9_E5_EXT', 0x8C3D )
GL_UNSIGNED_INT_5_9_9_9_REV_EXT = constant.Constant( 'GL_UNSIGNED_INT_5_9_9_9_REV_EXT', 0x8C3E )
GL_TEXTURE_SHARED_SIZE_EXT = constant.Constant( 'GL_TEXTURE_SHARED_SIZE_EXT', 0x8C3F )


def glInitTextureSharedExponentEXT():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
