import pygame
<<<<<<< HEAD
import random
import MenuEntities
import Player
import array

WIDTH = 1600
HEIGHT = 900
FPS = 30
#define colors
WHITE = (220,220,220)
BLACK = (30,30,30)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


=======
import time
from Player import *
        
>>>>>>> alec
# initialize pygame and create window
pygame.init()
pygame.mixer.init()  
screen = pygame.display.set_mode((st.SCREEN_WIDTH, st.SCREEN_HEIGHT))
pygame.display.set_caption("Joypack Jetride")
clock = pygame.time.Clock()
#create sprite group and add the player sprite to it
all_sprites = pygame.sprite.Group()
<<<<<<< HEAD
menuCursor = MenuEntities.MenuCursor()
startButton = MenuEntities.MenuButton(HEIGHT/2, "res/startText.png")
endButton = MenuEntities.MenuButton(HEIGHT/2+80, "res/endText.png")

all_sprites.add(menuCursor)
all_sprites.add(startButton)
all_sprites.add(endButton)
prevCursorPos = [Player.Vector2f(750, 750)]


#Game loop
running = True
game = False
menu = True
follow = False
deleteEnd = False
x = 0
=======
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
timeCounter = 0
font = pygame.font.Font('res/New Athletic M54.ttf', 36)
score = 0

with open("highscore.txt", "r") as file:
    try:
        highscore = int(file.readline())
    except:
        highscore = 0

startGame = pygame.image.load("res/menuFrame.png").convert_alpha()
startGame = pygame.transform.scale_by(startGame, st.SCREEN_WIDTH/st.BASE_WIDTH)
cursor = Cursor(st.SCREEN_WIDTH/2, st.SCREEN_HEIGHT/2)
cursorGroup = pygame.sprite.Group()
cursorGroup.add(cursor)
>>>>>>> alec

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
<<<<<<< HEAD
                if event.key == pygame.K_w:
                    menuCursor.rect.y -= 80
                if event.key == pygame.K_s:
                    menuCursor.rect.y += 80
                if event.key == pygame.K_SPACE:
                    if menuCursor.rect.y == startButton.rect.y:
                        menu = False
                        game = True
                        all_sprites.empty()
                        player = Player.Player()
                        cursor = Player.Cursor()
                        all_sprites.add(player)
                        all_sprites.add(cursor)
                    if menuCursor.rect.y == endButton.rect.y:
                        running = False
                        menu = False
        screen.fill(BLACK)
        all_sprites.update()

        all_sprites.draw(screen)
=======
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
>>>>>>> alec
        pygame.display.flip()

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
<<<<<<< HEAD
                if event.key == pygame.K_w:
                    cursor.pos.y -= 100
                elif event.key == pygame.K_a:
                    cursor.pos.x -= 100
                elif event.key == pygame.K_s:
                    cursor.pos.y += 100
                elif event.key == pygame.K_d:
                    cursor.pos.x += 100
                elif event.key == pygame.K_SPACE:
                    follow = True
                elif event.key == pygame.K_ESCAPE:
                    running = False
                    game = False
        if len(prevCursorPos) == 0:
            posx = cursor.pos.x
            posy = cursor.pos.y
            prevCursorPos.append(Player.Vector2f(posx, posy))
            follow = False
        if (cursor.pos.x != prevCursorPos[len(prevCursorPos) - 1].x or cursor.pos.y != prevCursorPos[len(prevCursorPos) - 1].y):
            posx = cursor.pos.x
            posy = cursor.pos.y
            prevCursorPos.append(Player.Vector2f(posx, posy))
            x = len(prevCursorPos)
            for i in prevCursorPos:
                if prevCursorPos[len(prevCursorPos) - 1].x == i.x and prevCursorPos[len(prevCursorPos) - 1].y == i.y:
                    x = prevCursorPos.index(i)+1
                    deleteEnd = True
            if deleteEnd:
                while x < len(prevCursorPos):
                    prevCursorPos.pop()
                deleteEnd = False
        print(x)
        if follow:
            player.setPos(prevCursorPos[0])
            del prevCursorPos[0]
        all_sprites.update()
        screen.fill(BLACK)
        boardImage = pygame.image.load("res/chessBoard.png")
        boardImage = pygame.transform.scale(boardImage, (800,800))
        screen.blit(boardImage, (400, 0))
=======
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
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    keyDownSpace = False       

        if keyDownSpace:
            player.acc = st.PLAYER_ACC
            player.changeImage("res/jetOn.png")
        else:
            player.changeImage("res/jet.png")
            player.acc = -st.PLAYER_ACC
        player.vel += player.acc 
        player.rect.y -= player.vel

        if player.rect.bottom > st.SCREEN_HEIGHT - ground.rect.height*2/3:
            player.rect.bottom = st.SCREEN_HEIGHT - ground.rect.height*2/3
            player.vel = 0
        if player.rect.top < 0:
            player.rect.top = 0
            player.vel = 0

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
            

        for i in obstacles:
            if pygame.sprite.collide_mask(player, i):
                running = False
                game = False
                with open("highscore.txt", 'w') as file:
                        file.write(str(highscore))
        if int(score/300) > highscore:
            highscore = int(score/300)
                           

        for i in lasers:
            spawnPlatform = abs(i.rect.centerx - player.rect.centerx) < st.playerSpeed/2+10
            if spawnPlatform and i.mother:
                i.mother = False
                haz2 = Hazard(randint(75, 125)*2, True, 0, randint(0,3))
                lasers.add(haz2)
                obstacles.add(haz2)
                all_sprites.add(haz2)
                if (bool(randint(0,1))):    
                    haz3 = Hazard(randint(75, 125)*2, False, randint(200 , round(st.SCREEN_WIDTH/4 )*2), randint(0, 3))   
                    lasers.add(haz3)
                    obstacles.add(haz3)
                    all_sprites.add(haz3)  

        resetGround = ground.startPos - ground.rect.x >= ground.rect.width
        if resetGround:
            ground.rect.x = ground.startPos 
            ground1.rect.x = ground1.startPos 
            ground2.rect.x = ground2.startPos 
            ground3.rect.x = ground3.startPos 
            ground4.rect.x = ground4.startPos 
        for i in ground_sprites:
            i.rect.x -= st.playerSpeed
        
        text_surface = font.render(str(int(score/300)) + " M", True, (0,0,0))
        highscore_surface = font.render("Highscore " + str(highscore) + " M", True, (0, 0, 0))
        score += st.playerSpeed
        all_sprites.update()       
        screen.fill((128, 186, 184))
>>>>>>> alec
        all_sprites.draw(screen)
        screen.blit(text_surface, (25, 25))
        screen.blit(highscore_surface, (25, 75))
        pygame.display.flip()
<<<<<<< HEAD
pygame.quit()
=======
pygame.quit()
>>>>>>> alec
