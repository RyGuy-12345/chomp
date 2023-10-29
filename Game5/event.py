import pygame
import sys

from game_paramaters import *
from background import draw_background

#initialize pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ocean")

#main loop
running = True
background = screen.copy()
draw_background(background)

while running:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print('you pressed the Up Key')
            if event.key == pygame.K_DOWN:
                print('you pressed the down Key')
            if event.key == pygame.K_LEFT:
                print('you pressed the left key')
            if event.key == pygame.K_RIGHT:
                print('you pressed the right key')
                



    #draw the background
    screen.blit(background, (0,0))

    pygame.display.flip()
pygame.quit()
