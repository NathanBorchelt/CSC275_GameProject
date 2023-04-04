import pygame
from random import *
import settings as st
import time

class Player(pygame.sprite.Sprite):
    #sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/jet.png").convert_alpha()
        self.image = pygame.transform.scale_by(self.image, st.SCREEN_WIDTH/st.BASE_WIDTH)
        self.jetpackImage = pygame.image.load("res/jet.png").convert_alpha()
        self.jetpackImage = pygame.transform.scale_by(self.image, st.SCREEN_WIDTH/st.BASE_WIDTH)
        self.rect = self.image.get_rect()
        self.rect.top = 700
        self.vel = 0
        self.acc = 0
        
        
    def update(self):
        self.rect.centerx = st.SCREEN_WIDTH/5

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
        self.image = pygame.transform.scale(self.image, (st.SCREEN_WIDTH/4, st.SCREEN_HEIGHT/8))
        self.rect = self.image.get_rect()
        self.rect.bottom = st.SCREEN_HEIGHT
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
        self.rect.left = st.SCREEN_WIDTH + offset
        self.rect.centery = randint(0 + self.height/2, st.SCREEN_HEIGHT - self.height/2-150)

    def update(self):
        self.rect.x -= st.playerSpeed
        if self.rect.right < 0:
            self.kill()

class MissleWarning(pygame.sprite.Sprite):
    def __init__(self, p_y):      
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/missleWarning.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = st.SCREEN_WIDTH - self.rect.width
        self.rect.y = p_y
        self.spawnTime = time.time()
        self.spawn = 0
    def update(self):
        self.spawn = time.time() - self.spawnTime
        if self.spawn % .5 > .25:
            self.image = pygame.image.load("res/missleWarning.png").convert_alpha()
        else:
            self.image = pygame.image.load("res/missleWarning2.png").convert_alpha()

class Missle(pygame.sprite.Sprite):
    def __init__(self, p_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/missle.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = st.SCREEN_WIDTH + self.rect.width
        self.rect.y = p_y
    def update(self):
        if self.rect.right < 0:
            self.kill()
        self.rect.x -= st.playerSpeed + 15

class Cursor(pygame.sprite.Sprite):
    def __init__(self, p_x, p_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/cursor.png").convert_alpha()
        self.image = pygame.transform.scale_by(self.image, st.SCREEN_WIDTH/st.BASE_WIDTH)
        self.rect = self.image.get_rect()
        self.rect.center = (p_x, p_y)