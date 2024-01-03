import pygame
import random

from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

'''константы'''
HEIGHT = 600  # 800
WIDTH = 800  # 1200
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
PLAYER_SIZE = (20, 20)

pygame.init()
FPS = pygame.time.Clock()
main_display = pygame.display.set_mode((WIDTH, HEIGHT))

player = pygame.Surface(PLAYER_SIZE)
player.fill(COLOR_WHITE)
player_rect = player.get_rect()
# player_speed = [1, 1]
player_move_down = [0, 1]
player_move_up = [0, -1]
player_move_right=[1,0]
player_move_left=[-1,0]


plaing = True
while plaing:
    FPS.tick(120 * 3)
    for event in pygame.event.get():
        if event.type == QUIT:
            plaing = False

    main_display.fill((COLOR_BLACK))

    keys = pygame.key.get_pressed()

    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(player_move_down)
    if keys[K_UP] and player_rect.top >0:
        player_rect=player_rect.move(player_move_up)
    if keys[K_RIGHT] and player_rect.right <WIDTH:
        player_rect=player_rect.move(player_move_right)
    if keys[K_LEFT] and player_rect.left >0:
        player_rect=player_rect.move(player_move_left)

    '''рисуем игрока, смещаем игрока, обновляем экран'''
    main_display.blit(player, player_rect)
    #    player_rect = player_rect.move(player_speed)
    pygame.display.flip()

    #   if player_rect.bottom >= HEIGHT or player_rect.top < 0:
    #       player_speed[1] = -player_speed[1]
    #   if player_rect.right >= WIDTH or player_rect.left < 0:
    #       player_speed[0] = -player_speed[0]
#    if player_rect.bottom >= HEIGHT:
#        player_speed = random.choice(([1, -1], [-1, -1]))
#    if player_rect.top <= 0:
#        player_speed = random.choice(([-1, 1], [1, 1]))
#    if player_rect.right >= WIDTH:
#        player_speed = random.choice(([-1, -1], [-1, 1]))
#    if player_rect.left <= 0:
#        player_speed = random.choice(([1, 1], [1, -1]))
