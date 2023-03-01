import pygame
from Player import *

WIDTH = 1600
HEIGHT = 900
FPS = 60
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
ground_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
#Game loop``
running = True
game = True
keyDownSpace = False
ground = Ground(0)
ground1 = Ground(400)
ground2 = Ground(800)
ground3 = Ground(1200)
ground4 = Ground(1600)
player = Player()
obj = Hazard(200)
all_sprites.add(ground)
all_sprites.add(ground1)
all_sprites.add(ground2)
all_sprites.add(ground3)
all_sprites.add(ground4)
all_sprites.add(obj)
ground_sprites.add(ground)
ground_sprites.add(ground1)
ground_sprites.add(ground2)
ground_sprites.add(ground3)
ground_sprites.add(ground4)
all_sprites.add(player)
obstacles.add(obj)
counter = 0

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
        if keyDownSpace:
            player.acc = 1
        else:
            player.acc = -1
        player.vel += player.acc
        player.rect.y -= player.vel
        if player.rect.bottom > 750:
            player.rect.bottom = 750
            player.vel = 0
        if player.rect.top < 0:
            player.rect.top = 0
            player.vel = 0
        for i in obstacles:
            if pygame.sprite.collide_rect(player, i):
                running = False
                game = False
                print("LOSER!")
                print(player.score)
        if counter >= round(400/player.speed):
            for i in ground_sprites:
                i.rect.x += 400
                counter = 0
                player.speedUpdate(1.01)
                print(player.speed)
                ground.rect.x = ground.startPos
                ground1.rect.x = ground1.startPos
                ground2.rect.x = ground2.startPos
                ground3.rect.x = ground3.startPos
                ground4.rect.x = ground4.startPos
        for i in ground_sprites:
            i.rect.x -= player.speed
        obj.rect.x -= player.speed
        counter += 1
        player.score += round(player.speed)
        all_sprites.update()
        screen.fill((128, 186, 184))
        all_sprites.draw(screen)
        pygame.display.flip()
pygame.quit()
