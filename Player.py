import pygame
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