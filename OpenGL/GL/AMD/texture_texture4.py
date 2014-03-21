'''OpenGL extension AMD.texture_texture4

This module customises the behaviour of the 
OpenGL.raw.GL.AMD.texture_texture4 to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension adds new shading language built-in texture functions
	to the shading language.
	
	These texture functions may be used to access one component textures.
	
	The texture4 built-in function returns a texture value derived from
	a 2x2 set of texels in the image array of level levelbase is selected.
	These texels are selected in the same way as when the value of
	TEXTURE_MIN_FILTER is LINEAR, but instead of these texels being
	filtered to generate the texture value, the R, G, B and A texture values
	are derived directly from these four texels.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/AMD/texture_texture4.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.AMD.texture_texture4 import *
from OpenGL.raw.GL.AMD.texture_texture4 import _EXTENSION_NAME

def glInitTextureTexture4AMD():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION