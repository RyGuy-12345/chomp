import pygame
import sys
import random
from player import Player

from fish import Fish, fishes, Enemy, enemies
from background import draw_background, add_fish, add_enemy
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

#draw fish
add_fish(5)
add_enemy(2)

#orange player fish
player = Player(screen_width/2, screen_height/2)


#score
score = 0
score_font = pygame.font.Font("../assets/fonts/Black_Crayon.ttf", 75)

#sounds
yum = pygame.mixer.Sound("../assets/sounds/hurt.wav")


while running:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
        #control player fish
        #player.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move_up()
            if event.key == pygame.K_DOWN:
                player.move_down()
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_RIGHT:
                player.move_right()
        if event.type == pygame.KEYUP:
            player.stop()


    screen.blit(background, (0, 0))

    # update fish position
    fishes.update()
    #update player fish
    player.update()
    #update enemy
    enemies.update()


    #check for collisions
    result = pygame.sprite.spritecollide(player, fishes, True)
    print(result)
    if result:
        pygame.mixer.Sound.play(yum)
        score += len(result)

     #draw more fish
        for s in range(len(result)):
            add_fish(1)

    #check for collisions w enemies
    result = pygame.sprite.spritecollide(player, enemies, True)
    print(result)
    if result:
        pygame.mixer.Sound.play(yum)
        score += len(result)
        for s in range(len(result)):
            add_enemy(1)


#print more fish if off screen
        for fish in fishes:
            if fish.rect.x < -fish.rect.width:
                fishes.remove(fish)
                fishes.add(Fish(random.randint(screen_width, screen_width * 2), random.randint(tile_size, screen_height - tile_size * 2)))

#print more enemies if off screen
        for enemy in enemies:
            if enemy.rect.x < -enemy.rect.width:
                enemies.remove(enemy)
                enemies.add(Enemy(random.randint(screen_width, screen_width * 2), random.randint(tile_size, screen_height - tile_size * 2)))


    #draw fish
    fishes.draw(screen)
    player.draw(screen)
    enemies.draw(screen)

    #display font
    text = score_font.render(f"{score}", True, (255, 29, 0))
    screen.blit(text, (screen_width - text.get_width() - 30, 0))

    pygame.display.flip()


    # set framerate
    clock.tick(100)



pygame.QUIT()



