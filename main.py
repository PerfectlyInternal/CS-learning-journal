# opengl imports
from OpenGL.GL import *
from OpenGL.GLU import *
import glfw
import glm
print("OpenGL and supporting libraries imported successfully!")

# utility imports
import glfw_init
import verts
import gl_buffer_util as gl_buf
import shader_loader
import mvp
import model
import gl_debugging as debug
print("utility libraries imported successfully!")

# other imports

print("All imports successful!")

def main():
	# initialize glfw
	window = glfw_init.init()

	# configure some OpenGL	global settings
	glClearColor(0, 0.5, 0.5, 0) # when screen is cleared, make it black
	glDepthFunc(GL_LESS) 	 # closer things are those with less distance from camera 
	#glEnable(GL_DEPTH_TEST)  # closer things should obscure farther things
	#glEnable(GL_CULL_FACE)	 # faces pointing away from the camera can be skipped

	# vertex array object
	# this is how OpenGL keeps track of groups of vertices and their attributes
	vao = glGenVertexArrays(1)
	glBindVertexArray(vao)
	
	cube = model.model(None, 'shaders/basic_vert_shader.glsl', 'shaders/basic_frag_shader.glsl', ['textures/cube.png'])

	# while the esc key isnt pressed *and* the window shouldnt close
	while(not (glfw.get_key(window, glfw.KEY_ESCAPE) or glfw.window_should_close(window))):
		# clear the screen
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		
		cube.draw()
	
		# draw all the new stuff to the screen
		glfw.swap_buffers(window)

		# update input events
		glfw.poll_events()
	glfw.terminate()

main()
