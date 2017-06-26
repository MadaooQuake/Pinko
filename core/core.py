# -*- coding: utf-8 -*-
import pygame
from objects.cir import Circle

class Screen:

    def __init__(self):
        pygame.init
        screen = pygame.display.set_mode((1024, 576))
        done = False
        Circle().drawCircle(screen)


        while not done:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    print "to do"
                if event.type == pygame.QUIT:
                    done = True
            pygame.display.flip()

if __name__ == "__main__":
    scr = Screen()

