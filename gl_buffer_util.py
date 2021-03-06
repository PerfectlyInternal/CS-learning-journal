from OpenGL.GL import *
import gl_debugging as debug

# load data into a gl buffer
# simplifies things because this is a mess
def load_data_into_buffer(buf, data):
	glBindBuffer(GL_ARRAY_BUFFER, buf)
	glBufferData(GL_ARRAY_BUFFER, len(data)*4, (GLfloat * len(data))(*data), GL_STATIC_DRAW)
	debug.check_gl_error()

# utility function to create a GL buffer filled with data
def create_buffer_with_data(data):
	buf = glGenBuffers(1)
	load_data_into_buffer(buf, data)
	return buf

# automates setting a buffer as a vertex attribute
def set_buffer_as_vertex_attrib(index, buf, vsize):
	glEnableVertexAttribArray(index)
	glBindBuffer(GL_ARRAY_BUFFER, buf)
	glVertexAttribPointer(
			index,	  # which attribute index to use
			vsize, 	  # size of vector per vertex
			GL_FLOAT, # type of data
			GL_FALSE, # dont normalize
			0, 	  # all data is tightly packed
			None)	  # offset to start of data in buffer
	debug.check_gl_error()
