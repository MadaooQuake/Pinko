# -*- coding: utf-8 -*-


import pygame
from pygame.locals import *

class Circle:
    positionX = 0
    positionY = 0

    def __init__(self):
        print "draw"
    
    def setCirclePositions(self, x, y):
        self.positionX = x
        self.positionY = y

    def drawCircle(self, screen):
        pygame.draw.circle(screen, (  0,   0, 255), (self.positionX, self.positionY), 60, 0)
        
    def moveCircle(self, screen, x, y):
        screen.fill((0, 0, 0))
        self.positionY += y
        self.positionX += x
        pygame.draw.circle(screen, (  0,   0, 255), (self.positionX, self.positionY), 60, 0)
        
    def getPositionX(self):
        return positionX
    
    def getPositionY(self):
        return positionY
    
        