import ctypes
from OpenGL import error

cdef class Wrapper:
	"""C-coded most-generic form of the wrapper's core function"""
	cdef public object calculate_pyArgs, calculate_cArgs, calculate_cArguments, wrappedOperation, storeValues,returnValues
	def __init__( 
		self, wrappedOperation,
		calculate_pyArgs=None, calculate_cArgs=None,
		calculate_cArguments=None, 
		storeValues=None, returnValues=None,
	):
		self.calculate_pyArgs = calculate_pyArgs
		self.calculate_cArgs = calculate_cArgs
		self.calculate_cArguments = calculate_cArguments
		self.wrappedOperation = wrappedOperation
		self.storeValues = storeValues
		self.returnValues = returnValues
	
	def __call__( self, *args ):
		cdef tuple pyArgs, cArgs, cArguments
		if self.calculate_pyArgs is not None:
			pyArgs = tuple(self.calculate_pyArgs( args ))
		else:
			pyArgs = args 
		if self.calculate_cArgs is not None:
			cArgs = tuple(self.calculate_cArgs( pyArgs ))
		else:
			cArgs = pyArgs
		if self.calculate_cArguments is not None:
			cArguments = tuple(self.calculate_cArguments( cArgs ))
		else:
			cArguments = cArgs
		try:
			result = self.wrappedOperation( *cArguments )
		except (ctypes.ArgumentError,TypeError,AttributeError), err:
			err.args = err.args + (cArguments,)
			raise err
		except error.GLError, err:
			err.cArgs = cArgs 
			err.pyArgs = pyArgs
			raise err
		# handle storage of persistent argument values...
		if self.storeValues:
			self.storeValues(
				result,
				self,
				pyArgs,
				cArgs,
			)
		if self.returnValues:
			return self.returnValues(
				result,
				self,
				pyArgs,
				cArgs,
			)
		else:
			return result

cdef class CArgCalculatorElement:
	cdef object wrapper
	cdef long index 
	cdef int callable
	cdef object converter 
	def __init__( self, wrapper, index, converter ):
		self.wrapper = wrapper 
		self.index = index 
		self.converter = converter
		self.callable = callable( converter )
	def __call__( self, pyArgs ):
		"""If callable, call converter( pyArgs, index, wrapper ), else return converter"""
		if self.callable:
			return self.converter( pyArgs, self.index, self.wrapper )
		return self.converter

cdef class CArgCalculator:
	"""C-coded version of the c-arg calculator pattern"""
	cdef list mapping
	def __init__( 
		self,
		wrapper,
		cConverters
	):
		self.mapping = [
			CArgCalculatorElement(self,i,converter)
			for (i,converter) in enumerate( cConverters )
		]
	def __call__( self, pyArgs ):
		return [
			calc( pyArgs )
			for calc in self.mapping
		]

cdef class PyArgCalculatorElement:
	cdef object wrapper
	cdef long index 
	cdef int callable
	cdef object converter 
	def __init__( self, wrapper, index, converter ):
		self.wrapper = wrapper 
		self.index = index 
		self.converter = converter
	def __call__( self, args ):
		"""If callable, call converter( pyArgs, index, wrapper ), else return converter"""
		if self.converter is None:
			return args[self.index]
		try:
			return self.converter( 
				args[self.index], self.wrapper, args 
			)
		except Exception, err:
			if hasattr( err, 'args' ):
				err.args += ( self.converter, )
			raise

cdef class PyArgCalculator:
	"""C-coded version of the py-arg calculator pattern"""
	cdef list mapping
	cdef int length
	def __init__( 
		self,
		wrapper,
		pyConverters
	):
		self.mapping = [
			PyArgCalculatorElement(self,i,converter)
			for (i,converter) in enumerate( pyConverters )
		]
		self.length = len(pyConverters)
		
	def __call__( self, args ):
		if self.length != len(args):
			raise ValueError(
				"""%s requires %r arguments (%s), received %s: %r"""%(
					self.wrapper.wrappedOperation.__name__,
					self.length,
					", ".join( self.wrapper.pyConverterNames ),
					len(args),
					args
				)
			)
		return [
			calc( args )
			for calc in self.mapping
		]

cdef class HandlerRegistry:
	cdef dict registry
	cdef object match
	def __init__( self, plugin_match ):
		self.registry = {}
		self.match = plugin_match
	def __setitem__( self,key,value ):
		self.registry[key] = value
	def __call__( self, value ):
		cdef type typ,base
		typ = value.__class__
		handler = self.registry.get( typ )
		if handler is None:
			if hasattr( typ, '__mro__' ):
				for base in typ.__mro__:
					handler = self.registry.get( base )
					if handler is None:
						handler = self.match( base )
					if handler:
						handler = self.registry[ base ]
						handler.registerEquivalent( typ, base )
						self.registry[ typ ] = handler 
						return handler
			raise TypeError(
				"""No array-type handler for type %r (value: %s) registered"""%(
					typ, repr(value)[:50]
				)
			)
		return handler
