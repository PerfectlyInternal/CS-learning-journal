#version 330 core

// vertex position in the world and vertex UV coords as inputs
layout(location = 0) in vec3 vertPosModelSpace;
layout(location = 1) in vec2 vertUV;

// output is fragment UV coords, interpolated between vertices for each fragment
// UV coords are basically X and Y coords on a texture
// U and V go from 0 to 1, where (0, 0) is the bottom left corner and (1, 1) is the upper left corner 
out vec2 fragUV;

// distance to camera for fog
out float distToCamera;

// transform matrix to turn world position into camera position
uniform mat4 MVP;

void main() {
	// calculate the position of the vertex
	// gl_Position is used by OpenGL and must be set by the vertex shader
	gl_Position = MVP * vec4(vertPosModelSpace,1);
	
	// vert uvs and colors dont change
	fragUV = vertUV;
	
	// distance to camera (for fog shaders)
    	distToCamera = gl_Position.w;
}
