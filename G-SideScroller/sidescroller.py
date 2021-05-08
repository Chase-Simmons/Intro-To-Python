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


class Cords:
    def __init__(self, x, y):
        self.x = x
        self.y = y


player_location = Cords(50, 50)
player_y_momentum = 0
player_bounds = pygame.Rect(player_location.x, player_location.y, player_image.get_width(), player_image.get_height())

test_bounds = pygame.Rect(100, 100, 100, 50)

while True:

    screen.fill((146, 244, 255))
    screen.blit(player_image, (player_location.x, player_location.y))

    if player_location.y > WINDOW_SIZE[1]-player_image.get_height():
        player_y_momentum = -player_y_momentum
    else:
        player_y_momentum += 0.2

    player_location.y += player_y_momentum
    player_bounds.x = player_location.x
    player_bounds.y = player_location.y

    if moving_right == True:
        player_location.x += 4
    if moving_left == True:
        player_location.x -= 4

    if player_bounds.colliderect(test_bounds):
        pygame.draw.rect(screen, (255, 0, 0), test_bounds)
    else:
        pygame.draw.rect(screen, (0, 0, 0), test_bounds)

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