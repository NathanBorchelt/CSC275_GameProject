import pygame
<<<<<<< HEAD
import pickle
import time
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
screen = pygame.display.set_mode((st.WIDTH, st.HEIGHT))
=======
import time
from Player import *

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((st.SCREEN_WIDTH, st.SCREEN_HEIGHT))
>>>>>>> main
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
game = False
menu = True
keyDownSpace = False
ground = Ground(0)
ground1 = Ground(st.SCREEN_WIDTH/4)
ground2 = Ground(st.SCREEN_WIDTH/2)
ground3 = Ground(st.SCREEN_WIDTH*3/4)
ground4 = Ground(st.SCREEN_WIDTH)
player = Player()
<<<<<<< HEAD
haz = Hazard(200, True,0,randint(0,3))
=======
haz = Hazard(True,0)
>>>>>>> main
all_sprites.add(ground)
all_sprites.add(ground1)
all_sprites.add(ground2)
all_sprites.add(ground3)
all_sprites.add(ground4)
all_sprites.add(haz)
<<<<<<< HEAD
=======
all_sprites.add(haz.head)
all_sprites.add(haz.tail)
>>>>>>> main
ground_sprites.add(ground)
ground_sprites.add(ground1)
ground_sprites.add(ground2)
ground_sprites.add(ground3)
ground_sprites.add(ground4)
all_sprites.add(player)
obstacles.add(haz)
<<<<<<< HEAD
startTime = time.time()
counter = 0
font = pygame.font.Font('res/New Athletic M54.ttf', 36)
score = 0

=======
obstacles.add(haz.head)
obstacles.add(haz.tail)
lasers.add(haz)
timeCounter = 0
font = pygame.font.Font('res/New Athletic M54.ttf', 36)
score = 0
frameCounter = 0
#jetpackSound = pygame.mixer.Sound("jetpack.wav")
#jetpackSound.play()

with open("highscore.txt", "r") as file:
    try:
        highscore = int(file.readline())
    except:
        highscore = 0

startGame = pygame.image.load("res/menu/menuFrame.png").convert_alpha()
startGame = pygame.transform.scale_by(startGame, st.scaleFactor)
cursor = Cursor(st.SCREEN_WIDTH/2, st.SCREEN_HEIGHT/2)
cursorGroup = pygame.sprite.Group()
cursorGroup.add(cursor)
>>>>>>> main

while running:
    while menu:
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
                menu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    keyDownSpace = True
                if event.key == pygame.K_ESCAPE:
                    running = False
                    menu = False
                if event.key == pygame.K_UP:
                    cursor.rect.y -= 1.5 * startGame.get_height()
                if event.key == pygame.K_DOWN:
                    cursor.rect.y += 1.5 * startGame.get_height()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    keyDownSpace = False

        if cursor.rect.centery < st.SCREEN_HEIGHT/2:
            cursor.rect.centery = st.SCREEN_HEIGHT/2
        elif cursor.rect.centery > st.SCREEN_HEIGHT/2 + 3 * startGame.get_height():
            cursor.rect.centery = st.SCREEN_HEIGHT/2 + 3 * startGame.get_height()

        if keyDownSpace:
            if cursor.rect.centery <= st.SCREEN_HEIGHT/2:
                menu = False
                game = True
                startTime = time.time()
                missleStartTime = time.time()
                missleInterval = randint(3, 7)

        screen.fill((0, 0, 0))
        screen.blit(startGame, (st.SCREEN_WIDTH/2 - startGame.get_width()/2, st.SCREEN_HEIGHT/2 - startGame.get_height()/2))
        screen.blit(startGame, (st.SCREEN_WIDTH/2 - startGame.get_width()/2, st.SCREEN_HEIGHT/2 + startGame.get_height()))
        screen.blit(startGame, (st.SCREEN_WIDTH/2 - startGame.get_width()/2, st.SCREEN_HEIGHT/2 + startGame.get_height()* 2.5))
        cursorGroup.draw(screen)
        pygame.display.flip()

    while game:
        timeSinceStart = time.time() - startTime
<<<<<<< HEAD
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
=======
        #player.speedUpdate()
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
>>>>>>> main
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
<<<<<<< HEAD
                    running = False
                    game = False
=======
                    running = True
                    menu = True
                    game = False
                    frameCounter = 0
>>>>>>> main
                if event.key == pygame.K_RIGHT:
                    st.playerSpeed += 4
                if event.key == pygame.K_LEFT:
                    st.playerSpeed -= 4
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    keyDownSpace = False

<<<<<<< HEAD

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
=======
        if keyDownSpace:

            player.jetpackImage = pygame.image.load(f"res/jetpack/jetpack{int(frameCounter % 40 / 10) + 1}.png")
            player.acc = st.PLAYER_ACC
            player.flying = True
        else:
            player.jetpackImage = pygame.image.load("res/jetpack/jetpack0.png")
            player.acc = -st.PLAYER_ACC
            player.flying = False
        player.jetpackImage = pygame.transform.scale_by(player.jetpackImage, st.scaleFactor)
        player.vel += player.acc
        player.rect.y -= player.vel

        if player.rect.bottom >= st.SCREEN_HEIGHT - ground.rect.height*2/3:
            player.rect.bottom = st.SCREEN_HEIGHT - ground.rect.height*2/3
>>>>>>> main
            player.vel = 0
        if player.rect.top < 0:
            player.rect.top = 0
            player.vel = 0

<<<<<<< HEAD
=======
        if(random() < .1):
            vehicle = VehicleSpawn()
            all_sprites.add(vehicle)


        for warning in warnings:
            warning.rect.y += (player.rect.y - warning.rect.y)/60
        if time.time() - missleStartTime > missleInterval:
            missleStartTime = time.time()
            missleInterval = randint(5, 7)
            warning = MissleWarning(randint(0, st.SCREEN_HEIGHT))
            all_sprites.add(warning)
            warnings.add(warning)

        for warning in warnings:
            if warning.spawn > 3:
                missle = Missle(warning.rect.y)
                obstacles.add(missle)
                missles.add(missle)
                all_sprites.add(missle)
                warning.kill()


>>>>>>> main
        for i in obstacles:
            if pygame.sprite.collide_mask(player, i):
                running = False
                game = False
<<<<<<< HEAD
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
=======
                with open("highscore.txt", 'w') as file:
                        file.write(str(highscore))
        if int(score/300) > highscore:
            highscore = int(score/300)

        #for i in missles:
        #    i.image = pygame.image.load(f"res/hazards/missle{int(frameCounter % 60 / 10)}.png").convert_alpha()

        for i in lasers:
            spawnPlatform = abs(i.rect.centerx - player.rect.centerx) < st.playerSpeed/2+10
            if spawnPlatform and i.mother:
                i.mother = False
                haz2 = Hazard(True, 0)
                lasers.add(haz2)
                obstacles.add(haz2)
                obstacles.add(haz2.head)
                obstacles.add(haz2.tail)
                all_sprites.add(haz2)
                all_sprites.add(haz2.head)
                all_sprites.add(haz2.tail)
                if (bool(randint(0,1))):
                    haz3 = Hazard(False, randint(200 , round(st.SCREEN_WIDTH/4 )*2))
                    lasers.add(haz3)
                    obstacles.add(haz3)
                    obstacles.add(haz3.head)
                    obstacles.add(haz3.tail)
                    all_sprites.add(haz3)
                    all_sprites.add(haz3.head)
                    all_sprites.add(haz3.tail)

        resetGround = ground.startPos - ground.rect.x >= ground.rect.width
        if resetGround:
>>>>>>> main
            ground.rect.x = ground.startPos
            ground1.rect.x = ground1.startPos
            ground2.rect.x = ground2.startPos
            ground3.rect.x = ground3.startPos
            ground4.rect.x = ground4.startPos
        for i in ground_sprites:
            i.rect.x -= st.playerSpeed

        text_surface = font.render(str(int(score/300)) + " M", True, (0,0,0))
<<<<<<< HEAD
=======
        highscore_surface = font.render("Highscore " + str(highscore) + " M", True, (0, 0, 0))
>>>>>>> main
        score += st.playerSpeed
        all_sprites.update()
        screen.fill((120, 120, 0))
        all_sprites.draw(screen)
<<<<<<< HEAD
        screen.blit(text_surface, (25, 25))
=======
        screen.blit(player.jetpackImage, (player.rect.centerx - 1.8* player.rect.width, player.rect.y + player.rect.height/10))
        screen.blit(text_surface, (25, 25))
        screen.blit(highscore_surface, (25, 75))
>>>>>>> main
        pygame.display.flip()
        frameCounter += 1
pygame.quit()
