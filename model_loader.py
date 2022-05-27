# loads .obj files, 
def load_model(model_path):
	# open the model file for reading as text
	model = open(model_path, 'r')

	# empty arrays to later hold model data
	# data for each individual vertex, each one is its own array of 2 or 3 elements
	raw_verts = []
	raw_uvs = []

	# data for each face, each one is a tuple of 3 elements, one for each vertex of the face
	# each vertex of the face has the indices for position, normals and uv in that order
	faces = []

	# go through every line in the obj file and store the data
	for line in model:
		data = line.split()

		# data is vertex position
		if(data[0] == 'v'):
			v = map(float, data[1:4])
			raw_verts.append(list(v))

		# data is a vertex UV
		elif(data[0] == 'vt'):
			vt = map(float, data[1:3])
			raw_uvs.append(list(vt))
	
		# data is a vertex normal (doesnt matter for now)
		elif(data[0] == 'vn'):
			pass
		# data is a face
		elif(data[0] == 'f'):
			faces.append((list(map(int, data[1].split('/'))),
				      list(map(int, data[2].split('/'))),
				      list(map(int, data[3].split('/')))))
		# data doesnt matter or is corrupted
		else:
			print("line skipped:", line)

	# combine all the indices for position and uvs into full arrays
	verts = []
	uvs = []
	for face in faces:
		for vert in face:
			pos_index = vert[0] - 1
			uv_index = vert[1] - 1
			pos = raw_verts[pos_index]
			uv = raw_uvs[uv_index]
			verts += pos # we need to concatenate the arrays for OpenGL to later understand it properly
			uvs += uv
	
	return verts, uvs
