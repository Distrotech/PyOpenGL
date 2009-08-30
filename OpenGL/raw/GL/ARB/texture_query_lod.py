'''OpenGL extension ARB.texture_query_lod

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/ARB/texture_query_lod.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_texture_query_lod'
_DEPRECATED = False



def glInitTextureQueryLodARB():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
