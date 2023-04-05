from math import cos, radians, sin
import pygame
from random import *
import settings as st
import time

class Player(pygame.sprite.Sprite):
    #sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/jet.png").convert_alpha()
        self.image = pygame.transform.scale_by(self.image, st.scaleFactor)
        self.jetpackImage = pygame.image.load("res/jet.png").convert_alpha()
        self.jetpackImage = pygame.transform.scale_by(self.image, st.scaleFactor)
        self.rect = self.image.get_rect()
        self.rect.top = 700
        self.vel = 0
        self.acc = 0
        
        
    def update(self):
        self.rect.centerx = st.SCREEN_WIDTH/5

    #def speedUpdate(self,factor):
    #    #exponential speed increase
    #    maxSpeed=50
    #    if(self.speed < maxSpeed):
    #        self.speed = round(self.speed ** factor,3)
    #    else:
    #        self.speed = maxSpeed
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
    def __init__(self, mother = True, offset = 0):
        self.rot = randint(-90, 90)
        self.length = 200
        self.mother = mother
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("res/lazer.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.length * st.scaleFactor, 50 * st.scaleFactor))
        self.image = pygame.transform.rotate(self.image, self.rot)
        self.rect = self.image.get_rect()

        self.head = LazerEnd()
        self.tail = LazerEnd()

        self.head.xOffset = ((self.length * st.scaleFactor)/2 * cos(radians(float(self.rot))))
        self.head.yOffset = ((self.length * st.scaleFactor)/2 * sin(radians(float(self.rot))))
        self.tail.xOffset = -((self.length * st.scaleFactor)/2 * cos(radians(float(self.rot))))
        self.tail.yOffset = -((self.length * st.scaleFactor)/2 * sin(radians(float(self.rot))))

        self.rect.left = st.SCREEN_WIDTH + offset
        
        self.rect.centery = randint(0, int(st.SCREEN_HEIGHT - st.SCREEN_HEIGHT/7))

    def update(self):
        self.rect.x -= st.playerSpeed
        self.head.rect.center = (self.rect.centerx + self.head.xOffset, self.rect.centery - self.head.yOffset)
        self.tail.rect.center = (self.rect.centerx + self.tail.xOffset, self.rect.centery - self.tail.yOffset)
        if self.rect.right < 0:
            self.head.kill()
            self.tail.kill()
            self.kill()
    
class LazerEnd(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/shockerBall0.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50 * st.scaleFactor, 50 * st.scaleFactor))
        self.rect = self.image.get_rect()
        self.xOffset = 0
        self.yOffset = 0
        

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
        self.image = pygame.image.load("res/missle0.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = st.SCREEN_WIDTH + self.rect.width
        self.rect.y = p_y
        self.time = time.time()
    def update(self):
        if self.rect.right < 0:
            self.kill()
        self.rect.x -= st.playerSpeed + 25
        

class Cursor(pygame.sprite.Sprite):
    def __init__(self, p_x, p_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/cursor.png").convert_alpha()
        self.image = pygame.transform.scale_by(self.image, st.scaleFactor)
        self.rect = self.image.get_rect()
        self.rect.center = (p_x, p_y)