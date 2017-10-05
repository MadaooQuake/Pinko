# -*- coding: utf-8 -*-


import pygame
from pygame.locals import *

class Circle:
    positionX = positionY = 0
    
    def set_circle_positions(self, x, y):
        self.positionX = x
        self.positionY = y

    def draw_circle(self, screen):
        pygame.draw.circle(screen, (  0,   0, 255), (self.positionX, self.positionY), 60, 0)
        
    def move_circle(self, screen, x, y):
        screen.fill((0, 0, 0))
        self.positionY += y
        self.positionX += x
        pygame.draw.circle(screen, (  0,   0, 255), (self.positionX, self.positionY), 60, 0)
        
    def get_position_x(self):
        return self.positionX
    
    def get_position_y(self):
        return self.positionY
    
        