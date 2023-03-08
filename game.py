import pygame
import pickle
import time
from Player import *
<<<<<<< HEAD

WIDTH = 1600
HEIGHT = 900
FPS = 60
#define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


=======
        
>>>>>>> 62e5c09181ea809694a2592ddd1ae0df530bc7fc
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
haz = Hazard(200, True,0,randint(0,3))
all_sprites.add(ground)
all_sprites.add(ground1)
all_sprites.add(ground2)
all_sprites.add(ground3)
all_sprites.add(ground4)
all_sprites.add(haz)
ground_sprites.add(ground)
ground_sprites.add(ground1)
ground_sprites.add(ground2)
ground_sprites.add(ground3)
ground_sprites.add(ground4)
all_sprites.add(player)
obstacles.add(haz)
startTime = time.time()
counter = 0
font = pygame.font.Font('res/New Athletic M54.ttf', 36)
score = 0


while running:
    while game:
        timeSinceStart = time.time() - startTime
        if timeSinceStart > 1 and counter == 0:
            st.playerSpeed += 4
            counter += 1
        if timeSinceStart > 2 and counter == 1:
            st.playerSpeed += 4
            counter += 1
        if timeSinceStart > 3 and counter == 2:
            st.playerSpeed += 4
            counter += 1
        if timeSinceStart > 4 and counter == 3:
            st.playerSpeed += 4
            counter += 1
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
                    st.playerSpeed += 4
                if event.key == pygame.K_LEFT:
                    st.playerSpeed -= 4
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
<<<<<<< HEAD
                    keyDownSpace = False
=======
                    keyDownSpace = False       

>>>>>>> 62e5c09181ea809694a2592ddd1ae0df530bc7fc
        if keyDownSpace:
            player.acc = st.PLAYER_ACC
            player.changeImage("res/jetOn.png")
        else:
<<<<<<< HEAD
            player.acc = -1
        player.vel += player.acc
=======
            player.changeImage("res/jet.png")
            player.acc = -st.PLAYER_ACC
        player.vel += player.acc 
>>>>>>> 62e5c09181ea809694a2592ddd1ae0df530bc7fc
        player.rect.y -= player.vel

        if player.rect.bottom > 750:
            player.rect.bottom = 750
            player.vel = 0
        if player.rect.top < 0:
            player.rect.top = 0
            player.vel = 0

        for i in obstacles:
            if pygame.sprite.collide_mask(player, i):
                running = False
                game = False
<<<<<<< HEAD
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
=======
            if abs(i.rect.centerx - player.rect.centerx) < st.playerSpeed/2+10 and i.mother:
                i.mother = False
                haz2 = Hazard(randint(75, 125)*2, True, 0, randint(0,3))
                obstacles.add(haz2)
                all_sprites.add(haz2)
                if (bool(randint(0,1))):    
                    haz3 = Hazard(randint(75, 125)*2, False, randint(200 , round(WIDTH/4 )*2), randint(0, 3))   
                    obstacles.add(haz3)
                    all_sprites.add(haz3)  

        if ground.startPos - ground.rect.x >= 400.0:
            ground.rect.x = ground.startPos 
            ground1.rect.x = ground1.startPos 
            ground2.rect.x = ground2.startPos 
            ground3.rect.x = ground3.startPos 
            ground4.rect.x = ground4.startPos 
        for i in ground_sprites:
            i.rect.x -= st.playerSpeed
        
        text_surface = font.render(str(int(score/300)) + " M", True, (0,0,0))
        score += st.playerSpeed
        all_sprites.update()       
>>>>>>> 62e5c09181ea809694a2592ddd1ae0df530bc7fc
        screen.fill((128, 186, 184))
        all_sprites.draw(screen)
        screen.blit(text_surface, (25, 25))
        pygame.display.flip()
pygame.quit()