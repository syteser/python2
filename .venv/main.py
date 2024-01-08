import os
import random

import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

'''константы'''
HEIGHT = 600  # 800
WIDTH = 1000  # 1200
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_RED = (255, 0, 0)

pygame.init()

FONT = pygame.font.SysFont('Verdana', 20)
FPS = pygame.time.Clock()
main_display = pygame.display.set_mode((WIDTH, HEIGHT))

bg = pygame.transform.scale(pygame.image.load('background.png'), (WIDTH, HEIGHT))
bg_X1 = 0
bg_X2 = bg.get_width()
bg_move = 3

IMAGE_PATH = "Goose"
PLAYER_IMAGES = os.listdir(IMAGE_PATH)

player_size = (100, 50)
player = pygame.transform.scale(pygame.image.load('player.png').convert_alpha(), player_size)
player_speed = bg_move + 1
player_rect = player.get_rect()
player_move_down = [0, player_speed]
player_move_up = [0, -player_speed]
player_move_right = [player_speed, 0]
player_move_left = [-player_speed, 0]


def create_enemy():
    eneme_size = (50, 30)
    enemy_speed = bg_move
    #    enemy = pygame.image.load('enemy.png').convert_alpha()
    enemy = pygame.transform.scale(pygame.image.load('enemy.png'), eneme_size)
    enemy_sdvig = 100
    enemy_rect = pygame.Rect(WIDTH, random.randint(enemy_sdvig, HEIGHT - enemy_sdvig), *eneme_size)
    enemy_move = [random.randint(-enemy_speed * 4, -enemy_speed * 2), 0]
    return [enemy, enemy_rect, enemy_move]


def create_bonus():
    bonus_size = (30, 30)
    bonus_speed = bg_move
    #   bonus = pygame.image.load('bonus.png').convert_alpha()
    bonus = pygame.transform.scale(pygame.image.load('bonus.png'), bonus_size)
    bonus_sdvig = 100
    bonus_rect = pygame.Rect(random.randint(bonus_sdvig, WIDTH - bonus_sdvig), 0, *bonus_size)
    bonus_move = [0, random.randint(bonus_speed, bonus_speed * 2)]
    return [bonus, bonus_rect, bonus_move]


CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)
CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 4)
CHANGE_IMAGE = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMAGE, 100)

enemies = []
bonuses = []
score = 0
image_index = 0

plaing = True
while plaing:
    FPS.tick(120 * 3)
    for event in pygame.event.get():
        if event.type == QUIT:
            plaing = False
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())
        if event.type == CHANGE_IMAGE:
            player = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, PLAYER_IMAGES[image_index])),
                                            player_size)
            image_index += 1
            if image_index >= len(PLAYER_IMAGES):
                image_index = 0

    #   main_display.fill((COLOR_BLACK))
    bg_X1 -= bg_move
    bg_X2 -= bg_move

    if bg_X1 < -bg.get_width():
        bg_X1 = bg.get_width()
    if bg_X2 < -bg.get_width():
        bg_X2 = bg.get_width()

    main_display.blit(bg, (bg_X1, 0))
    main_display.blit(bg, (bg_X2, 0))

    keys = pygame.key.get_pressed()

    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(player_move_down)
    if keys[K_UP] and player_rect.top > 0:
        player_rect = player_rect.move(player_move_up)
    if keys[K_RIGHT] and player_rect.right < WIDTH:
        player_rect = player_rect.move(player_move_right)
    if keys[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(player_move_left)

    for enemy in enemies:
        enemy[1] = enemy[1].move(enemy[2])
        main_display.blit(enemy[0], enemy[1])
        if player_rect.colliderect(enemy[1]):
            score -= 100
            enemies.pop(enemies.index(enemy))
            # plaing = False

    for bonus in bonuses:
        bonus[1] = bonus[1].move(bonus[2])
        main_display.blit(bonus[0], bonus[1])
        if player_rect.colliderect(bonus[1]):
            score += 1
            bonuses.pop(bonuses.index(bonus))

    '''вывод очков'''
    text_score = 'Счет: ' + str(score)
    main_display.blit(FONT.render(text_score, True, COLOR_BLACK), (WIDTH - len(text_score)*10-30, 20))
    '''вывод игрока'''
    main_display.blit(player, player_rect)
    pygame.display.flip()

    for enemy in enemies:
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))

    for bonus in bonuses:
        if bonus[1].bottom > HEIGHT:
            bonuses.pop(bonuses.index(bonus))
