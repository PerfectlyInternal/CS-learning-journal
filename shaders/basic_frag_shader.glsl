#version 330 core

// interpolated values from vertex shader
in vec3 fragColor;
in vec2 fragUV;

// color to draw on screen
out vec4 color;

// the texture sampler
//uniform sampler2D texture0;

void main() {
	// this is how textures are sampled
	color = vec4(fragUV.xy, fragColor.b, 1);
}

