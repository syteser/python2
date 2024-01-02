import pygame, sys

"""константы"""
application_name = 'Game name'
screen_x=800
screen_y=600

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((screen_x, screen_y))
    pygame.init()
    pygame.display.set_caption(application_name)

    run = True
    while run:
        screen.fill((192, 192, 192))
        pygame.display.update()
#        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

def start_game():
    pass

init_game()
start_game()
