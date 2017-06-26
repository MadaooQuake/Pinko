# -*- coding: utf-8 -*-


import pygame
from pygame.locals import *

class Circle:

    def __init__(self):
        print "draw"

    def drawCircle(self, screen):
        pygame.draw.circle(screen, (  0,   0, 255), (50, 0), 60, 0)