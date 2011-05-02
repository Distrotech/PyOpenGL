"""8-bit string definition for Python 2/3 compatibility"""
try:
    bytes = bytes
    _NULL_8_BYTE = bytes( '\000','latin1' )
    def as_8_bit( x, encoding='utf-8' ):
        if isinstance( x,unicode ):
            return x.encode(encoding)
        return str(x).encode( encoding )
except NameError, err:
    bytes = str 
    _NULL_8_BYTE = '\000'
    def as_8_bit( x, encoding='utf-8' ):
        if isinstance( x, unicode ):
            return x.encode( encoding )
        return bytes( x ) 
