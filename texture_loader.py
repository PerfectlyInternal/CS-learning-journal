from OpenGL.GL import *
import gl_debugging as debug
#from PIL import Image
from bitmap import Image

# loads a texture from an image file into VRAM
def load_texture(texture_path):
	# this section was deprecated due to Pillow breaking OpenGL
	"""
	# open the image file and convert to necessary formats	
	print("loading image", texture_path)
	image = Image.open(texture_path)
	convert = image.convert("RGBA")
	image_data = image.transpose(Image.FLIP_TOP_BOTTOM ).tobytes()
	w = image.width
	h = image.height
	image.close()
	"""
	# convert binary data from bmp file into pixel data and metadata
	image = Image(open(texture_path, 'rb').read())	
	image_data = image.getRawPixelData()

	# get image dimensions, we need these later to allocate memory
	w = image.getBitmapWidth()
	h = image.getBitmapHeight()

	# create the texture in VRAM
	texture = glGenTextures(1)
	glBindTexture(GL_TEXTURE_2D, texture)
	
	# configure some texture settings
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT) # when you try to reference points beyond the edge of the texture, how should it behave?
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT) # in this case, repeat the texture data
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR) # when you zoom in, how should the new pixels be calculated?
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR) # when you zoom out, how should the existing pixels be combined?
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_BASE_LEVEL, 0);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAX_LEVEL, 0);

	# load texture onto the GPU
	glTexImage2D(
		GL_TEXTURE_2D, 	  # where to load texture data
		0, 	 	  # mipmap level
		GL_RGB8, 	  # format to store data in
		w, 		  # image dimensions
		h,	 	  #
		0, 		  # border thickness
		GL_RGB, 	  # format data is provided in
		GL_UNSIGNED_BYTE, # type to read data as
		image_data)	  # data to load as texture
	debug.check_gl_error()
	
	# generate smaller versions of the texture to save time when its zoomed out
	glGenerateMipmap(GL_TEXTURE_2D) 

	# clean up afterwards
	glBindTexture(GL_TEXTURE_2D, 0)

	return texture
