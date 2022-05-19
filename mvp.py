from OpenGL.GL import *
import glm
import gl_debugging as debug

# calculate the MVP matrix for a specific position
def calcMVP(width, height):
	projection = glm.perspective(glm.radians(45.0),float(width)/float(height),0.1,1000.0)
	view = glm.lookAt(glm.vec3(4,3,-3), # Camera is at (4,3,-3), in World Space
						glm.vec3(0,0,0), #and looks at the (0.0.0))
						glm.vec3(0,1,0) ) #Head is up (set to 0,-1,0 to look upside-down)
	model = glm.mat4(1.0)

	return projection * view * model

# sets mvpID to the shader's MVP input
# must be run every time a new shader is used
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
			mvpID, 		# matrix to load
			1, 		# number to load
			GL_FALSE, 	# dont transpose
			glm.value_ptr(calcMVP(w, h)))
