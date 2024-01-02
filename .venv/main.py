import pygame

pygame.init()

HEIGHT=1200
WIDTH=800

main_display=pygame.display.set_mode((HEIGHT, WIDTH))

count =0
while True:
    print("")
    count+=1
    if count>=100:
        break
