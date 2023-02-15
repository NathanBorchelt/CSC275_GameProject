import pygame
from random import *
HEIGHT = 900
WIDTH = 1600

class Player(pygame.sprite.Sprite):
    #sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/jet.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = 700
        self.vel = 0
        self.acc = 0
        
        
    def update(self):
        self.rect.centerx = 350
class Ground(pygame.sprite.Sprite):
    def __init__(self, p_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/tempG.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = 900
        self.rect.left = p_x

class Hazard(pygame.sprite.Sprite):
    def __init__(self, p_height):
        self.height = p_height
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, self.height))
        self.image.fill((170, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.left = 1600
        self.rect.centery = randint(0 + self.height/2, 900 - self.height/2)
    def update(self):
        self.rect.x -= 10
        if self.rect.right < 0:
            self.rect.left = 1600
            self.rect.centery = randint(0 + self.height/2, 900 - self.height/2)