import pygame
from Player import *

WIDTH = 1600
HEIGHT = 900
FPS = 60
SPEED = 10
PLAYER_ACC = 1
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
                if event.key == pygame.K_ESCAPE:
                    running = False
                    game = False
                if event.key == pygame.K_RIGHT:
                    for i in obstacles:
                        i.speed += 1
                if event.key == pygame.K_LEFT:
                    for i in obstacles:
                        i.speed -=1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    keyDownSpace = False       
        if keyDownSpace:
            player.acc = PLAYER_ACC
            player.changeImage("res/jetOn.png")
        else:
            player.changeImage("res/jet.png")
            player.acc = -PLAYER_ACC
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
        if counter >= 20:
            for i in ground_sprites:
                i.rect.x += 400
                counter = 0
        for i in ground_sprites:
            i.rect.x -= 20
        counter += 1
        all_sprites.update()       
        screen.fill((128, 186, 184))
        all_sprites.draw(screen)
        pygame.display.flip()
pygame.quit()
