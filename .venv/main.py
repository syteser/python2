import pygame
from pygame.constants import QUIT

pygame.init()
FPS=pygame.time.Clock()

HEIGHT = 600  # 800
WIDTH = 800  # 1200
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK=(0,0,0)
PLAYER_SIZE = (20, 20)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

player = pygame.Surface(PLAYER_SIZE)
player.fill(COLOR_WHITE)
player_rect = player.get_rect()
player_speed = [1, 1]

plaing = True
while plaing:
    FPS.tick(120)
    for event in pygame.event.get():
        if event.type == QUIT:
            plaing = False

    main_display.fill((COLOR_BLACK))
    main_display.blit(player, player_rect)
    player_rect=player_rect.move(player_speed)

    pygame.display.flip()
