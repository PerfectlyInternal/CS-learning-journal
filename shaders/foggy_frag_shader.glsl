#version 330 core

// interpolated values from vertex shader
in vec2 fragUV;
in float distToCamera;

// color to draw on screen
out vec4 color;

// the texture sampler
uniform sampler2D texture0;

void main() {
	// the base color of the fragment, before fog
	vec4 baseColor = texture(texture0, fragUV);
	
	// fog constants
	float maxFog = 5.5;
	float minFog = 2.5;
	vec4 fogColor = vec4(0.5, 0.5, 0.5, 1);
	
	// apply fog
	float fogAmount = clamp((distToCamera - minFog)/(maxFog-minFog), 0.0, 1.0);
	color = mix(baseColor, fogColor, fogAmount);
}
