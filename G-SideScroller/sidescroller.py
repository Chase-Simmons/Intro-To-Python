import pygame, sys
from pygame.locals import *

clock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption('SideScroller')

WINDOW_SIZE = (1280, 720)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

player_image = pygame.image.load('player.png')

moving_right = False
moving_left = False

player_location = [50, 50]
player_y_momentum = 0
while True:

    screen.fill((146, 244, 255))
    screen.blit(player_image, player_location)

    if player_location[1] > WINDOW_SIZE[1]-player_image.get_height():
        player_y_momentum = -player_y_momentum
    else:
        player_y_momentum += 0.2

    player_location[1] += player_y_momentum

    if moving_right == True:
        player_location[0] += 4
        print(player_location)
    if moving_left == True:
        player_location[0] -= 4
        print(player_location)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_d:
                moving_right = True
            if event.key == K_a:
                moving_left = True
        if event.type == KEYUP:
            if event.key == K_d:
                moving_right = False
            if event.key == K_a:
                moving_left = False


    pygame.display.update()
    clock.tick(60)