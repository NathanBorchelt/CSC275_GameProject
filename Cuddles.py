import pygame
import random
import settings as st
vec = pg.math.Vector2

class Cuddles(pygame.sprite.Sprite):
    def __init__(self, playerSpeed = 0, playerPos = 0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60,30))
        self.image.fill(st.YELLOW)
        self.rect = self.image.get_rect()
        self.rect.top = st.HEIGHT*.7
        self.pos = (playerPos)
        self.velo = vec(playerSpeed,0)
        self.acc = vec(0,0)




class _CBody(pygame.sprite.Sprite):
    def __init__(self, head,size = [0,0]):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60,30))
        self.image.fill(st.BLUE)
        self.rect = self.image.get_rect()
        self.pos = (head.rect.left+round((size[0]*.8)), round(head.rect.top+round((head.rect.height*.5))-round((size[1]*.5))))
        self.velo = head.velo
        self.acc = head.acc
