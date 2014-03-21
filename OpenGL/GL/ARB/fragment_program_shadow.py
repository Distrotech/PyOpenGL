'''OpenGL extension ARB.fragment_program_shadow

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.fragment_program_shadow to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension extends ARB_fragment_program to remove
	the interaction with ARB_shadow.
	
	This extension defines the program option
	"ARB_fragment_program_shadow".
	
	If a fragment program specifies the option "ARB_fragment_program_shadow"
	
	    SHADOW1D, SHADOW2D, SHADOWRECT
	
	are added as texture targets.  When shadow map comparisons are
	desired, specify the SHADOW1D, SHADOW2D, or SHADOWRECT texture
	targets in texture instructions.
	
	Programs must assure that the comparison mode for each depth
	texture (TEXTURE_COMPARE_MODE) and/or the internal texture
	format (DEPTH_COMPONENT) and the targets of the texture lookup
	instructions match.  Otherwise, if the comparison mode
	and/or the internal texture format are inconsistent with the
	texture target, the results of the texture lookup are undefined.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/fragment_program_shadow.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.ARB.fragment_program_shadow import *
from OpenGL.raw.GL.ARB.fragment_program_shadow import _EXTENSION_NAME

def glInitFragmentProgramShadowARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION

# This extension is entirely within the fragment program functionality,
# it doesn't affect the function-level operations AFAICS.