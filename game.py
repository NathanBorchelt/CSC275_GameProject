import pygame
import pickle
from Player import *
        
# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((st.WIDTH, st.HEIGHT))
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
counter2 = 0

while running:
    while game:
        clock.tick(st.FPS)
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
                    counter2 += 1
                if event.key == pygame.K_LEFT:
                    counter2 -=1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    keyDownSpace = False       
        if keyDownSpace:
            player.acc = st.PLAYER_ACC
            player.changeImage("res/jetOn.png")
        else:
            player.changeImage("res/jet.png")
            player.acc = -st.PLAYER_ACC
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
        if counter >= 400.0/st.playerSpeed+.01:
            ground.rect.x = ground.startPos 
            ground1.rect.x = ground1.startPos 
            ground2.rect.x = ground2.startPos 
            ground3.rect.x = ground3.startPos 
            ground4.rect.x = ground4.startPos 
            counter = 0
            st.playerSpeed += counter2
            counter2 = 0
        for i in ground_sprites:
            i.rect.x -= st.playerSpeed
        counter += 1
        all_sprites.update()       
        screen.fill((128, 186, 184))
        all_sprites.draw(screen)
        pygame.display.flip()
pygame.quit()
