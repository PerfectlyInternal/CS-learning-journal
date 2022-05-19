from OpenGL.GL import *

from PIL import Image

# loads a texture from an image file into VRAM
def load_texture(texture_path):
	# open the image file and convert to necessary formats
	print("loading image", texture_path)
	image = Image.open(texture_path).convert("RGB")
	image_data = image.transpose(Image.FLIP_TOP_BOTTOM).tobytes()
	image.close()
	
	# create the texture and load data into VRAM
	texture = glGenTextures(1)
	glBindTexture(GL_TEXTURE_2D, texture)
	glTexImage2D(
		GL_TEXTURE_2D, 	  # where to load texture data
		0, 	 	  # mipmap level
		GL_RGB, 	  # format to store data in
		image.width, 	  # image dimensions
		image.height, 	  #
		0, 		  # border thickness
		GL_RGB, 	  # format data is provided in
		GL_UNSIGNED_BYTE, # type to read data as
		image_data)	  # data to load as texture
	
	# configure some texture settings
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT) # when you try to reference points beyond the edge of the texture, how should it behave?
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT) # in this case, repeat the texture data
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR) # when you zoom in, how should the new pixels be calculated?
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR) # when you zoom out, how should the existing pixels be combined?
	glGenerateMipmap(GL_TEXTURE_2D) # generate smaller versions of the texture to save time when its zoomed out

	return texture
