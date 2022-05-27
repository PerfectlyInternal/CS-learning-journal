# my utils
import glfw_init
import texture_loader
import model

# OpenGL libs
from OpenGL.GL import *
import glfw

window = glfw_init.init() # create a window, no OpenGL calls
vao = glGenVertexArrays(1) # vao stuff
glBindVertexArray(vao)
# model only loads verts and shaders, no textures
model = model.model(None, 'shaders/basic_vert_shader.glsl', 'shaders/basic_frag_shader.glsl', ['textures/cube.bmp'])
glClearColor(1, 1, 1, 1)
# main loop
while(not (glfw.get_key(window, glfw.KEY_ESCAPE) or glfw.window_should_close(window))):
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	# draw the model with the verts and shaders, textures dont exist in there
	model.draw()
	glfw.swap_buffers(window)
	glfw.poll_events()
