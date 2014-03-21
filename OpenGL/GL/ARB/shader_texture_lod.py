'''OpenGL extension ARB.shader_texture_lod

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.shader_texture_lod to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension adds additional texture functions to the
	OpenGL Shading Language which provide the shader writer
	with explicit control of LOD.
	
	Mipmap texture fetches and anisotropic texture fetches
	require an implicit derivatives to calculate rho, lambda
	and/or the line of anisotropy.  These implicit derivatives
	will be undefined for texture fetches occurring inside
	non-uniform control flow or for vertex shader texture
	fetches, resulting in undefined texels.
	
	The additional texture functions introduced with
	this extension provide explict control of LOD
	(isotropic texture functions) or provide explicit
	derivatives (anisotropic texture functions).
	
	Anisotropic texture functions return defined texels
	for mipmap texture fetches or anisotropic texture fetches,
	even inside non-uniform control flow.  Isotropic texture
	functions return defined texels for mipmap texture fetches,
	even inside non-uniform control flow.  However, isotropic
	texture functions return undefined texels for anisotropic
	texture fetches.
	
	The existing isotropic vertex texture functions:
	
	    texture1DLod,   texture1DProjLod,
	    texture2DLod,   texture2DProjLod,
	    texture3DLod,   texture3DProjLod,
	    textureCubeLod,
	    shadow1DLod,    shadow1DProjLod,
	    shadow2DLod,    shadow2DProjLod,
	
	are added to the built-in functions for fragment shaders.
	
	New anisotropic texture functions, providing explicit
	derivatives:
	
	    texture1DGradARB(         sampler1D sampler,
	                              float P, float dPdx, float dPdy );
	    texture1DProjGradARB(     sampler1D sampler,
	                              vec2  P, float dPdx, float dPdy );
	    texture1DProjGradARB(     sampler1D sampler,
	                              vec4  P, float dPdx, float dPdy );
	
	    texture2DGradARB(         sampler2D sampler,
	                              vec2  P, vec2  dPdx, vec2  dPdy );
	    texture2DProjGradARB(     sampler2D sampler,
	                              vec3  P, vec2  dPdx, vec2  dPdy );
	    texture2DProjGradARB(     sampler2D sampler,
	                              vec4  P, vec2  dPdx, vec2  dPdy );
	
	    texture3DGradARB(         sampler3D sampler,
	                              vec3  P, vec3  dPdx, vec3  dPdy );
	    texture3DProjGradARB(     sampler3D sampler,
	                              vec4  P, vec3  dPdx, vec3  dPdy );
	
	    textureCubeGradARB(       samplerCube sampler,
	                              vec3  P, vec3  dPdx, vec3  dPdy );
	
	    shadow1DGradARB(          sampler1DShadow sampler,
	                              vec3  P, float dPdx, float dPdy );
	    shadow1DProjGradARB(      sampler1DShadow sampler,
	                              vec4  P, float dPdx, float dPdy );
	
	    shadow2DGradARB(          sampler2DShadow sampler,
	                              vec3  P, vec2  dPdx, vec2  dPdy );
	    shadow2DProjGradARB(      sampler2DShadow sampler,
	                              vec4  P, vec2  dPdx, vec2  dPdy );
	
	
	    texture2DRectGradARB(     sampler2DRect sampler,
	                              vec2  P, vec2  dPdx, vec2  dPdy );
	    texture2DRectProjGradARB( sampler2DRect sampler,
	                              vec3  P, vec2  dPdx, vec2  dPdy );
	    texture2DRectProjGradARB( sampler2DRect sampler,
	                              vec4  P, vec2  dPdx, vec2  dPdy );
	
	    shadow2DRectGradARB(      sampler2DRectShadow sampler,
	                              vec3  P, vec2  dPdx, vec2  dPdy );
	    shadow2DRectProjGradARB(  sampler2DRectShadow sampler,
	                              vec4  P, vec2  dPdx, vec2  dPdy );
	
	 are added to the built-in functions for vertex shaders
	 and fragment shaders.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/shader_texture_lod.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.ARB.shader_texture_lod import *
from OpenGL.raw.GL.ARB.shader_texture_lod import _EXTENSION_NAME

def glInitShaderTextureLodARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION