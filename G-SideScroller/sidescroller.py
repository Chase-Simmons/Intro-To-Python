import pygame, sys
from pygame.locals import *

pygame.init()

WINDOW_SIZE = (1280, 720)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()