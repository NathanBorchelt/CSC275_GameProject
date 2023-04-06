from math import cos, radians, sin
import pygame
from random import *
import settings as st
import time

class Player(pygame.sprite.Sprite):
    #sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/player/player0.png").convert_alpha()
        self.image = pygame.transform.scale_by(self.image, st.scaleFactor)
        self.jetpackImage = pygame.image.load("res/jetpack/jetpack0.png").convert_alpha()
        self.jetpackImage = pygame.transform.scale_by(self.image, st.scaleFactor)
        self.rect = self.image.get_rect()
        self.rect.top = 700
        self.vel = 0
        self.acc = 0
        self.frameCounter = 0
        self.flying = False


    def update(self):
        self.rect.centerx = st.SCREEN_WIDTH/5
        if self.flying:
            self.frameCounter -= 1
        else:
            self.frameCounter += 1
        self.image = pygame.image.load(f"res/player/player{int(self.frameCounter /10 % 5)}.png").convert_alpha()
        self.image = pygame.transform.scale_by(self.image, st.scaleFactor)

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
        self.image = pygame.image.load("res/hazards/tempG.png").convert_alpha()
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
        self.frameCount = 0
        self.scale = self.length * st.scaleFactor, 50 * st.scaleFactor
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("res/hazards/bar/bar0.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, self.scale)
        self.image = pygame.transform.rotate(self.image, self.rot)
        self.rect = self.image.get_rect()

        self.head = LazerEnd()
        self.tail = LazerEnd()

        self.xOff = ((self.length * st.scaleFactor)/2 * cos(radians(float(self.rot))))
        self.yOff = ((self.length * st.scaleFactor)/2 * sin(radians(float(self.rot))))

        self.head.xOffset = -self.xOff
        self.head.yOffset = -self.yOff
        self.tail.xOffset = self.xOff
        self.tail.yOffset = self.yOff

        self.rect.left = st.SCREEN_WIDTH + offset

        self.rect.centery = randint(0, int(st.SCREEN_HEIGHT - st.SCREEN_HEIGHT/7))

    def update(self):
        self.frameCount += 1
        self.rect.x -= st.playerSpeed
        self.head.rect.center = (self.rect.centerx + self.head.xOffset, self.rect.centery - self.head.yOffset)
        self.tail.rect.center = (self.rect.centerx + self.tail.xOffset, self.rect.centery - self.tail.yOffset)
        self.image = pygame.image.load(f"res/hazards/bar/bar{int(self.frameCount % 40 / 10) + 1}.png")
        self.image = pygame.transform.scale(self.image, self.scale)
        self.image = pygame.transform.rotate(self.image, self.rot)
        if self.rect.right < 0:
            self.head.kill()
            self.tail.kill()
            self.kill()

class LazerEnd(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.frameCount = 0
        self.image = pygame.image.load("res/hazards/shockerball/shockerBall0.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50 * st.scaleFactor, 50 * st.scaleFactor))
        self.rect = self.image.get_rect()
        self.xOffset = 0
        self.yOffset = 0

    def update(self):
        self.frameCount += 1
        self.image = pygame.image.load(f"res/hazards/shockerball/shockerBall{int(self.frameCount % 40 / 10) + 1}.png")

class MissleWarning(pygame.sprite.Sprite):
    def __init__(self, p_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/hazards/missleWarning.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = st.SCREEN_WIDTH - self.rect.width
        self.rect.y = p_y
        self.spawnTime = time.time()
        self.spawn = 0
    def update(self):
        self.spawn = time.time() - self.spawnTime
        if self.spawn % .5 > .25:
            self.image = pygame.image.load("res/hazards/missleWarning.png").convert_alpha()
        else:
            self.image = pygame.image.load("res/hazards/missleWarning2.png").convert_alpha()

class Missle(pygame.sprite.Sprite):
    def __init__(self, p_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/hazards/missle0.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = st.SCREEN_WIDTH + self.rect.width
        self.rect.y = p_y
        self.time = time.time()
    def update(self):
        if self.rect.right < 0:
            self.kill()
        self.rect.x -= st.playerSpeed + 25

class VehicleSpawn(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.frameCount = 0
        self.image = pygame.image.load("res/vehicle/box/box0.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = st.SCREEN_WIDTH + self.rect.width
        self.rect.y = st.SCREEN_HEIGHT + st.SCREEN_HEIGHT*3/16
        print("spawn")
    def update(self):
        self.rect.x -= st.playerSpeed
        self.frameCount += 1
        self.image = pygame.image.load(f"res/vehicle/box/box{int(self.frameCount % 40 / 10) + 1}.png")
        if self.rect.right < 0:
            self.kill()


class Cursor(pygame.sprite.Sprite):
    def __init__(self, p_x, p_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/menu/cursor.png").convert_alpha()
        self.image = pygame.transform.scale_by(self.image, st.scaleFactor)
        self.rect = self.image.get_rect()
        self.rect.center = (p_x, p_y)
