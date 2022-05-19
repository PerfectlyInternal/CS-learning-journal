from OpenGL.GL import *
import glfw

def init():
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
	
        return window
