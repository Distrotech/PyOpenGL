"""Base class for platform implementations
"""
import ctypes
from OpenGL.platform import ctypesloader
import sys
import OpenGL as top_level_module
from OpenGL import logs

class BasePlatform( object ):
	"""Base class for per-platform implementations
	
	Attributes of note:
	
		EXPORTED_NAMES -- set of names exported via the platform 
			module's namespace...
	
		GL, GLU, GLUT, GLE, OpenGL -- ctypes libraries
	
		DEFAULT_FUNCTION_TYPE -- used as the default function 
			type for functions unless overridden on a per-DLL
			basis with a "FunctionType" member
		
		GLUT_GUARD_CALLBACKS -- if True, the GLUT wrappers 
			will provide guarding wrappers to prevent GLUT 
			errors with uninitialised GLUT.
		
		EXTENSIONS_USE_BASE_FUNCTIONS -- if True, uses regular
			dll attribute-based lookup to retrieve extension 
			function pointers.
	"""
	
	EXPORTED_NAMES = [
		'GetCurrentContext','CurrentContextIsValid','safeGetError',
		'createBaseFunction', 'createExtensionFunction', 'copyBaseFunction',
		'GL','GLU','GLUT','GLE','OpenGL',
		'getGLUTFontPointer',
		'GLUT_GUARD_CALLBACKS',
	]

	
	DEFAULT_FUNCTION_TYPE = None
	GLUT_GUARD_CALLBACKS = False
	EXTENSIONS_USE_BASE_FUNCTIONS = False
	
	def install( self, namespace ):
		"""Install this platform instance into the platform module"""
		for name in self.EXPORTED_NAMES:
			namespace[ name ] = getattr(self,name)
		namespace['PLATFORM'] = self
		return self
	
	def functionTypeFor( self, dll ):
		"""Given a DLL, determine appropriate function type..."""
		if hasattr( dll, 'FunctionType' ):
			return dll.FunctionType
		else:
			return self.DEFAULT_FUNCTION_TYPE
	
	def errorChecking( self, func ):
		"""Add error checking to the function if appropriate"""
		from OpenGL import error
		if top_level_module.ERROR_CHECKING:
			func.errcheck = error.glCheckError
		return func
	def wrapLogging( self, func ):
		"""Wrap function with logging operations if appropriate"""
		return logs.logOnFail( func, logs.getLog( 'OpenGL.errors' ))
	
	def constructFunction( 
		self,
		functionName, dll, 
		resultType=ctypes.c_int, argTypes=(),
		doc = None, argNames = (),
		extension = None,
	):
		"""Core operation to create a new base ctypes function
		
		raises AttributeError if can't find the procedure...
		"""
		if extension and not self.checkExtension( extension ):
			raise AttributeError( """Extension not available""" )
		if extension and not self.EXTENSIONS_USE_BASE_FUNCTIONS:
			# what about the VERSION values???
			if self.checkExtension( extension ):
				pointer = self.getExtensionProcedure( functionName )
				if pointer:
					func = self.functionTypeFor( dll )(
						resultType,
						*argTypes
					)(
						pointer
					)
				else:
					AttributeError( """Extension %r available, but no pointer for function %r"""%(extension,functionName))
			else:
				raise AttributeError( """No extension %r"""%(extension,))
		else:
			func = ctypesloader.buildFunction(
				self.functionTypeFor( dll )(
					resultType,
					*argTypes
				),
				functionName,
				dll,
			)
		func.__doc__ = doc 
		func.argNames = list(argNames or ())
		func.__name__ = functionName
		func.DLL = dll
		func.extension = extension
		func = self.wrapLogging( self.errorChecking( func ))
		return func

	def createBaseFunction( 
		self,
		functionName, dll, 
		resultType=ctypes.c_int, argTypes=(),
		doc = None, argNames = (),
		extension = None,
	):
		"""Create a base function for given name
		
		Normally you can just use the dll.name hook to get the object,
		but we want to be able to create different bindings for the 
		same function, so we do the work manually here to produce a
		base function from a DLL.
		"""
		from OpenGL import wrapper
		try:
			return self.constructFunction(
				functionName, dll, 
				resultType=resultType, argTypes=argTypes,
				doc = doc, argNames = argNames,
				extension = extension,
			)
		except AttributeError, err:
			return self.nullFunction( 
				functionName, dll=dll,
				resultType=resultType, 
				argTypes=argTypes,
				doc = doc, argNames = argNames,
				extension = extension,
			)
	def checkExtension( self, name ):
		"""Check whether the given extension is supported by current context"""
		if not name:
			return True
		context = self.GetCurrentContext()
		if context:
			from OpenGL import contextdata
			from OpenGL.raw.GL import GL_EXTENSIONS
			set = contextdata.getValue( GL_EXTENSIONS, context=context )
			if set is None:
				set = {}
				contextdata.setValue( 
					GL_EXTENSIONS, set, context=context, weak=False 
				)
			current = set.get( name )
			if current is None:
				from OpenGL import extensions
				result = extensions.hasGLExtension( name )
				set[name] = result 
				return result
			return current
		else:
			return False
	createExtensionFunction = createBaseFunction

	def copyBaseFunction( self, original ):
		"""Create a new base function based on an already-created function
		
		This is normally used to provide type-specific convenience versions of
		a definition created by the automated generator.
		"""
		from OpenGL import wrapper, error
		if isinstance( original, _NullFunctionPointer ):
			return self.nullFunction(
				original.__name__,
				original.DLL,
				resultType = original.restype,
				argTypes= original.argtypes,
				doc = original.__doc__,
				argNames = original.argNames,
				extension = original.extension,
			)
		elif hasattr( original, 'originalFunction' ):
			original = original.originalFunction
		return self.createBaseFunction(
			original.__name__, original.DLL, 
			resultType=original.restype, argTypes=original.argtypes,
			doc = original.__doc__, argNames = original.argNames,
			extension = original.argNames,
		)
	def nullFunction( 
		self,
		functionName, dll,
		resultType=ctypes.c_int, 
		argTypes=(),
		doc = None, argNames = (),
		extension = None,
	):
		"""Construct a "null" function pointer"""
		cls = type( functionName, (_NullFunctionPointer,), {
			'__doc__': doc,
		} )
		return cls(
			functionName, dll, resultType, argTypes, argNames, extension=extension, doc=doc,
		)
	def GetCurrentContext( self ):
		"""Retrieve opaque pointer for the current context"""
		raise NotImplementedError( 
			"""Platform does not define a GetCurrentContext function""" 
		)
	def CurrentContextIsValid( self ):
		"""Return boolean of whether current context is valid"""
		raise NotImplementedError( 
			"""Platform does not define a CurrentContextIsValid function""" 
		)
	def getGLUTFontPointer(self, constant ):
		"""Retrieve a GLUT font pointer for this platform"""
		raise NotImplementedError( 
			"""Platform does not define a GLUT font retrieval function""" 
		)
	def safeGetError( self ):
		"""Safety-checked version of glError() call (checks for valid context first)"""
		raise NotImplementedError( 
			"""Platform does not define a safeGetError function""" 
		)

class _NullFunctionPointer( object ):
	"""Function-pointer-like object for undefined functions"""
	def __init__( self, name, dll, resultType, argTypes, argNames, extension=None, doc=None ):
		from OpenGL import error
		self.__name__ = name
		self.DLL = dll
		self.argNames = argNames
		self.argtypes = argTypes
		if top_level_module.ERROR_CHECKING:
			self.errcheck = error.glCheckError
		else:
			self.errcheck = None
		self.restype = resultType
		self.extension = extension
		self.doc = doc
	resolved = False
	def __nonzero__( self ):
		"""Make this object appear to be NULL"""
		if self.extension and not self.resolved:
			self.load()
		return self.resolved
	def load( self ):
		"""Attempt to load the function again, presumably with a context this time"""
		from OpenGL import platform
		if not platform.PLATFORM.checkExtension( self.extension ):
			return None
		try:
			func = platform.PLATFORM.constructFunction(
				self.__name__, self.DLL, 
				resultType=self.restype, 
				argTypes=self.argtypes,
				doc = self.doc, 
				argNames = self.argNames,
				extension = self.extension,
			)
		except AttributeError, err:
			return None 
		else:
			# now short-circuit so that we don't need to check again...
			self.__class__.__call__ = staticmethod( func.__call__ )
			self.resolved = True
			return func
		return None
	def __call__( self, *args, **named ):
		if self.load():
			return self( *args, **named )
		else:
			from OpenGL import error
			raise error.NullFunctionError(
				"""Attempt to call an undefined function %s, check for bool(%s) before calling"""%(
					self.__name__, self.__name__,
				)
			)
