# -*- coding: utf-8 -*-
import pygame
from objects.cir import Circle

class Screen:

    def __init__(self):
        pygame.init
        screen = pygame.display.set_mode((1024, 576))
        done = False
        circle = Circle()
        circle.setCirclePositions(100,100)
        circle.drawCircle(screen)
        
        clock = pygame.time.Clock()

        while not done:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    done = True
            
            #this element move to another file
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]:
                circle.moveCircle(screen, 0, -5)
            if pressed[pygame.K_DOWN]:
                circle.moveCircle(screen, 0, 5)
            if pressed[pygame.K_LEFT]:
                circle.moveCircle(screen, -5, 0)
            if pressed[pygame.K_RIGHT]:
                circle.moveCircle(screen, 5, 0)
                
            # next step is colision
            pygame.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    scr = Screen()

