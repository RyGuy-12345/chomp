import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600

BLUE = (0, 0, 225)
Brown = (222, 204, 113)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ocean")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLUE)

    rectangle_height = 150
    pygame.draw.rect(screen, Brown, (0,screen_height-rectangle_height, screen_width, rectangle_height))

    pygame.display.flip()
pygame.QUIT
