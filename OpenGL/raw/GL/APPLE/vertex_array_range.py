'''OpenGL extension APPLE.vertex_array_range

Overview (from the spec)
	
	This extension is designed to allow very high vertex processing rates which
	are facilitated both by relieving the CPU of as much processing burden as
	possible and by allowing graphics hardware to directly access vertex data.
	Because this extension is implemented as an addition to the vertex array
	specification provided by OpenGL 1.1, applications can continue to use
	existing vertex submission logic while taking advantage of vertex array
	ranges to more efficiently process those arrays.
	
	The vertex array coherency model provided by OpenGL 1.1 requires that
	vertex data specified in vertex arrays be transferred from system memory
	each time Begin, DrawArrays, or DrawElements is called.  Further, OpenGL
	1.1 requires that the transfer of data be completed by the time End,
	DrawArrays, or DrawElements returns.  Both of these requirements are
	relaxed by the vertex array range extension.  Vertex data may be cached
	by the GL so there is no guarantee that changes to the vertex data will
	be reflected in following drawing commands unless it is flushed with
	FlushVertexArrayRangeAPPLE.  The reading of vertex data may be deferred 
	by the GL so there is no guarantee that the GL will be finished reading
	the data until completion is forced by the use of Finish or the APPLE_fence
	extension.
	
	EnableClientState must be used with the VERTEX_ARRAY_RANGE_APPLE param to
	enable vertex array range.  Once this is done use of vertex array range
	requires the definition of a specific memory range for vertex data through
	VertexArrayRangeAPPLE.  It is recommended this data be page aligned (4096
	byte boundaries) and a multiple of page size in length for maximum
	efficiency in data handling and internal flushing, but this is not a
	requirement and any location and length of data can be defined as a vertex
	array.  This extension provides no memory allocators as any convenient
	memory allocator can be used.
	
	Once a data set is established, using VertexArrayRangeAPPLE, it can be can
	be drawn using standard OpenGL vertex array commands, as one would do
	without this extension.  Note, if any the data for any enabled array for a
	given array element index falls outside of the vertex array range, an
	undefined vertex is generated.  One should also understand removing or
	replacing all calls to vertex array range functions with no-ops or disabling
	the vertex array range by disabling the VERTEX_ARRAY_RANGE_APPLE client
	state should not change the results of an application's OpenGL drawing.
	
	For static data no addition coherency nor synchronization must be done and
	the client is free to draw with the specified draw as it sees fit.
	
	If data is dynamic, thus to be modified, FlushVertexArrayRangeAPPLE should
	be used.  The command is issued when data has been modified since the last
	call to VertexArrayRangeAPPLE or FlushVertexArrayRangeAPPLE and prior to
	drawing with such data. FlushVertexArrayRangeAPPLE only provides memory
	coherency prior to drawing (such as ensuring CPU caches are flushed or VRAM
	cached copies are updated) and does not provide any synchronization with
	previously issued drawing commands. The range flushed can be the specific
	range modified and does not have to be the entire vertex array range.
	Additionally, data maybe read immediately after a flush without need for
	further synchronization, thus overlapping areas of data maybe read, modified
	and written between two successive flushings and the data will be
	consistent.
	
	To synchronize data modification after drawing two methods can be used. A
	Finish command can be issued which will not return until all previously
	issued commands are complete, forcing completely synchronous operation.
	While this guarantees all drawing is complete it may not be the optimal
	solution for clients which just need to ensure drawing with the vertex array
	range or a specific range with the array is compete.  The APPLE_fence
	extension can be used when dynamic data modifications need to be
	synchronized with drawing commands. Specifically, if data is to be modified,
	a fence can be set immediately after drawing with the data.  Once it comes
	time to modify the data, the application must test (or finish) this fence to
	ensure the drawing command has completed. Failure to do this could result in
	new data being used by the previously issued drawing commands.  It should be
	noted that providing the maximum time between the drawing set fence and the
	modification test/finish fence allows the most asynchronous behavior and
	will result in the least stalling waiting for drawing completion. Techniques
	such as double buffering vertex data can be used to help further prevent
	stalls based on fence completion but are beyond the scope of this extension.
	
	Once an application is finished with a specific vertex array range or at
	latest prior to exit, and prior to freeing the memory associated with this
	vertex array, the client should call VertexArrayRangeAPPLE with a data
	location and length of 0 to allow the internal memory managers to complete
	any commitments for the array range.  In this case once
	VertexArrayRangeAPPLE returns it is safe to de-allocate the memory.
	
	An additional option is presented for vertex array ranges, the ability of
	the client to hint to OpenGL the type of access and/or use the vertex array
	memory is expected to have, by using VertexArrayParameteriAPPLE with either
	of the STORAGE_CACHED_APPLE or STORAGE_SHARED_APPLE parameter.  By default,
	all vertex array ranges are considered to be "shared".  These options allow
	the tuning of memory handling by OpenGL.  "Shared" memory is normally used
	for dynamic data that is expected to be modified and is likely mapped to AGP
	space for access by the graphics hardware and client.  "Cached" memory is
	designed to support static data and could be cached into to VRAM to provide
	the maximum access bandwidth for the vertex array.  Note, these hints can
	affect how array flushes are handled and the overhead associated with
	flushing the array, it is recommended that data be left as "shared" unless
	it really is static and there are no plans to modify it.
	
	To summarize the vertex array range extension provides relaxed
	synchronization rules for handling vertex array data allowing high bandwidth
	asynchronous data transfer from client memory to graphics hardware.
	Different flushing and synchronization rules are required to ensure data
	coherency when modifying data.  Lastly, memory handling hints are provided
	to allow the tunning of memory storage and access for maximum efficiency.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/APPLE/vertex_array_range.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_APPLE_vertex_array_range'
_DEPRECATED = False
GL_VERTEX_ARRAY_RANGE_APPLE = constant.Constant( 'GL_VERTEX_ARRAY_RANGE_APPLE', 0x851D )
GL_VERTEX_ARRAY_RANGE_LENGTH_APPLE = constant.Constant( 'GL_VERTEX_ARRAY_RANGE_LENGTH_APPLE', 0x851E )
glget.addGLGetConstant( GL_VERTEX_ARRAY_RANGE_LENGTH_APPLE, (1,) )
GL_VERTEX_ARRAY_STORAGE_HINT_APPLE = constant.Constant( 'GL_VERTEX_ARRAY_STORAGE_HINT_APPLE', 0x851F )
GL_VERTEX_ARRAY_RANGE_POINTER_APPLE = constant.Constant( 'GL_VERTEX_ARRAY_RANGE_POINTER_APPLE', 0x8521 )
GL_STORAGE_CACHED_APPLE = constant.Constant( 'GL_STORAGE_CACHED_APPLE', 0x85BE )
GL_STORAGE_SHARED_APPLE = constant.Constant( 'GL_STORAGE_SHARED_APPLE', 0x85BF )
glVertexArrayRangeAPPLE = platform.createExtensionFunction( 
	'glVertexArrayRangeAPPLE', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLsizei, ctypes.c_void_p,),
	doc = 'glVertexArrayRangeAPPLE( GLsizei(length), c_void_p(pointer) ) -> None',
	argNames = ('length', 'pointer',),
	deprecated = _DEPRECATED,
)

glFlushVertexArrayRangeAPPLE = platform.createExtensionFunction( 
	'glFlushVertexArrayRangeAPPLE', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLsizei, ctypes.c_void_p,),
	doc = 'glFlushVertexArrayRangeAPPLE( GLsizei(length), c_void_p(pointer) ) -> None',
	argNames = ('length', 'pointer',),
	deprecated = _DEPRECATED,
)

glVertexArrayParameteriAPPLE = platform.createExtensionFunction( 
	'glVertexArrayParameteriAPPLE', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLint,),
	doc = 'glVertexArrayParameteriAPPLE( GLenum(pname), GLint(param) ) -> None',
	argNames = ('pname', 'param',),
	deprecated = _DEPRECATED,
)


def glInitVertexArrayRangeAPPLE():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
