import pygame, sys, player__init__
from pygame.locals import *


player = player__init__.Player()

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Side Scroller')
WINDOW_SIZE = (1280, 720)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
dirt_img = pygame.image.load('dirt.png')
player_image = pygame.image.load('player.png')

frame = 0


player_bounds = pygame.Rect(player.x, player.y, player_image.get_width(), player_image.get_height())

test_bounds = pygame.Rect(0, 600, 1200, 50)
visual_test_bounds = pygame.Rect(0, 602, 1200, 50)


def collision_test(bounds, tiles):
    hit_list = []
    for tile in tiles:
        if bounds.colliderect(tile):
            hit_list.append(tile)
        return hit_list


def move(bounds, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    bounds.x += movement.x
    bounds.y += movement.y
    hit_list = collision_test(bounds, tiles)
    for tile in hit_list:
        if movement.x > 0:
            bounds.right = tile.left
            collision_types['right'] = True
        elif movement.x < 0:
            bounds.left = tile.right
            collision_types['left'] = True
    for tile in hit_list:
        if movement.y > 0:
            bounds.bottom = tile.top
            collision_types['bottom'] = True
        elif movement.y < 0:
            bounds.top = tile.bottom
            collision_types['top'] = True
    return bounds, collision_types


def jump():
    player.y -= player_bounds.height * 3
    player.jumping = False
    print(frame)


while True:

    frame += 1

    screen.fill((146, 244, 255))
    screen.blit(player_image, (player.x, player.y))

    if player.grounded is False:
        player.vertical_momentum = 5
    else:
        player.vertical_momentum = 0

    player.y += player.vertical_momentum
    player_bounds.x = player.x
    player_bounds.y = player.y

    if player.moving_right:
        player.x += 4
    if player.moving_left:
        player.x -= 4

    if player_bounds.colliderect(test_bounds):
        pygame.draw.rect(screen, (255, 0, 0), visual_test_bounds)
        player.grounded = True
    else:
        pygame.draw.rect(screen, (0, 0, 0), visual_test_bounds)
        player.grounded = False

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_d:
                player.moving_right = True
            if event.key == K_a:
                player.moving_left = True
            if event.key == K_SPACE and player.grounded is not False:
                jump()
                player.jumping = True
                player.grounded = False
        if event.type == KEYUP:
            if event.key == K_d:
                player.moving_right = False
            if event.key == K_a:
                player.moving_left = False


    pygame.display.update()
    clock.tick(60)