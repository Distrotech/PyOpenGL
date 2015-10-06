"""Transliteration of https://open.gl/feedback into Python"""
from __future__ import print_function
import pygamegltest
from OpenGL._bytes import as_8_bit
from OpenGL.GL import *
from OpenGL.GL import shaders
vertex_shader = """#version 150 core
    in float inValue;
    out float geoValue;

    void main() {
        geoValue = sqrt(inValue);
    }
"""

geometry_shader = """#version 150 core
    layout(points) in;
    layout(triangle_strip, max_vertices = 3) out;

    in float[] geoValue;
    out float outValue;

    void main() {
        for (int i = 0; i < 3; i++) {
            outValue = geoValue[0] + i;
            EmitVertex();
        }

        EndPrimitive();
    }
"""

@pygamegltest.pygametest(name="Geometry Shader Test")
def main():
    program = shaders.compileProgram(
        shaders.compileShader([vertex_shader], GL_VERTEX_SHADER), 
        shaders.compileShader([geometry_shader], GL_GEOMETRY_SHADER)
    )
    
    # test that we can describe the attributes in the shader
    for i in range( glGetProgramiv( program, GL_ACTIVE_ATTRIBUTES )):
        result = glGetActiveAttrib( program, i )
        name,size,type = result
        print( 'Arribute %s(%i) -> %s %s'%(name,i,size,type))

    buff = (ctypes.c_char_p * 1)( as_8_bit("outValue\000") )
    c_text = ctypes.cast(ctypes.pointer(buff), ctypes.POINTER(ctypes.POINTER(GLchar)))
    # modifies the state in the linking of the program
    glTransformFeedbackVaryings(program, 1, c_text, GL_INTERLEAVED_ATTRIBS);
    # so have to re-link
    glLinkProgram(program)
    

    glUseProgram(program);

    vao = glGenVertexArrays(1);
    glBindVertexArray(vao);

    data = (GLfloat * 5)(1.0, 2.0, 3.0, 4.0, 5.0)
    
    vbo = glGenBuffers(1);
    glBindBuffer(GL_ARRAY_BUFFER, vbo);
    glBufferData(GL_ARRAY_BUFFER, ctypes.sizeof(data), data, GL_STATIC_DRAW);

    inputAttrib = glGetAttribLocation(program, "inValue");
    glEnableVertexAttribArray(inputAttrib);
    glVertexAttribPointer(inputAttrib, 1, GL_FLOAT, GL_FALSE, 0, 0);

    tbo = glGenBuffers(1);
    glBindBuffer(GL_ARRAY_BUFFER, tbo);
    glBufferData(GL_ARRAY_BUFFER, ctypes.sizeof(data) * 3, None, GL_STATIC_READ);

    glEnable(GL_RASTERIZER_DISCARD);

    glBindBufferBase(GL_TRANSFORM_FEEDBACK_BUFFER, 0, tbo);

    glBeginTransformFeedback(GL_TRIANGLES);
    glDrawArrays(GL_POINTS, 0, 5);
    glEndTransformFeedback();

    glDisable(GL_RASTERIZER_DISCARD);

    glFlush();

    feedback = (GLfloat*15)(*([0]*15))
    glGetBufferSubData(GL_TRANSFORM_FEEDBACK_BUFFER, 0, ctypes.sizeof(feedback), feedback);

    for value in feedback:
        print(value)

if __name__ == "__main__":
    main()
