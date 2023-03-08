import pygame
from random import *
import settings as st
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
<<<<<<< HEAD
        self.speed = 2
        self.score = 0


=======
    def changeImage(self, p_tex):
        self.image = pygame.image.load(p_tex)
        
        
>>>>>>> 62e5c09181ea809694a2592ddd1ae0df530bc7fc
    def update(self):
        self.rect.centerx = 350

    def speedUpdate(self,factor):
        #exponential speed increase
        maxSpeed=50
        if(self.speed < maxSpeed):
            self.speed = round(self.speed ** factor,3)
        else:
            self.speed = maxSpeed
class Ground(pygame.sprite.Sprite):
    def __init__(self, p_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/tempG.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.bottom = 900
        self.rect.left = p_x
        self.startPos = p_x

class Hazard(pygame.sprite.Sprite):
    def __init__(self, height = 150, mother = True, offset = 0, type = 0):
        self.height = height
        self.mother = mother
        self.type = type
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((50, self.height))
        self.image = pygame.image.load("res/lazer.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(50, height))
        
        #if type == 0:            
            #self.image.fill((170, 0, 0))

        if type == 1:
            #self.image = self.image.convert_alpha()
            #self.image.fill((0, 170, 0, 255))
            self.image = pygame.transform.rotate(self.image, 45)
        elif type == 2:
            #self.image = self.image.convert_alpha()
            #self.image.fill((170, 170, 0, 255))
            self.image = pygame.transform.rotate(self.image, -45)
        elif type == 3:
            #self.image.fill((0, 0, 170))
            self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.left = WIDTH + offset
        self.rect.centery = randint(0 + self.height/2, HEIGHT - self.height/2-150)

    def update(self):
<<<<<<< HEAD
        if self.rect.right < 0:
            self.rect.left = 1600
            self.rect.centery = randint(0 + self.height/2, 900 - self.height/2)
=======
        self.rect.x -= st.playerSpeed
        if self.rect.right < 0:
            self.kill()
        
>>>>>>> 62e5c09181ea809694a2592ddd1ae0df530bc7fc
