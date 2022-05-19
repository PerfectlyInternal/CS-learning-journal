from OpenGL.GL import *
import gl_debugging as debug

# generates a shader program from a vertex and fragment shader
# vertex shaders calculate the position of each vertex on the screen + other attributes that are interpolated and passed on to fragments
# fragment shaders calculate the color of each pixel on the screen using the data from the vertex shader
def load_shader(vert_shader_path, frag_shader_path):
	# read vertex shader data in binary format
	vert_shader_file = open(vert_shader_path, 'rb')
	vert_shader_data = vert_shader_file.read()
	vert_shader_file.close()

	# read fragment shader data in binary format
	frag_shader_file = open(frag_shader_path, 'rb')
	frag_shader_data = frag_shader_file.read()
	frag_shader_file.close()

	# create shader program
	# this is what is then passed to the rendering pipeline
	program = glCreateProgram()

	# create and compile vertex shader
	vert_shader = glCreateShader(GL_VERTEX_SHADER)
	glShaderSource(vert_shader, vert_shader_data)
	glCompileShader(vert_shader)
	glAttachShader(program, vert_shader)

	# create and compile fragment shader
	frag_shader = glCreateShader(GL_FRAGMENT_SHADER)
	glShaderSource(frag_shader, frag_shader_data)
	glCompileShader(frag_shader)
	glAttachShader(program, frag_shader)

	# link shaders into full program
	glLinkProgram(program)
	debug.check_gl_error()
	return program
