# my utils
import glfw_init
import texture_loader
import model

# OpenGL libs
from OpenGL.GL import *
import glfw

from PIL import Image

window = glfw_init.init() # create a window, no OpenGL calls
vao = glGenVertexArrays(1) # vao stuff
glBindVertexArray(vao)
# model only loads verts and shaders, no textures
model = model.model(None, 'shaders/basic_vert_shader.glsl', 'shaders/basic_frag_shader.glsl', [])
# this is where the problem is, commenting this out magically makes everything work
# the teture is never used, only loaded
#texture = texture_loader.load_texture('textures/cube.png')
img = Image.open('textures/cube.png')
glClearColor(1, 1, 1, 1)
# main loop
while(not (glfw.get_key(window, glfw.KEY_ESCAPE) or glfw.window_should_close(window))):
	glClear(GL_COLOR_BUFFER_BIT)
	# draw the model with the verts and shaders, textures dont exist in there
	model.draw()
	glfw.swap_buffers(window)
	glfw.poll_events()
