#version 330 core

// interpolated values from vertex shader
in vec2 fragUV;

// color to draw on screen
out vec4 color;

// the texture sampler
uniform sampler2D texture0;
uniform sampler2D texture1;

void main() {
	// blends the two textures together
	vec4 color0 = texture(texture0, fragUV);
	vec4 color1 = texture(texture1, fragUV);
	color = mix(color0, color1, 0.5);
}
