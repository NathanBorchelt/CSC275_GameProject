import pygame
import time
from Player import *

WIDTH = 1600
HEIGHT = 900
FPS = 30
#define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

        
# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Joypack Jetride")
clock = pygame.time.Clock()
#create sprite group and add the player sprite to it
all_sprites = pygame.sprite.Group()
#Game loop``
running = True
game = True
player = Player()
all_sprites.add(player)
keyDownSpace = False
startTime = time.time()
while running:
    while game:
        clock.tick(FPS)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    keyDownSpace = True
                elif event.key == pygame.K_ESCAPE:
                    running = False
                    game = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    keyDownSpace = False
                    startTime = time.time()
        
        if keyDownSpace:
            player.acc = 1
        else:
            player.acc = -1
        player.vel += player.acc 
        player.rect.y -= player.vel
        if player.rect.bottom > 900:
            player.rect.bottom = 900
            player.vel = 0
        if player.rect.top < 0:
            player.rect.top = 0
            player.vel = 0

        all_sprites.update()       
        screen.fill(BLACK)
        all_sprites.draw(screen)
        pygame.display.flip()
pygame.quit()
