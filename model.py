from OpenGL.GL import *

import shader_loader
import texture_loader
import model_loader
import gl_buffer_util as gl_buf
import gl_debugging as debug
import mvp
import verts

# wrapper class to handle separate models with different textures, shaders, etc.
# handles all file loading within itself
# loads a separate shader program for each model, this may be changed later to simplify things
# shader program only exists within the instance, so setting uniforms has to happen in here
# provides the method to draw itself as well
class model:
	def __init__(self, model_path=None, vert_shader_path=None, frag_shader_path=None, texture_paths=[], offset=[0,0,0]):
		# check if we should use default cube model
		if(model_path == None):
			self.verts = verts.verts
			self.colors = verts.colors
			self.uv = verts.uv
			self.vert_buf = gl_buf.create_buffer_with_data(self.verts)
			self.color_buf = gl_buf.create_buffer_with_data(self.colors)
			self.uv_buf = gl_buf.create_buffer_with_data(self.uv)
		else:
			self.load_model(model_path, offset)

		# no default shaders, yet
		if(vert_shader_path != None and frag_shader_path != None):
			self.load_shaders(vert_shader_path, frag_shader_path)
			self.mvpID = mvp.initMVP(self.shader)

		# no default textures, yet
		self.textures = []
		for path in texture_paths:
			self.textures.append(texture_loader.load_texture(path))

		if(len(self.textures) > GL_MAX_TEXTURE_UNITS):
			print("Warning: too many textures loaded, OpenGL may not behave correctly")
		
		# get IDs for texture inputs and set which texture slot should be used for them in the shader program
		glUseProgram(self.shader)
		for i in range(len(self.textures)):
			uniformID = glGetUniformLocation(self.shader, "texture" + str(i))
			if(uniformID >= 0):
				glUniform1i(uniformID, i)
			print(uniformID, i)
	
	def load_shaders(self, vert_shader_path, frag_shader_path):
		self.shader = shader_loader.load_shader(vert_shader_path, frag_shader_path)

	def load_model(self, model_path, offset):
		self.verts, self.uv = model_loader.load_model(model_path, offset)
		self.vert_buf = gl_buf.create_buffer_with_data(self.verts)
		self.uv_buf = gl_buf.create_buffer_with_data(self.uv)

	def draw(self):
		glUseProgram(self.shader)

		# set the camera to be 640x480p and some other stuff
		mvp.setMVP(self.mvpID, 640, 480)

		# tell OpenGL to use vertex data
		gl_buf.set_buffer_as_vertex_attrib(0, self.vert_buf, 3)
		gl_buf.set_buffer_as_vertex_attrib(1, self.uv_buf, 2)

		# pass textures to shaders
		for i in range(len(self.textures)):
			glActiveTexture(GL_TEXTURE0 + i)
			glBindTexture(GL_TEXTURE_2D, self.textures[i])
			debug.check_gl_error()

		glDrawArrays(GL_TRIANGLES, 0, int(len(self.verts)/3))
		glDrawArrays(GL_POINTS, 0, len(self.verts))
		debug.check_gl_error()

		# disable the attribute arrays after rendering
		glDisableVertexAttribArray(0)
		glDisableVertexAttribArray(1)
