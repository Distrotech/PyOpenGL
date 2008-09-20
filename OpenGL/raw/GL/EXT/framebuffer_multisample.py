'''OpenGL extension EXT.framebuffer_multisample

Overview (from the spec)
	
	This extension extends the EXT_framebuffer_object framework to
	enable multisample rendering.
	
	The new operation RenderbufferStorageMultisampleEXT() allocates
	storage for a renderbuffer object that can be used as a multisample
	buffer.  A multisample render buffer image differs from a
	single-sample render buffer image in that a multisample image has a
	number of SAMPLES that is greater than zero.  No method is provided
	for creating multisample texture images.
	
	All of the framebuffer-attachable images attached to a framebuffer
	object must have the same number of SAMPLES or else the framebuffer
	object is not "framebuffer complete".  If a framebuffer object with
	multisample attachments is "framebuffer complete", then the
	framebuffer object behaves as if SAMPLE_BUFFERS is one.
	
	In traditional multisample rendering, where
	DRAW_FRAMEBUFFER_BINDING_EXT is zero and SAMPLE_BUFFERS is one, the
	GL spec states that "the color sample values are resolved to a
	single, displayable color each time a pixel is updated."  There are,
	however, several modern hardware implementations that do not
	actually resolve for each sample update, but instead postpones the
	resolve operation to a later time and resolve a batch of sample
	updates at a time.  This is OK as long as the implementation behaves
	"as if" it had resolved a sample-at-a-time. Unfortunately, however,
	honoring the "as if" rule can sometimes degrade performance.
	
	In contrast, when DRAW_FRAMEBUFFER_BINDING_EXT is an
	application-created framebuffer object, MULTISAMPLE is enabled, and
	SAMPLE_BUFFERS is one, there is no implicit per-sample-update
	resolve.  Instead, the application explicitly controls when the
	resolve operation is performed.  The resolve operation is affected
	by calling BlitFramebufferEXT (provided by the EXT_framebuffer_blit
	extension) where the source is a multisample application-created
	framebuffer object and the destination is a single-sample
	framebuffer object (either application-created or window-system
	provided).
	
	This design for multisample resolve more closely matches current
	hardware, but still permits implementations which choose to resolve
	a single sample at a time.  If hardware that implementes the
	multisample resololution "one sample at a time" exposes
	EXT_framebuffer_multisample, it could perform the implicit resolve
	to a driver-managed hidden surface, then read from that surface when
	the application calls BlitFramebufferEXT.
	
	Another motivation for granting the application explicit control
	over the multisample resolve operation has to do with the
	flexibility afforded by EXT_framebuffer_object.  Previously, a
	drawable (window or pbuffer) had exclusive access to all of its
	buffers.  There was no mechanism for sharing a buffer across
	multiple drawables.  Under EXT_framebuffer_object, however, a
	mechanism exists for sharing a framebuffer-attachable image across
	several framebuffer objects, as well as sharing an image between a
	framebuffer object and a texture.  If we had retained the "implicit"
	resolve from traditional multisampled rendering, and allowed the
	creation of "multisample" format renderbuffers, then this type of
	sharing would have lead to two problematic situations:
	
	  * Two contexts, which shared renderbuffers, might perform
	    competing resolve operations into the same single-sample buffer
	    with ambiguous results.
	
	  * It would have introduced the unfortunate ability to use the
	    single-sample buffer as a texture while MULTISAMPLE is ENABLED.
	
	By using the BlitFramebufferEXT from EXT_framebuffer_blit as an
	explicit resolve to serialize access to the multisampeld contents
	and eliminate the implicit per-sample resolve operation, we avoid
	both of these problems.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/EXT/framebuffer_multisample.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_framebuffer_multisample'
GL_RENDERBUFFER_SAMPLES_EXT = constant.Constant( 'GL_RENDERBUFFER_SAMPLES_EXT', 0x8CAB )
GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_EXT = constant.Constant( 'GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_EXT', 0x8D56 )
GL_MAX_SAMPLES_EXT = constant.Constant( 'GL_MAX_SAMPLES_EXT', 0x8D57 )
glRenderbufferStorageMultisampleEXT = platform.createExtensionFunction( 
	'glRenderbufferStorageMultisampleEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLsizei, constants.GLenum, constants.GLsizei, constants.GLsizei,),
	doc = 'glRenderbufferStorageMultisampleEXT( GLenum(target), GLsizei(samples), GLenum(internalformat), GLsizei(width), GLsizei(height) ) -> None',
	argNames = ('target', 'samples', 'internalformat', 'width', 'height',),
)


def glInitFramebufferMultisampleEXT():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
