#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include <GL/glut.h>
#include <GL/gl.h>
#include <GL/glu.h>

typedef struct { unsigned char r, g, b; } rgb;

void set_texture();
void render();

rgb** texture = 0;
int width, height;

// OpenGl секция

int gwin;
GLuint gltexture;
int tex_w, tex_h;

void allocate_texture()
{
	int i, ow = tex_w, oh = tex_h;

	for (tex_w = 1; tex_w < width; tex_w <<= 1);
	for (tex_h = 1; tex_h < height; tex_h <<= 1);

	if (tex_h != oh || tex_w != ow)
		texture = realloc(texture, tex_h * tex_w * 3 + tex_h * sizeof(rgb*));
	
	for (texture[0] = (rgb*)(texture + tex_h), i = 1; i < tex_h; i++)
		texture[i] = texture[i - 1] + tex_w;
}


void set_texture()
{
	allocate_texture();	
	//mandelbrot();
	
	glEnable(GL_TEXTURE_2D);
	glBindTexture(GL_TEXTURE_2D, gltexture);
	glTexImage2D(GL_TEXTURE_2D, 0, 3, tex_w, tex_h, 0, GL_RGB, GL_UNSIGNED_BYTE, texture[0]);

	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
	render();
}

void resize(int w, int h)
{	
	width = w;
	height = h;

	glViewport(0, 0, w, h);
	glOrtho(0, w, 0, h, -1, 1);

	set_texture();
}

void init_gfx(int* c, char** v)
{
	glutInit(c, v);
	glutInitDisplayMode(GLUT_RGB);
	glutInitWindowSize(600, 600);

	gwin = glutCreateWindow("Mandelbrot");
	glutDisplayFunc(render);

	glutReshapeFunc(resize);
	glGenTextures(1, &gltexture);
	set_texture();
}

void render()
{
	double x = (double)width / tex_w;
	double y = (double)height / tex_h;

	glClear(GL_COLOR_BUFFER_BIT);
	glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE);

	glBindTexture(GL_TEXTURE_2D, gltexture);

	glBegin(GL_QUADS);


	glTexCoord2f(0, 0); glVertex2i(0, 0);
	glTexCoord2f(x, 0); glVertex2i(width, 0);
	glTexCoord2f(x, y); glVertex2i(width/2, height);	
	glTexCoord2f(0, y); glVertex2i(width/2, height);
	
	glEnd();
	glFlush();
	glFinish();
}

int main(int c, char** v)
{
	init_gfx(&c, v);
	glClearColor(0.3 ,0.2 ,1 , 0.5); 
    glShadeModel(GLU_FLAT);
	glutMainLoop();
	
	return 0;
}

