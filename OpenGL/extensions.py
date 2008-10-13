"""Extension module support methods

This module provides the tools required to check whether
an extension is available
"""
VERSION_PREFIX = 'GL_VERSION_GL_'
CURRENT_GL_VERSION = ''
AVAILABLE_GL_EXTENSIONS = []
AVAILABLE_GLU_EXTENSIONS = []

def hasGLExtension( specifier ):
	"""Given a string specifier, check for extension being available"""
	global AVAILABLE_GL_EXTENSIONS, CURRENT_GL_VERSION
	specifier = specifier.replace('.','_')
	if specifier.startswith( VERSION_PREFIX ):
		from OpenGL.GL import glGetString, GL_VERSION
		if not CURRENT_GL_VERSION:
			new = glGetString( GL_VERSION )
			if new:
				CURRENT_GL_VERSION = [
					int(x) for x in new.split(' ',1)[0].split( '.' )
				]
			else:
				return False # not yet loaded/supported
		specifier = [
			int(x) 
			for x in specifier[ len(VERSION_PREFIX):].split('_')
		]
		return specifier <= CURRENT_GL_VERSION
	else:
		from OpenGL.GL import glGetString, GL_EXTENSIONS
		if not AVAILABLE_GL_EXTENSIONS:
			AVAILABLE_GL_EXTENSIONS[:] = glGetString( GL_EXTENSIONS ).split()
		return specifier in AVAILABLE_GL_EXTENSIONS

def hasGLUExtension( specifier ):
	"""Given a string specifier, check for extension being available"""
	from OpenGL.GLU import gluGetString, GLU_EXTENSIONS
	if not AVAILABLE_GLU_EXTENSIONS:
		AVAILABLE_GLU_EXTENSIONS[:] = gluGetString( GLU_EXTENSIONS )
	return specifier.replace('.','_') in AVAILABLE_GLU_EXTENSIONS

class _Alternate( object ):
	resolved = False 
	implementation = None
	def __init__( self, name, *alternates ):
		"""Initialize set of alternative implementations of the same function"""
		self.__name__ = name
		self._alternatives = alternates
	def __nonzero__( self ):
		for alternate in self._alternatives:
			if alternate:
				return True 
		return False
	def __call__( self, *args, **named ):
		"""Call, doing a late lookup and bind to find an implementation"""
		for alternate in self._alternatives:
			if alternate:
				self.__class__.__call__ = alternate.__call__
				return self( *args, **named )
		from OpenGL import error
		raise error.NullFunctionError(
			"""Attempt to call an undefined alterate function (%s), check for bool(%s) before calling"""%(
				', '.join([x.__name__ for x in self._alternatives]),
				self.__name__,
			)
		)
def alternate( name, *functions ):
	"""Construct a callable that functions as the first implementation found of given set of alternatives
	
	if name is a function then its name will be used....
	"""
	if not isinstance( name, (str,unicode)):
		functions = (name,)+functions
		name = name.__name__
	return type( name, (_Alternate,), {} )( name, *functions )
