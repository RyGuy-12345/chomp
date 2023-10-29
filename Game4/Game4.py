import pygame
import sys
import random
from fish import Fish, fishes

pygame.init()

screen_width = 800
screen_height = 600
tile_size = 64

#add pygame clock
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ocean")


def draw_background(screen):
    water = pygame.image.load("../assets/sprites/water.png").convert()
    sand = pygame.image.load("../assets/sprites/sand_top.png").convert()
    seagrass = pygame.image.load("../assets/sprites/seagrass.png").convert()
    sand.set_colorkey((0, 0, 0))
    seagrass.set_colorkey((0, 0, 0))

    for x in range(0,screen_width,tile_size):
        for y in range(0,screen_height, tile_size):
            screen.blit(water, (x,y))

    #sand
    for x in range(0,screen_width,tile_size):
        screen.blit(sand, (x,screen_height-tile_size))

    #seagrass
    for _ in range(7):
        x = random.randint(0,screen_width)
        screen.blit(seagrass, (x, screen_height- tile_size*2+5))

    custom_font = pygame.font.Font("../assets/fonts/Black_Crayon.ttf", 115)
    text = custom_font.render("chomp", True, (255, 29, 0))
    screen.blit(text, (screen_width / 2 - text.get_width() / 2, screen_height / 7 - text.get_height() / 2))


#main loop
running = True
background = screen.copy()
draw_background(background)

for a in range(5):
    fishes.add(Fish(random.randint(screen_width, screen_width*2), random.randint(tile_size, screen_height - tile_size*2)))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0,0))

    #update fish position
    fishes.update()

    #check if fish have left the screen
    for fish in fishes:
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            fishes.add(Fish(random.randint(screen_width, screen_width * 2), random.randint(tile_size, screen_height - tile_size * 2)))

    fishes.draw(screen)
    pygame.display.flip()

    #set framerate
    clock.tick(100)
pygame.quit()