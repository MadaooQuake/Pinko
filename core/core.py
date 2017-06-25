# -*- coding: utf-8 -*-
import pygame
from objects.cir import Circle

class Screen:

    def __init__(self):
        pygame.init
        screen = pygame.display.set_mode((1024, 576))
        done = False
        Circle().drawCircle(screen)
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            pygame.display.flip()

if __name__ == "__main__":
    scr = Screen()

