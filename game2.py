import pygame
import sys
import random

pygame.init()

screen_width = 800
screen_height = 600
tile_size = 64

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ocean")

custom_font = pygame.font.Font("../labs/L8/fonts/Brainfish_Rush.ttf")

def draw_background(screen):
    water = pygame.image.load("../labs/L7/sprites/water.png").convert()
    sand = pygame.image.load("../labs/L7/sprites/sand_top.png").convert()
    seagrass = pygame.image.load("../labs/L7/sprites/seagrass.png").convert()
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


    text = custom_font.render("chomp", True, (255, 29, 0))
    screen.blit(text, (screen_width/2-text.get_width()/2, screen_height/2-text.get_height()/2))


running = True
background = screen.copy()
draw_background(background)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0,0))
    pygame.display.flip()
pygame.quit()