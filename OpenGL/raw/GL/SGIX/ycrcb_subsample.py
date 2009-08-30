'''OpenGL extension SGIX.ycrcb_subsample

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/SGIX/ycrcb_subsample.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SGIX_ycrcb_subsample'
_DEPRECATED = False



def glInitYcrcbSubsampleSGIX():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
