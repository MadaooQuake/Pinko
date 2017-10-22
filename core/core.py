# -*- coding: utf-8 -*-
import pygame
from collision import Collision
from objects.cir import Circle
from controls import Control

class Screen:
    screen_width = 1024
    screen_height = 576
    move_available = True;
    def __init__(self):
        
        pygame.init
        control = Control()
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        done = False
        circle = Circle()
        circle.set_circle_positions(100,100)
        circle.draw_circle(screen)
        check_colision = Collision()
        check_colision.set_width_and_height(self.screen_width, self.screen_height)
        Control
        
        clock = pygame.time.Clock()

        while not done:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    done = True
            
            control.get_event(pygame.key.get_pressed())
            control.check_key()
            check_colision.get_move(control.get_x(), control.get_y())
            if check_colision.check_board(circle.get_position_x(),circle.get_position_y()):
                circle.move_circle(screen, control.get_x(), control.get_y())
            
            pygame.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    scr = Screen()

