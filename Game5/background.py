import pygame
from game_paramaters import *
import random

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
