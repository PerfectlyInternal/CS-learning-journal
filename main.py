# opengl imports
from OpenGL.GL import *
from OpenGL.GLU import *
import glfw
print("OpenGL and GLFW imported successfully!")

# other imports

print("All imports successful!")

def main():
	# init glfw, exit if fails
	if(not glfw.init()):
		print("GLFW initialization failed!")
		return

	# window settings ("hints")
	glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3) # minimum OpenGL version is 3.3
	glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
	glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE) # we need these features of OpenGL
	glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE) # no legacy features (OpenGL 1 and 2)
	# create a window with GLFW
	window = glfw.create_window(
				640, # width
				480, # height
				"hey i made a window", # title
				None, # monitor to use (None means default)
				None) # share buffers with another context? (No other context to share with)
	if(not window):
		print("Window creation failed!")
		return
	glfw.make_context_current(window) # render things to the window

	# configure some OpenGL	global settings
	glClearColor(0, 0, 0, 0) # when screen is cleared, make it black
	glDepthFunc(GL_LESS) 	 # closer things are those with less distance from camera 
	glEnable(GL_DEPTH_TEST)  # closer things should obscure farther things
	glEnable(GL_CULL_FACE)	 # faces pointing away from the camera can be skipped

	# while the esc key isnt pressed *and* the window shouldnt close
	while(not (glfw.get_key(window, glfw.KEY_ESCAPE) or glfw.window_should_close(window))):
		# clear the screen
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		
		# draw all the new stuff to the screen
		glfw.swap_buffers(window)

		# update input events
		glfw.poll_events()
	glfw.terminate()

main()
