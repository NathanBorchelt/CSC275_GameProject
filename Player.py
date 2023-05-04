from math import cos, radians, sin
import pygame
from random import *
import settings as st
import time



class Player(pygame.sprite.Sprite):
    #sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/player/UFO0.png").convert_alpha()
        self.image = pygame.transform.scale_by(self.image, st.scaleFactor)
        self.rect = self.image.get_rect()
        self.rect.top = 700
        self.vely = 0
        self.velx = 0
        self.frameCounter = 0
        self.flying = False
        self.rect.centerx = st.SCREEN_WIDTH/5
        self.prevPos = self.rect.x
        self.state = 0
        self.money = 0
        self.shotgun = 3
        self.invincible = 0
        self.color = 170

    def update(self):
        self.color += 5
        if self.color > 255:
            self.color = 170
        if self.prevPos < self.rect.x:
            if self.state != 1:
                self.state = 1
                self.frameCounter = 0
            self.image = pygame.image.load(f"res/player/UFO_R{int(self.frameCounter /10 % 3)}.png").convert_alpha()

        elif self.prevPos > self.rect.x:
            if self.state != -1:
                self.state = -1
                self.frameCounter = 0
            self.image = pygame.image.load(f"res/player/UFO_L{int(self.frameCounter /10 % 3)}.png").convert_alpha()
        else:
            if self.state != 0:
                self.state = 0
                self.frameCounter = 0
            self.image = pygame.image.load(f"res/player/UFO{int(self.frameCounter /10 % 3)}.png").convert_alpha()
        self.image = pygame.transform.scale_by(self.image, st.scaleFactor)
        if self.invincible > 0:
            self.image.fill(pygame.Color(0, 0, self.color), None, pygame.BLEND_RGB_MAX)
            self.invincible -= 1
        self.prevPos = self.rect.x
        self.frameCounter += 1

    def speedUpdate(self,factor):
        #exponential speed increase
        maxSpeed = 15
        if(st.playerSpeed < maxSpeed):
            st.playerSpeed = round(st.playerSpeed ** factor,3)
        else:
            st.playerSpeed = maxSpeed
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
        self.mother = mother
        pygame.sprite.Sprite.__init__(self)
        self.length = 200
        self.rot = randint(0, 179)
        self.image = pygame.image.load("res/hazards/lazer.png").convert_alpha()
        self.image = pygame.transform.rotate(self.image, self.rot)
        self.rect = self.image.get_rect()

        self.head = LazerEnd(self)
        self.tail = LazerEnd(self)

        self.head.xOffset = ((self.length)/2 * cos(radians(float(self.rot))))
        self.head.yOffset = ((self.length)/2 * sin(radians(float(self.rot))))
        self.tail.xOffset = -((self.length)/2 * cos(radians(float(self.rot))))
        self.tail.yOffset = -((self.length)/2 * sin(radians(float(self.rot))))

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
    def __init__(self, parent):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/hazards/shockerBall0.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50 * st.scaleFactor, 50 * st.scaleFactor))
        self.rect = self.image.get_rect()
        self.xOffset = 0
        self.yOffset = 0
        self.parent = parent


class MissleWarning(pygame.sprite.Sprite):
    def __init__(self, p_y, game):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/hazards/missleWarning.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = st.SCREEN_WIDTH - self.rect.width
        self.rect.y = p_y
        self.frameCounter = 0
        self.game = game

    def update(self):
        if self.frameCounter%30 == 0:
            self.image = pygame.image.load("res/hazards/missleWarning.png").convert_alpha()
        elif self.frameCounter%30 == 15:
            self.image = pygame.image.load("res/hazards/missleWarning2.png").convert_alpha()
            self.game.missleBeep.play()
        self.frameCounter += 1

class Coin(pygame.sprite.Sprite):
    def __init__(self,host,value):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((30,30))
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect()
        #self.game = host.game
        self.value = value
        self.rect.center = host.rect.center

    def update(self):
        if self.rect.right < 0:
            self.kill()
        self.rect.x -= st.playerSpeed

class Missle(pygame.sprite.Sprite):
    def __init__(self, p_y, game):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/hazards/missle0.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = st.SCREEN_WIDTH + self.rect.width
        self.rect.y = p_y
        self.time = time.time()
        self.game = game

    def update(self):
        if self.rect.right < 0:
            self.kill()
            self.game.missleSound.stop()
        self.rect.x -= st.playerSpeed + 25


class Cursor(pygame.sprite.Sprite):
    def __init__(self, p_x, p_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/menu/cursor.png").convert_alpha()
        self.image = pygame.transform.scale_by(self.image, st.scaleFactor)
        self.rect = self.image.get_rect()
        self.rect.center = (p_x, p_y)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,p_x, p_y, dir):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/player/bullet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 15))
        self.rect = self.image.get_rect()
        self.rect.center = (p_x, p_y)
        self.dir = dir

    def update(self):
        if self.dir == 'right':
            self.rect.x += 10
        elif self.dir == 'up':
            self.rect.x += 7
            self.rect.y -= 3
        elif self.dir == 'down':
            self.rect.x += 7
            self.rect.y += 3
        if self.rect.left > st.SCREEN_WIDTH:
            self.kill()

class Gun(pygame.sprite.Sprite):
    def __init__(self, groups, game):
        pygame.sprite.Sprite.__init__(self)
        self.type = choice([1,2,3,4])
        self.image = pygame.image.load("res/hazards/gun.png").convert_alpha()
        if self.type == 3:
            self.image = pygame.transform.rotate(self.image, 90)
        if self.type == 4:
            self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()
        self.rect.right = st.SCREEN_WIDTH
        self.rect.top = 0
        if self.type == 2 or self.type == 4:
            self.rect.bottom = st.SCREEN_HEIGHT
        self.spawn = time.time()
        self.groups = groups
        self.game = game

    def update(self):
        if self.type == 1:
            self.rect.y += 3
            if time.time() - self.spawn > .75:
                self.spawn = time.time()
                bullet = EnemyBullet(self.rect.x, self.rect.centery, 'left')
                for group in self.groups:
                    group.add(bullet)
                self.game.gunShoot.play()
        if self.type == 2:
            self.rect.y -= 3
            if time.time() - self.spawn > .75:
                self.spawn = time.time()
                bullet = EnemyBullet(self.rect.x, self.rect.centery, 'left')
                for group in self.groups:
                    group.add(bullet)
                self.game.gunShoot.play()
        if self.type == 3:
            self.rect.x -= 3
            if time.time() - self.spawn > .75:
                self.spawn = time.time()
                bullet = EnemyBullet(self.rect.centerx, self.rect.y + self.rect.h, 'down')
                for group in self.groups:
                    group.add(bullet)
                self.game.gunShoot.play()
        if self.type == 4:
            self.rect.x -= 3
            if time.time() - self.spawn > .75:
                self.spawn = time.time()
                bullet = EnemyBullet(self.rect.centerx, self.rect.y, 'up')
                for group in self.groups:
                    group.add(bullet)
                self.game.gunShoot.play()
        if self.rect.right < 0 or self.rect.top > st.SCREEN_HEIGHT or self.rect.bottom < 0:
            self.kill()



class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, p_x, p_y, dir):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/hazards/bullet.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (p_x, p_y)

        self.dir = dir
        if self.dir == 'left':
            self.image = pygame.transform.rotate(self.image, 180)
        if self.dir == 'up':
            self.image = pygame.transform.rotate(self.image, 90)
        if self.dir == 'down':
            self.image = pygame.transform.rotate(self.image, 270)
    def update(self):
        if self.dir == 'left':
            self.rect.x -= st.playerSpeed + 5
        if self.dir == 'up':
            self.rect.y -= st.playerSpeed + 5
            #self.rect.x -= 3
        if self.dir == 'down':
            self.rect.y += st.playerSpeed + 5
            #self.rect.x -= 3
        if self.rect.right < 0:
            self.kill()
class Powerups(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.type = choice(['shotgun'])
        self.image = pygame.image.load(f"res/{self.type}.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    def update(self):
        self.rect.x -= 3