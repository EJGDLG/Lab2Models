import pygame
from pygame.locals import *
from GL import *
from model import Model
from shaders import VertexShader

width = 960
height = 540


screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock() 

#Cargar modelo
modelo1 = Model("Porsche_911_GT2.obj")

modelo1.translate[2] = -30
modelo1.scale[0] = 5
modelo1.scale[1] = 5
modelo1.scale[2] = 5

rend = Renderer(screen)
rend.vertexShader = VertexShader 

rend.glColor(0, 0, 1)  
rend.glClearColor(0, 0, 0)  


rend.models.append(modelo1)
isRunning = True
while isRunning:
    
    for event in pygame.event.get():
     
        if event.type == pygame.QUIT:
            isRunning = False
       
        elif event.type == pygame.KEYDOWN:
           
            if event.key == pygame.K_ESCAPE:
                isRunning = False

            elif event.key == pygame.K_RIGHT:
                rend.camera.translate[0] -= 1
            elif event.key == pygame.K_LEFT:
                rend.camera.translate[0] += 1 
            elif event.key == pygame.K_UP:
                modelo1.rotate[0] += 10
            elif event.key == pygame.K_DOWN:
                modelo1.rotate[0] -= 10
            elif event.key  == pygame.K_k:                
                modelo1.scale[0] += 2
                modelo1.scale[1] += 2
                modelo1.scale[2] += 2
            elif event.key == pygame.K_w:
                modelo1.translate[1] += 5
            elif event.key == pygame.K_a:
                modelo1.translate[0] -= 5
            elif event.key == pygame.K_s:
                modelo1.translate[1] -= 5
            elif event.key == pygame.K_d:
                modelo1.translate[0] += 5
            elif event.key == pygame.K_1:
                rend.primitiveType = POINTS
            elif event.key == pygame.K_2:
                rend.primitiveType = LINES          


    rend.glClear()  

    
    rend.glRender()

    pygame.display.flip()  
    clock.tick(60)  

rend.generateFrameBuffer("./output.bmp")
pygame.quit()  


                
         