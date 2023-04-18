import pygame
import time
from Player import *

        
# initialize pygame and create window
pygame.init()
pygame.mixer.init()  
screen = pygame.display.set_mode((st.SCREEN_WIDTH, st.SCREEN_HEIGHT))
pygame.display.set_caption("Joypack Jetride")
clock = pygame.time.Clock()
#create sprite group and add the player sprite to it
all_sprites = pygame.sprite.Group()
ground_sprites = pygame.sprite.Group()
lasers = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
warnings = pygame.sprite.Group()
missles = pygame.sprite.Group()
bullets = pygame.sprite.Group()
#Game loop
running = True
game = False
menu = True
keyPressedSpace = False
keyPressedUp = False
keyPressedLeft = False
keyPressedDown = False
keyPressedRight = False

player = Player()
haz = Hazard(True,0)

all_sprites.add(haz)

all_sprites.add(player)
obstacles.add(haz)
lasers.add(haz)
obstacles.add(haz.head)
obstacles.add(haz.tail)
all_sprites.add(haz.head)
all_sprites.add(haz.tail)
timeCounter = 0
font = pygame.font.Font('res/New Athletic M54.ttf', 36)
score = 0
frameCounter = 0
randomHazardSpawnTime = 7

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

while running:
    while menu: 
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
                menu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    keyPressedSpace = True
                if event.key == pygame.K_ESCAPE:
                    running = False
                    menu = False
                if event.key == pygame.K_UP:
                    cursor.rect.y -= 1.5 * startGame.get_height()
                if event.key == pygame.K_DOWN:
                    cursor.rect.y += 1.5 * startGame.get_height()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    keyPressedSpace = False  
            
        if cursor.rect.centery < st.SCREEN_HEIGHT/2:
            cursor.rect.centery = st.SCREEN_HEIGHT/2
        elif cursor.rect.centery > st.SCREEN_HEIGHT/2 + 3 * startGame.get_height():
            cursor.rect.centery = st.SCREEN_HEIGHT/2 + 3 * startGame.get_height()

        if keyPressedSpace:
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
        player.speedUpdate(1)
        
        if timeSinceStart > randomHazardSpawnTime:
            startTime = time.time()
            randomHazardSpawnTime = randint(5, 10)
            match(randint(0, 3)):
                case _:
                    tempHaz = Gun([all_sprites, obstacles])
                    all_sprites.add(tempHaz)
                    obstacles.add(tempHaz)
        clock.tick(st.FPS)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
                game = False
            if event.type == pygame.KEYDOWN:
                match (event.key):
                    case pygame.K_SPACE:
                        keyPressedSpace = True
                    case pygame.K_ESCAPE:
                        running = True
                        menu = True
                        game = False
                        frameCounter = 0
                    case pygame.K_RIGHT:
                        keyPressedRight = True
                    case pygame.K_LEFT:
                        keyPressedLeft = True
                    case pygame.K_UP:
                        keyPressedUp = True
                    case pygame.K_DOWN:
                        keyPressedDown = True
            if event.type == pygame.KEYUP:
                match (event.key):
                    case pygame.K_SPACE:
                        if len(bullets) < 3:
                            bullet = Bullet(player.rect.centerx + player.rect.width/2, player.rect.centery)
                            all_sprites.add(bullet)
                            bullets.add(bullet)
                        keyPressedSpace = False       
                    case pygame.K_RETURN:
                        keyPressedSpace = False
                    case pygame.K_RIGHT:
                        keyPressedRight = False
                    case pygame.K_LEFT:
                        keyPressedLeft = False
                    case pygame.K_UP:
                        keyPressedUp = False
                    case pygame.K_DOWN:
                        keyPressedDown = False

        if keyPressedUp:
            player.vely += st.PLAYER_ACC
            if player.vely > 15:
                player.vely = 15
            
            player.flying = True           
        elif keyPressedDown:
            player.vely -= st.PLAYER_ACC
            if player.vely < -15:
                player.vely = -15
            player.flying = False
        else:
            player.vely *= 15/16
            player.flying = False
        if keyPressedLeft:
            player.velx -= st.PLAYER_ACC
            if player.velx < -15:
                player.velx = -15
        elif keyPressedRight:
            player.velx += st.PLAYER_ACC
            if player.velx > 15:
                player.velx = 15
        else:
            player.velx *= 15/16
        player.rect.y -= player.vely
        player.rect.x += player.velx

        if player.rect.top > st.SCREEN_HEIGHT:
            player.rect.bottom = 0
        if player.rect.bottom < 0:
            player.rect.top = st.SCREEN_HEIGHT
        if player.rect.left < 0:
            player.rect.left = 0
        if player.rect.right > st.SCREEN_WIDTH:
            player.rect.right = st.SCREEN_WIDTH

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
            for bul in bullets:
                if pygame.sprite.collide_mask(bul, i):
                    if i in lasers:
                        i.image = pygame.image.load("res/transparent.png").convert_alpha()
                        obstacles.remove(i.head)
                        obstacles.remove(i.tail)
                    elif type(i) == LazerEnd:
                        i.parent.image = pygame.image.load("res/transparent.png").convert_alpha()
                    else:
                        i.image = pygame.image.load("res/transparent.png").convert_alpha()
                    bul.kill()



        if int(score/300) > highscore:
            highscore = int(score/300)
            
        for i in lasers:
            spawnPlatform = i.rect.centerx < st.SCREEN_WIDTH/2
            if spawnPlatform and i.mother:
                i.mother = False
                haz2 = Hazard(True, 0)
                lasers.add(haz2)
                obstacles.add(haz2)
                all_sprites.add(haz2)
                obstacles.add(haz2.head)
                obstacles.add(haz2.tail)
                all_sprites.add(haz2.head)
                all_sprites.add(haz2.tail)
                if (bool(randint(0,1))):    
                    haz3 = Hazard(False, randint(200 , round(st.SCREEN_WIDTH/4 )*2))   
                    lasers.add(haz3)
                    obstacles.add(haz3)
                    all_sprites.add(haz3)
                    obstacles.add(haz3.head)
                    obstacles.add(haz3.tail)
                    all_sprites.add(haz3.head)
                    all_sprites.add(haz3.tail)
        
        text_surface = font.render(str(int(score/300)) + " M", True, (0,0,0))
        highscore_surface = font.render("Highscore " + str(highscore) + " M", True, (0, 0, 0))
        score += st.playerSpeed
        all_sprites.update() 
        screen.fill((50, 50, 200))
        all_sprites.draw(screen)
        screen.blit(text_surface, (25, 25))
        screen.blit(highscore_surface, (25, 75))
        pygame.display.flip()
        frameCounter += 1
pygame.quit()