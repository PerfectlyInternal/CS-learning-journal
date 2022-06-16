# my utils
import glfw_init
import json_loader

# OpenGL libs
from OpenGL.GL import *
import glfw

window = glfw_init.init() # create a window, no OpenGL calls
vao = glGenVertexArrays(1) # vao stuff
glBindVertexArray(vao)

glClearColor(0.5, 0.5, 0.5, 1)

models = json_loader.load_json("json/fog.json")

# main loop
while(not (glfw.get_key(window, glfw.KEY_ESCAPE) or glfw.window_should_close(window))):
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	# draw the model with the verts and shaders, textures dont exist in there

	for model in models:
		model.draw()

	glfw.swap_buffers(window)
	glfw.poll_events()
