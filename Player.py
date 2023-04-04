import pygame
from random import *
import settings as st
from math import sin, cos, radians
class Player(pygame.sprite.Sprite):
    #sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/jet.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = st.HEIGHT*.7
        self.vel = 0
        self.acc = 0
        self.speed = 2
        self.score = 0


    def changeImage(self, p_tex):
        self.image = pygame.image.load(p_tex)


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
        self.rect.bottom = st.HEIGHT
        self.rect.left = p_x
        self.startPos = p_x

class Hazard(pygame.sprite.Sprite):
    def __init__(self, height = 150, mother = True, offset = 0):
        self.height = height
        self.mother = mother
        pygame.sprite.Sprite.__init__(self)

        self.head = pygame.image.load("res/shockerBall0.png").convert_alpha()
        self.body = pygame.image.load("res/lazer.png").convert_alpha()
        self.tail = pygame.image.load("res/shockerBall0.png").convert_alpha()
        self.head_rect = self.head.get_rect()
        self.body_rect = self.body.get_rect()
        self.tail_rect = self.tail.get_rect()
        #if type == 0:
            #self.image.fill((170, 0, 0))
        rot = randint(-90,90)
        size = randint(160,240)

        self.body - pygame.transform.rotate(rot)

        self.body_rect.centery = self.height

        self.heady = size/2*sin(radians(rot))
        self.headx = size/2*cos(radians(rot))

        self.taily = -size/2*sin(radians(rot))
        self.tailx = -size/2*cos(radians(rot))

    def update(self):
        if self.body_rect.right < 0:
            self.body_rect.left = 1600
            self.head_rect.centery = randint(0 + self.height/2, 900 - self.height/2)
        self.body_rect.x -= st.playerSpeed
        self.head_rect.center = (self.body_rect.centerx+self.headx, self.body_rect.centery +self.heady)
        self.tail_rect.center = (self.body_rect.centerx+self.tailx, self.body_rect.centery +self.taily)
        if self.rect.right < 0:
            self.kill()
