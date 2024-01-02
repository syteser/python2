import pygame
from pygame.constants import QUIT

pygame.init()

HEIGHT = 600 #800
WIDTH = 800 #1200

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

player = pygame.Surface((20, 20))
player.fill((255, 255, 255))

plaing = True
while plaing:
    for event in pygame.event.get():
        if event.type == QUIT:
            plaing = False

    main_display.blit(player, (0, 0))

    pygame.display.flip()
