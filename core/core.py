# -*- coding: utf-8 -*-
import pygame
from collision import Collision
from objects.cir import Circle

class Screen:
    screen_width = 1024
    screen_height = 576
    def __init__(self):
        
        pygame.init
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        done = False
        circle = Circle()
        circle.set_circle_positions(100,100)
        circle.draw_circle(screen)
        check_colision = Collision()
        
        clock = pygame.time.Clock()

        while not done:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    done = True
            
            #this element move to another file
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]:
                circle.move_circle(screen, 0, -5)
            if pressed[pygame.K_DOWN]:
                circle.move_circle(screen, 0, 5)
            if pressed[pygame.K_LEFT]:
                circle.move_circle(screen, -5, 0)
            if pressed[pygame.K_RIGHT]:
                circle.move_circle(screen, 5, 0)
            check_colision.check_board(circle.get_position_x(), circle.get_position_y())
            # next step is colision
            
            pygame.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    scr = Screen()

