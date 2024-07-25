import pygame 
from pygame.locals import * 
from gl import Renderer
from shaders import vertexShader
from model import Model

width = 960
height = 540

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

rend = Renderer(screen)
rend.vertexShader = vertexShader

model1= Model("Porsche_911_GT2.obj")
model1.translate[0] = width / 2
model1.translate[1] = height / 4

model1.scale[0] = 10
model1.scale[1] = 10
model1.scale[2] = 10

rend.models.append(model1)


isRunning = True
while isRunning:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
    
    rend.glClear()
    
    rend.glRender()
    
    pygame.display.flip()
    clock.tick(60)
    
rend.glGenerateFrameBuffer("output.bmp")

pygame.quit()

                
         