import random

import pygame
from game_paramaters import *
MIN_SPEED = 0.5
MAX_SPEED = 3.5

class Fish(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image = pygame.image.load("../assets/sprites/green_fish.png").convert()
        self.image.set_colorkey((0,0,0))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(MIN_SPEED, MAX_SPEED)
        self.rect.center = (x,y)

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x



    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.transform.flip()

fishes = pygame.sprite.Group()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image = pygame.image.load("../assets/sprites/puffer_fish.png").convert()
        self.image.set_colorkey((0,0,0))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = MAX_SPEED
        self.rect.center = (x,y)

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x



    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.transform.flip()

enemies = pygame.sprite.Group()
