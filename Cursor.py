import pygame
HEIGHT = 900
WIDTH = 1600
class Cursor(pygame.sprite.Sprite):
    #sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/cursor.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (750,750)
        
    def update(self):
        if self.rect.centery > 750:
            self.rect.centery = 750
        if self.rect.centery < 50:
            self.rect.centery = 50
        if self.rect.centerx > 1150:
            self.rect.centerx = 1150
        if self.rect.centerx < 450:
            self.rect.centerx = 450