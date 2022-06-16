import model_loader, texture_loader, shader_loader
import model

import json

def load_json(filename):
	json_file = open(filename, 'r')
	json_raw = json.load(json_file)

	models_out = []
	for obj in json_raw:
		models_out.append(model.model(json_raw[obj]["model"], 
					      json_raw[obj]["shaders"]["vert_shader"],
					      json_raw[obj]["shaders"]["frag_shader"],
					      json_raw[obj]["textures"],
					      json_raw[obj]["offset"]))

	return models_out
