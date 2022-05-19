#version 330 core

// interpolated values from vertex shader
in vec2 fragUV;

// color to draw on screen
out vec3 color;

// the texture sampler
uniform sampler2D texture0;

void main() {
	// this is how textures are sampled
	color = vec3(fragUV, 0); //texture(texture0, fragUV).rgb;
}
