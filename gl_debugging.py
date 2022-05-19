from OpenGL.GL import *

# debug method to handle OpenGL errors
# OpenGL rarely crashes, most errors just raise flags
# this checks if an error flag is raised and if it is, prints out the error
# returns wether or not there was an error
def check_gl_error():
	error = glGetError()
	if(error != GL_NO_ERROR):
		print(error)
		return True
	return False
