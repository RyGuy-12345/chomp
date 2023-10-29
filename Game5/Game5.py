import pygame
import sys
import random
from player import Player

from fish import Fish, fishes
from background import draw_background
from game_paramaters import *

#initialize pygame
pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ocean")

#set clock
clock = pygame.time.Clock()

#main loop
running = True
background = screen.copy()
draw_background(background)

for a in range(5):
    fishes.add(Fish(random.randint(screen_width, screen_width*2), random.randint(tile_size, screen_height - tile_size*2)))


#orange player fish
player = Player(screen_width/2, screen_height/2)

while running:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
        #control player fish
        player.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move_up()
            if event.key == pygame.K_DOWN:
                player.move_down()
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_RIGHT:
                player.move_right()


    screen.blit(background, (0, 0))

    # update fish position
    fishes.update()
    #update player fish
    player.update()

    for fish in fishes:
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            fishes.add(Fish(random.randint(screen_width, screen_width * 2), random.randint(tile_size, screen_height - tile_size * 2)))


    fishes.draw(screen)
    player.draw(screen)

    pygame.display.flip()


    # set framerate
    clock.tick(100)



pygame.QUIT()



