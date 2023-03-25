import pygame
import pickle
import time
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
lasers = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
warnings = pygame.sprite.Group()
missles = pygame.sprite.Group()
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
lasers.add(haz)
startTime = time.time()
missleStartTime = time.time()
missleInterval = randint(3, 7)
timeCounter = 0
font = pygame.font.Font('res/New Athletic M54.ttf', 36)
score = 0

with open("highscore.txt", "r") as file:
    highscore = int(file.readline())

print(highscore)


while running:
    while game:
        timeSinceStart = time.time() - startTime
        if timeSinceStart > 1 and timeCounter == 0:
            st.playerSpeed += 4
            timeCounter += 1
        if timeSinceStart > 2 and timeCounter == 1:
            st.playerSpeed += 4
            timeCounter += 1
        if timeSinceStart > 3 and timeCounter == 2:
            st.playerSpeed += 4
            timeCounter += 1
        if timeSinceStart > 4 and timeCounter == 3:
            st.playerSpeed += 4
            timeCounter += 1
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

        for warning in warnings:
            warning.rect.y += (player.rect.y - warning.rect.y)/100
        if time.time() - missleStartTime > missleInterval:
            missleStartTime = time.time()
            missleInterval = randint(3, 7)
            warning = MissleWarning(randint(0, HEIGHT))
            all_sprites.add(warning)
            warnings.add(warning)

        for warning in warnings:
            if warning.spawn > 3: 
                missle = Missle(warning.rect.y)
                obstacles.add(missle)
                missles.add(missle)
                all_sprites.add(missle)
                warning.kill()
            

        for i in obstacles:
            if pygame.sprite.collide_mask(player, i):
                running = False
                game = False
                if int(score/300) > highscore:
                    with open("highscore.txt", 'w') as file:
                        file.write(str(int(score/300)))
                

        for i in lasers:
            spawnPlatform = abs(i.rect.centerx - player.rect.centerx) < st.playerSpeed/2+10
            if spawnPlatform and i.mother:
                i.mother = False
                haz2 = Hazard(randint(75, 125)*2, True, 0, randint(0,3))
                lasers.add(haz2)
                obstacles.add(haz2)
                all_sprites.add(haz2)
                if (bool(randint(0,1))):    
                    haz3 = Hazard(randint(75, 125)*2, False, randint(200 , round(WIDTH/4 )*2), randint(0, 3))   
                    lasers.add(haz3)
                    obstacles.add(haz3)
                    all_sprites.add(haz3)  

        resetGround = ground.startPos - ground.rect.x >= 400
        if resetGround:
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
        screen.fill((128, 186, 184))
        all_sprites.draw(screen)
        screen.blit(text_surface, (25, 25))
        pygame.display.flip()
pygame.quit()