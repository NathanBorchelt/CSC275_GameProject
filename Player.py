import pygame
HEIGHT = 900
WIDTH = 1600

class Vector2f():
    def __init__(self, p_x, p_y):
        self.x = p_x
        self.y = p_y

class Player(pygame.sprite.Sprite):
    #sprite for the Player
    def __init__(self):
        self.pos = Vector2f(750, 750)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/playerSprite.png").convert_alpha()
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
        
        self.rect.centerx = self.pos.x
        self.rect.centery = self.pos.y

    def setPos(self, p_vector):
        self.pos.x = p_vector.x
        self.pos.y = p_vector.y


class Cursor(pygame.sprite.Sprite):
    #sprite for the Player
    
    def __init__(self):
        self.pos = Vector2f(750, 750)
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
        
        self.rect.centerx = self.pos.x
        self.rect.centery = self.pos.y
