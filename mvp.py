from OpenGL.GL import *
import glm
import gl_debugging as debug

# calculate the MVP matrix for a specific position
def calcMVP(width, height):
	projection = glm.perspective(glm.radians(45.0),float(width)/float(height),0.1,1000.0)
	view = glm.lookAt(glm.vec3(5,5,5), # Camera is at (4,3,-3), in World Space
						glm.vec3(0,0,0), #and looks at the (0.0.0))
						glm.vec3(0,1,0) ) #Head is up (set to 0,-1,0 to look upside-down)
	model = glm.mat4(1.0)

	return projection * view * model

# gets the MVP uniform id for the given shader program
def initMVP(shader):
	mvpID = glGetUniformLocation(shader, "MVP")
	debug.check_gl_error()
	return mvpID

# claculates and loads the MVP matrix into VRAM where it can be used for rendering
# must be run *every frame* or the camera won't move
def setMVP(mvpID, w, h):
	if(mvpID == None):
		return
	glUniformMatrix4fv(
			mvpID, 		# where to load matrix
			1, 		# number of matricies to load
			GL_FALSE, 	# dont transpose
			glm.value_ptr(calcMVP(w, h))) # pointer to matrix object
