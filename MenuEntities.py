import pygame
HEIGHT = 900
WIDTH = 1600

class MenuCursor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/menuCursor.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.top = HEIGHT/2
    def update(self):
        if self.rect.top < HEIGHT/2:
            self.rect.bottom = HEIGHT/2 + 140 
        if self.rect.bottom > HEIGHT/2 + 140:
            self.rect.top = HEIGHT/2

class MenuButton(pygame.sprite.Sprite):
    def __init__(self, p_y, p_tex):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(p_tex).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.top = p_y