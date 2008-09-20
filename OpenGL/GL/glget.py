"""Implementation of the special "glGet" functions

For comparison, here's what a straightforward implementation looks like:

	def glGetDoublev( pname ):
		"Natural writing of glGetDoublev using standard ctypes"
		output = c_double*sizes.get( pname )
		result = output()
		result = platform.OpenGL.glGetDoublev( pname, byref(result) )
		return Numeric.array( result )
"""
from OpenGL import platform, arrays, error, wrapper, converters
from OpenGL.raw import GL as simple
import ctypes
GLenum = ctypes.c_uint
GLsize = GLsizei = ctypes.c_int

__all__ = (
	'glGetBoolean','glGetBooleanv','glGetInteger','glGetIntegerv',
	'glGetFloat','glGetFloatv','glGetDouble','glGetDoublev',
	'glGetString',
	'glGetLightfv','glGetLightiv',
	'glGetMaterialfv','glGetMaterialiv',
	'glGetPixelMapfv','glGetPixelMapusv','glGetPixelMapuiv',
	'glGetPolygonStipple', 'glGetPolygonStippleub',
	'glGetTexEnviv','glGetTexEnvfv',
	'glGetTexGenfv','glGetTexGeniv','glGetTexGendv',
	'glGetTexLevelParameteriv',
	'glGetTexLevelParameterfv',
	'glGetTexParameterfv',
	'glGetTexParameteriv',
)

glGetString = platform.OpenGL.glGetString
glGetString.restype = ctypes.c_char_p
glGetString.__doc__ = """glGetString( constant ) -> Current string value"""

GL_GET_SIZES = {
	simple.GL_AUX_BUFFERS                           : (1,),
	simple.GL_CLIP_PLANE0                           : (1,),
	simple.GL_CLIP_PLANE2                           : (1,),
	simple.GL_CLIP_PLANE3                           : (1,),
	simple.GL_CLIP_PLANE4                           : (1,),
	simple.GL_BLEND_COLOR                           : (4,),
	simple.GL_LIGHT0                                : (1,),
	simple.GL_CLIP_PLANE1                           : (1,),
	simple.GL_BLEND_EQUATION                        : (1,),
	simple.GL_STENCIL_BITS                          : (1,),
	simple.GL_LIGHT2                                : (1,),
	simple.GL_MAX_EVAL_ORDER                        : (1,),
	simple.GL_CONVOLUTION_1D                        : (1,),
	simple.GL_CONVOLUTION_2D                        : (1,),
	simple.GL_SEPARABLE_2D                          : (1,),
	simple.GL_LIGHT3                                : (1,),
	simple.GL_LIGHT4                                : (1,),
	simple.GL_POST_CONVOLUTION_RED_SCALE            : (1,),
	simple.GL_POST_CONVOLUTION_GREEN_SCALE          : (1,),
	simple.GL_POST_CONVOLUTION_BLUE_SCALE           : (1,),
	simple.GL_CLIP_PLANE5                           : (1,),
	simple.GL_INDEX_CLEAR_VALUE                     : (1,),
	simple.GL_INDEX_WRITEMASK                       : (1,),
	simple.GL_COLOR_CLEAR_VALUE                     : (4,),
	simple.GL_COLOR_WRITEMASK                       : (4,),
	simple.GL_HISTOGRAM                             : (1,),
	simple.GL_LIGHT6                                : (1,),
	simple.GL_MAP2_INDEX                            : (1,),
	simple.GL_PACK_SWAP_BYTES                       : (1,),
	simple.GL_LIGHT7                                : (1,),
	simple.GL_PIXEL_MAP_I_TO_R_SIZE                 : (1,),
	simple.GL_MINMAX                                : (1,),
	simple.GL_INDEX_MODE                            : (1,),
	simple.GL_RGBA_MODE                             : (1,),
	simple.GL_DOUBLEBUFFER                          : (1,),
	simple.GL_PIXEL_MAP_I_TO_G_SIZE                 : (1,),
	simple.GL_POLYGON_OFFSET_FILL                   : (1,),
	simple.GL_POLYGON_OFFSET_FACTOR                 : (1,),
	simple.GL_POST_COLOR_MATRIX_RED_SCALE           : (1,),
	simple.GL_RESCALE_NORMAL                        : (1,),
	simple.GL_POST_COLOR_MATRIX_GREEN_SCALE         : (1,),
	simple.GL_RENDER_MODE                           : (1,),
	simple.GL_POST_COLOR_MATRIX_BLUE_SCALE          : (1,),
	simple.GL_SCISSOR_BOX                           : (4,),
	simple.GL_TEXTURE_GEN_T                         : (1,),
	simple.GL_POST_COLOR_MATRIX_ALPHA_SCALE         : (1,),
	simple.GL_STENCIL_TEST                          : (1,),
	simple.GL_PERSPECTIVE_CORRECTION_HINT           : (1,),
	simple.GL_POINT_SMOOTH_HINT                     : (1,),
	simple.GL_LINE_SMOOTH_HINT                      : (1,),
	simple.GL_POLYGON_SMOOTH_HINT                   : (1,),
	simple.GL_FOG_HINT                              : (1,),
	simple.GL_POST_COLOR_MATRIX_GREEN_BIAS          : (1,),
	simple.GL_TEXTURE_GEN_S                         : (1,),
	simple.GL_POINT_SMOOTH                          : (1,),
	simple.GL_TEXTURE_GEN_R                         : (1,),
	simple.GL_TEXTURE_GEN_Q                         : (1,),
	simple.GL_SCISSOR_TEST                          : (1,),
	simple.GL_VERTEX_ARRAY                          : (1,),
	simple.GL_POINT_SIZE                            : (1,),
	simple.GL_TEXTURE_BINDING_1D                    : (1,),
	simple.GL_MAX_TEXTURE_SIZE                      : (1,),
	simple.GL_TEXTURE_BINDING_3D                    : (1,),
	simple.GL_PACK_SKIP_IMAGES                      : (1,),
	simple.GL_PACK_IMAGE_HEIGHT                     : (1,),
	simple.GL_ALIASED_POINT_SIZE_RANGE              : (2,),
	simple.GL_ALIASED_LINE_WIDTH_RANGE              : (2,),
	simple.GL_TEXTURE_3D                            : (1,),
	simple.GL_MAX_3D_TEXTURE_SIZE                   : (1,),
	simple.GL_COLOR_MATERIAL_PARAMETER              : (1,),
	simple.GL_NORMAL_ARRAY                          : (1,),
	simple.GL_COLOR_ARRAY                           : (1,),
	simple.GL_INDEX_ARRAY                           : (1,),
	simple.GL_TEXTURE_COORD_ARRAY                   : (1,),
	simple.GL_EDGE_FLAG_ARRAY                       : (1,),
	simple.GL_POINT_SIZE_RANGE                      : (2,),
	simple.GL_VERTEX_ARRAY_TYPE                     : (1,),
	simple.GL_CURRENT_INDEX                         : (1,),
	simple.GL_NORMAL_ARRAY_TYPE                     : (1,),
	simple.GL_NORMAL_ARRAY_STRIDE                   : (1,),
	simple.GL_COLOR_ARRAY_SIZE                      : (1,),
	simple.GL_COLOR_ARRAY_TYPE                      : (1,),
	simple.GL_COLOR_ARRAY_STRIDE                    : (1,),
	simple.GL_DRAW_BUFFER                           : (1,),
	simple.GL_INDEX_ARRAY_TYPE                      : (1,),
	simple.GL_INDEX_ARRAY_STRIDE                    : (1,),
	simple.GL_TEXTURE_COORD_ARRAY_SIZE              : (1,),
	simple.GL_TEXTURE_COORD_ARRAY_TYPE              : (1,),
	simple.GL_TEXTURE_COORD_ARRAY_STRIDE            : (1,),
	simple.GL_EDGE_FLAG_ARRAY_STRIDE                : (1,),
	simple.GL_UNPACK_SWAP_BYTES                     : (1,),
	simple.GL_UNPACK_SKIP_IMAGES                    : (1,),
	simple.GL_VERTEX_ARRAY_STRIDE                   : (1,),
	simple.GL_UNPACK_IMAGE_HEIGHT                   : (1,),
	simple.GL_POINT_SIZE_GRANULARITY                : (1,),
	simple.GL_LIGHT5                                : (1,),
	simple.GL_NAME_STACK_DEPTH                      : (1,),
	simple.GL_READ_BUFFER                           : (1,),
	simple.GL_PACK_ROW_LENGTH                       : (1,),
	simple.GL_PIXEL_MAP_I_TO_I_SIZE                 : (1,),
	simple.GL_COLOR_MATRIX                          : (4, 4),
	simple.GL_COLOR_MATRIX_STACK_DEPTH              : (1,),
	simple.GL_MAX_COLOR_MATRIX_STACK_DEPTH          : (1,),
	simple.GL_PIXEL_MAP_I_TO_B_SIZE                 : (1,),
	simple.GL_PIXEL_MAP_I_TO_A_SIZE                 : (1,),
	simple.GL_PIXEL_MAP_R_TO_R_SIZE                 : (1,),
	simple.GL_PIXEL_MAP_G_TO_G_SIZE                 : (1,),
	simple.GL_PIXEL_MAP_B_TO_B_SIZE                 : (1,),
	simple.GL_PIXEL_MAP_A_TO_A_SIZE                 : (1,),
	simple.GL_POST_COLOR_MATRIX_BLUE_BIAS           : (1,),
	simple.GL_POST_COLOR_MATRIX_ALPHA_BIAS          : (1,),
	simple.GL_PACK_LSB_FIRST                        : (1,),
	simple.GL_POST_CONVOLUTION_RED_BIAS             : (1,),
	simple.GL_LIGHT1                                : (1,),
	simple.GL_POST_CONVOLUTION_GREEN_BIAS           : (1,),
	simple.GL_PACK_SKIP_ROWS                        : (1,),
	simple.GL_POST_CONVOLUTION_BLUE_BIAS            : (1,),
	simple.GL_COLOR_TABLE                           : (1,),
	simple.GL_POST_CONVOLUTION_COLOR_TABLE          : (1,),
	simple.GL_POST_COLOR_MATRIX_COLOR_TABLE         : (1,),
	simple.GL_POST_CONVOLUTION_ALPHA_BIAS           : (1,),
	simple.GL_MAP1_GRID_DOMAIN                      : (2,),
	simple.GL_VERTEX_ARRAY_SIZE                     : (1,),
	simple.GL_ACTIVE_TEXTURE_ARB                    : (1,),
	simple.GL_CLIENT_ACTIVE_TEXTURE_ARB             : (1,),
	simple.GL_MAX_TEXTURE_UNITS_ARB                 : (1,),
	simple.GL_PACK_SKIP_PIXELS                      : (1,),
	simple.GL_MAX_ELEMENTS_VERTICES                 : (1,),
	simple.GL_MAX_ELEMENTS_INDICES                  : (1,),
	simple.GL_MAP2_COLOR_4                          : (1,),
	simple.GL_UNPACK_LSB_FIRST                      : (1,),
	simple.GL_UNPACK_ROW_LENGTH                     : (1,),
	simple.GL_UNPACK_SKIP_ROWS                      : (1,),
	simple.GL_UNPACK_SKIP_PIXELS                    : (1,),
	simple.GL_UNPACK_ALIGNMENT                      : (1,),
	simple.GL_SUBPIXEL_BITS                         : (1,),
	simple.GL_STENCIL_WRITEMASK                     : (1,),
	simple.GL_CURRENT_COLOR                         : (4,),
	simple.GL_AUTO_NORMAL                           : (1,),
	simple.GL_CURRENT_NORMAL                        : (3,),
	simple.GL_CURRENT_TEXTURE_COORDS                : (4,),
	simple.GL_CURRENT_RASTER_COLOR                  : (4,),
	simple.GL_CURRENT_RASTER_INDEX                  : (1,),
	simple.GL_CURRENT_RASTER_TEXTURE_COORDS         : (4,),
	simple.GL_CURRENT_RASTER_POSITION               : (4,),
	simple.GL_CURRENT_RASTER_POSITION_VALID         : (1,),
	simple.GL_CURRENT_RASTER_DISTANCE               : (1,),
	simple.GL_MAP_COLOR                             : (1,),
	simple.GL_MAP_STENCIL                           : (1,),
	simple.GL_INDEX_SHIFT                           : (1,),
	simple.GL_INDEX_OFFSET                          : (1,),
	simple.GL_RED_SCALE                             : (1,),
	simple.GL_RED_BIAS                              : (1,),
	simple.GL_ZOOM_X                                : (1,),
	simple.GL_ZOOM_Y                                : (1,),
	simple.GL_GREEN_SCALE                           : (1,),
	simple.GL_GREEN_BIAS                            : (1,),
	simple.GL_BLUE_SCALE                            : (1,),
	simple.GL_BLUE_BIAS                             : (1,),
	simple.GL_ALPHA_SCALE                           : (1,),
	simple.GL_ALPHA_BIAS                            : (1,),
	simple.GL_DEPTH_SCALE                           : (1,),
	simple.GL_DEPTH_BIAS                            : (1,),
	simple.GL_LINE_SMOOTH                           : (1,),
	simple.GL_LINE_WIDTH                            : (1,),
	simple.GL_LINE_WIDTH_RANGE                      : (2,),
	simple.GL_LINE_WIDTH_GRANULARITY                : (1,),
	simple.GL_LINE_STIPPLE                          : (1,),
	simple.GL_LINE_STIPPLE_PATTERN                  : (1,),
	simple.GL_LINE_STIPPLE_REPEAT                   : (1,),
	simple.GL_MAX_LIST_NESTING                      : (1,),
	simple.GL_PIXEL_MAP_S_TO_S_SIZE                 : (1,),
	simple.GL_MAX_CLIP_PLANES                       : (1,),
	simple.GL_LIST_MODE                             : (1,),
	simple.GL_MAX_LIGHTS                            : (1,),
	simple.GL_LIST_BASE                             : (1,),
	simple.GL_LIST_INDEX                            : (1,),
	simple.GL_MAX_PIXEL_MAP_TABLE                   : (1,),
	simple.GL_MAX_ATTRIB_STACK_DEPTH                : (1,),
	simple.GL_MAX_MODELVIEW_STACK_DEPTH             : (1,),
	simple.GL_MAX_NAME_STACK_DEPTH                  : (1,),
	simple.GL_MAX_PROJECTION_STACK_DEPTH            : (1,),
	simple.GL_MAX_TEXTURE_STACK_DEPTH               : (1,),
	simple.GL_MAX_VIEWPORT_DIMS                     : (2,),
	simple.GL_MAX_CLIENT_ATTRIB_STACK_DEPTH         : (1,),
	simple.GL_POLYGON_MODE                          : (2,),
	simple.GL_POLYGON_SMOOTH                        : (1,),
	simple.GL_POLYGON_STIPPLE                       : (1,),
	simple.GL_EDGE_FLAG                             : (1,),
	simple.GL_CULL_FACE                             : (1,),
	simple.GL_CULL_FACE_MODE                        : (1,),
	simple.GL_FRONT_FACE                            : (1,),
	simple.GL_TEXTURE_2D                            : (1,),
	simple.GL_POLYGON_OFFSET_POINT                  : (1,),
	simple.GL_LIGHTING                              : (1,),
	simple.GL_INDEX_BITS                            : (1,),
	simple.GL_LIGHT_MODEL_TWO_SIDE                  : (1,),
	simple.GL_GREEN_BITS                            : (1,),
	simple.GL_BLUE_BITS                             : (1,),
	simple.GL_ALPHA_BITS                            : (1,),
	simple.GL_DEPTH_BITS                            : (1,),
	simple.GL_COLOR_MATERIAL                        : (1,),
	simple.GL_ACCUM_RED_BITS                        : (1,),
	simple.GL_ACCUM_GREEN_BITS                      : (1,),
	simple.GL_ACCUM_BLUE_BITS                       : (1,),
	simple.GL_ACCUM_ALPHA_BITS                      : (1,),
	simple.GL_FOG                                   : (1,),
	simple.GL_FOG_INDEX                             : (1,),
	simple.GL_FOG_DENSITY                           : (1,),
	simple.GL_FOG_START                             : (1,),
	simple.GL_FOG_END                               : (1,),
	simple.GL_FOG_MODE                              : (1,),
	simple.GL_FOG_COLOR                             : (4,),
	simple.GL_STENCIL_CLEAR_VALUE                   : (1,),
	simple.GL_STENCIL_FUNC                          : (1,),
	simple.GL_DEPTH_RANGE                           : (2,),
	simple.GL_DEPTH_TEST                            : (1,),
	simple.GL_DEPTH_WRITEMASK                       : (1,),
	simple.GL_DEPTH_CLEAR_VALUE                     : (1,),
	simple.GL_DEPTH_FUNC                            : (1,),
	simple.GL_PACK_ALIGNMENT                        : (1,),
	simple.GL_STENCIL_PASS_DEPTH_FAIL               : (1,),
	simple.GL_ACCUM_CLEAR_VALUE                     : (4,),
	simple.GL_STENCIL_PASS_DEPTH_PASS               : (1,),
	simple.GL_STENCIL_REF                           : (1,),
	simple.GL_TEXTURE_1D                            : (1,),
	simple.GL_MAP1_COLOR_4                          : (1,),
	simple.GL_MAP1_INDEX                            : (1,),
	simple.GL_MAP1_NORMAL                           : (1,),
	simple.GL_MAP1_TEXTURE_COORD_1                  : (1,),
	simple.GL_MAP1_TEXTURE_COORD_2                  : (1,),
	simple.GL_MAP1_TEXTURE_COORD_3                  : (1,),
	simple.GL_MAP1_TEXTURE_COORD_4                  : (1,),
	simple.GL_MAP1_VERTEX_3                         : (1,),
	simple.GL_MAP1_VERTEX_4                         : (1,),
	simple.GL_POST_COLOR_MATRIX_RED_BIAS            : (1,),
	simple.GL_STENCIL_VALUE_MASK                    : (1,),
	simple.GL_POLYGON_OFFSET_UNITS                  : (1,),
	simple.GL_MATRIX_MODE                           : (1,),
	simple.GL_NORMALIZE                             : (1,),
	simple.GL_VIEWPORT                              : (4,),
	simple.GL_MODELVIEW_STACK_DEPTH                 : (1,),
	simple.GL_PROJECTION_STACK_DEPTH                : (1,),
	simple.GL_TEXTURE_STACK_DEPTH                   : (1,),
	simple.GL_MODELVIEW_MATRIX                      : (4, 4),
	simple.GL_INDEX_LOGIC_OP                        : (1,),
	simple.GL_POST_CONVOLUTION_ALPHA_SCALE          : (1,),
	simple.GL_FEEDBACK_BUFFER_TYPE                  : (1,),
	simple.GL_ATTRIB_STACK_DEPTH                    : (1,),
	simple.GL_CLIENT_ATTRIB_STACK_DEPTH             : (1,),
	simple.GL_MAP2_NORMAL                           : (1,),
	simple.GL_MAP2_TEXTURE_COORD_1                  : (1,),
	simple.GL_MAP2_TEXTURE_COORD_2                  : (1,),
	simple.GL_MAP2_TEXTURE_COORD_3                  : (1,),
	simple.GL_MAP2_TEXTURE_COORD_4                  : (1,),
	simple.GL_MAP2_VERTEX_3                         : (1,),
	simple.GL_MAP2_VERTEX_4                         : (1,),
	simple.GL_STENCIL_FAIL                          : (1,),
	simple.GL_ALPHA_TEST                            : (1,),
	simple.GL_ALPHA_TEST_FUNC                       : (1,),
	simple.GL_ALPHA_TEST_REF                        : (1,),
	simple.GL_DITHER                                : (1,),
	simple.GL_MAP1_GRID_SEGMENTS                    : (1,),
	simple.GL_MAP2_GRID_DOMAIN                      : (4,),
	simple.GL_MAP2_GRID_SEGMENTS                    : (2,),
	simple.GL_TEXTURE_BINDING_2D                    : (1,),
	simple.GL_TEXTURE_MATRIX                        : (4, 4),
	simple.GL_BLEND_DST                             : (1,),
	simple.GL_BLEND_SRC                             : (1,),
	simple.GL_BLEND                                 : (1,),
	simple.GL_POLYGON_OFFSET_LINE                   : (1,),
	simple.GL_LIGHT_MODEL_LOCAL_VIEWER              : (1,),
	simple.GL_STEREO                                : (1,),
	simple.GL_PROJECTION_MATRIX                     : (4, 4),
	simple.GL_RED_BITS                              : (1,),
	simple.GL_LOGIC_OP_MODE                         : (1,),
	simple.GL_FEEDBACK_BUFFER_SIZE                  : (1,),
	simple.GL_COLOR_LOGIC_OP                        : (1,),
	simple.GL_LIGHT_MODEL_AMBIENT                   : (4,),
	simple.GL_SELECTION_BUFFER_SIZE                 : (1,),
	simple.GL_LIGHT_MODEL_COLOR_CONTROL             : (1,),
	simple.GL_SHADE_MODEL                           : (1,),
	simple.GL_COLOR_MATERIAL_FACE                   : (1,),
}
def addGLGetConstant( constant, arraySize ):
	"""Add a glGet* constant to return an output array of correct size"""
	GL_GET_SIZES[ constant ] = arraySize
glGetDouble = glGetDoublev = wrapper.wrapper(simple.glGetDoublev).setOutput(
	"params",GL_GET_SIZES, "pname", 
)
glGetFloat = glGetFloatv = wrapper.wrapper(simple.glGetFloatv).setOutput(
	"params",GL_GET_SIZES, "pname", 
)
glGetBoolean = glGetBooleanv = glGetInteger = glGetIntegerv = wrapper.wrapper(simple.glGetIntegerv).setOutput(
	"params",GL_GET_SIZES, "pname", 
)

GL_GET_LIGHT_SIZES = {
	# glGetLightXv
	simple.GL_AMBIENT                               : (4,),
	simple.GL_DIFFUSE                               : (4,),
	simple.GL_SPECULAR                              : (4,),
	simple.GL_POSITION                              : (4,),
	simple.GL_SPOT_DIRECTION                        : (3,),
	simple.GL_SPOT_EXPONENT                         : (1,),
	simple.GL_SPOT_CUTOFF                           : (1,),
	simple.GL_CONSTANT_ATTENUATION                  : (1,),
	simple.GL_LINEAR_ATTENUATION                    : (1,),
	simple.GL_QUADRATIC_ATTENUATION                 : (1,),
} # end of sizes
glGetLightfv = wrapper.wrapper(simple.glGetLightfv).setOutput(
	"params",GL_GET_LIGHT_SIZES, "pname", 
)
glGetLightiv = wrapper.wrapper(simple.glGetLightiv).setOutput(
	"params",GL_GET_LIGHT_SIZES, "pname", 
)

GL_GET_MATERIAL_SIZES = {
	simple.GL_AMBIENT: (4,),
	simple.GL_DIFFUSE: (4,),
	simple.GL_SPECULAR: (4,),
	simple.GL_EMISSION: (4,),
	simple.GL_SHININESS: (1,),
	simple.GL_COLOR_INDEXES: (3,)
}
glGetMaterialfv = wrapper.wrapper(simple.glGetMaterialfv).setOutput(
	"params",GL_GET_MATERIAL_SIZES, "pname", 
)
glGetMaterialiv = wrapper.wrapper(simple.glGetMaterialiv).setOutput(
	"params",GL_GET_MATERIAL_SIZES, "pname", 
)
PIXEL_MAP_SIZE_CONSTANT_MAP = {
	simple.GL_PIXEL_MAP_A_TO_A: simple.GL_PIXEL_MAP_A_TO_A_SIZE,
	simple.GL_PIXEL_MAP_B_TO_B: simple.GL_PIXEL_MAP_B_TO_B_SIZE,
	simple.GL_PIXEL_MAP_G_TO_G: simple.GL_PIXEL_MAP_G_TO_G_SIZE,
	simple.GL_PIXEL_MAP_I_TO_A: simple.GL_PIXEL_MAP_I_TO_A_SIZE,
	simple.GL_PIXEL_MAP_I_TO_B: simple.GL_PIXEL_MAP_I_TO_B_SIZE,
	simple.GL_PIXEL_MAP_I_TO_G: simple.GL_PIXEL_MAP_I_TO_G_SIZE,
	simple.GL_PIXEL_MAP_I_TO_I: simple.GL_PIXEL_MAP_I_TO_I_SIZE,
	simple.GL_PIXEL_MAP_I_TO_R: simple.GL_PIXEL_MAP_I_TO_R_SIZE,
	simple.GL_PIXEL_MAP_R_TO_R: simple.GL_PIXEL_MAP_R_TO_R_SIZE,
	simple.GL_PIXEL_MAP_S_TO_S: simple.GL_PIXEL_MAP_S_TO_S_SIZE,
}
def GL_GET_PIXEL_MAP_SIZE( pname ):
	"""Given a pname, lookup the size using a glGet query..."""
	constant = PIXEL_MAP_SIZE_CONSTANT_MAP[ pname ]
	return glGetIntegerv( constant )
glGetPixelMapfv = wrapper.wrapper(simple.glGetPixelMapfv).setOutput(
	"values",GL_GET_PIXEL_MAP_SIZE, "map", 
)
glGetPixelMapuiv = wrapper.wrapper(simple.glGetPixelMapuiv).setOutput(
	"values",GL_GET_PIXEL_MAP_SIZE, "map", 
)
glGetPixelMapusv = wrapper.wrapper(simple.glGetPixelMapusv).setOutput(
	"values",GL_GET_PIXEL_MAP_SIZE, "map", 
)

# 32 * 32 bits
POLYGON_STIPPLE_SIZE = (32*32/8,)
glGetPolygonStipple = glGetPolygonStippleub = wrapper.wrapper(simple.glGetPolygonStipple).setOutput(
	"mask",POLYGON_STIPPLE_SIZE, 
)
GL_GET_TEX_ENV_SIZES = {
	simple.GL_TEXTURE_ENV_MODE: (1,),
	simple.GL_TEXTURE_ENV_COLOR: (4,),
}
glGetTexEnvfv = wrapper.wrapper(simple.glGetTexEnvfv).setOutput(
	"params",GL_GET_TEX_ENV_SIZES, 'pname',  
)
glGetTexEnviv = wrapper.wrapper(simple.glGetTexEnviv).setOutput(
	"params",GL_GET_TEX_ENV_SIZES, 'pname',  
)
GL_GET_TEX_GEN_SIZES = {
	simple.GL_TEXTURE_GEN_MODE: (1,),
	simple.GL_OBJECT_PLANE: (4,),
	simple.GL_EYE_PLANE: (4,),
}
glGetTexGendv = wrapper.wrapper(simple.glGetTexGendv).setOutput(
	"params",GL_GET_TEX_GEN_SIZES, 'pname',  
)
glGetTexGenfv = wrapper.wrapper(simple.glGetTexGenfv).setOutput(
	"params",GL_GET_TEX_GEN_SIZES, 'pname',  
)
glGetTexGeniv = wrapper.wrapper(simple.glGetTexGeniv).setOutput(
	"params",GL_GET_TEX_GEN_SIZES, 'pname',  
)

glGetTexLevelParameterfv = wrapper.wrapper(simple.glGetTexLevelParameterfv).setOutput(
	"params",(1,)
)
glGetTexLevelParameteriv = wrapper.wrapper(simple.glGetTexLevelParameteriv).setOutput(
	"params",(1,)
)
TEX_PARAMETER_SIZES = {
	simple.GL_TEXTURE_MAG_FILTER: (1,),
	simple.GL_TEXTURE_MIN_FILTER: (1,), 
	simple.GL_TEXTURE_MIN_LOD: (1,),
	simple.GL_TEXTURE_MAX_LOD: (1,),
	simple.GL_TEXTURE_BASE_LEVEL: (1,),
	simple.GL_TEXTURE_MAX_LEVEL: (1,),
	simple.GL_TEXTURE_WRAP_S: (1,),
	simple.GL_TEXTURE_WRAP_T: (1,),
	simple.GL_TEXTURE_WRAP_R: (1,),
	simple.GL_TEXTURE_BORDER_COLOR: (4,), 
	simple.GL_TEXTURE_PRIORITY: (1,),
	simple.GL_TEXTURE_RESIDENT: (1,)
}

glGetTexParameterfv = wrapper.wrapper(simple.glGetTexParameterfv).setOutput(
	"params",TEX_PARAMETER_SIZES, 'pname',
)
glGetTexParameteriv = wrapper.wrapper(simple.glGetTexParameteriv).setOutput(
	"params",TEX_PARAMETER_SIZES, 'pname',
)

