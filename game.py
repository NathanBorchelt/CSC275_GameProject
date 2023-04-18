import pygame
import time
from Player import *



class Game:
        def __init__(self):
            # initialize pygame and create window
            pygame.init()
            pygame.mixer.init()
            self.screen = pygame.display.set_mode((st.SCREEN_WIDTH,st.SCREEN_HEIGHT))
            pygame.display.set_caption("Joypack Jetride")
            self.clock = pygame.time.Clock()

            #all sprite groups


            #menu logic
            self.running = True
            self.game = False
            self.menu = True

            #movement binaries
            self.keyPressedSpace = False
            self.keyPressedUp = False
            self.keyPressedLeft = False
            self.keyPressedDown = False
            self.keyPressedRight = False

        def load(self):
            with open("highscore.txt", "r") as file:
                try:
                    self.highscore = int(file.readline())
                except:
                    self.highscore = 0

        def new(self):
            self.all_sprites = pygame.sprite.Group()
            self.ground_sprites = pygame.sprite.Group()
            self.lasers = pygame.sprite.Group()
            self.obstacles = pygame.sprite.Group()
            self.warnings = pygame.sprite.Group()
            self.missles = pygame.sprite.Group()
            self.bullets = pygame.sprite.Group()
            self.player = Player()
            self.haz = Hazard(True,0)

            self.all_sprites.add(haz)

            self.all_sprites.add(player)
            self.obstacles.add(haz)
            self.lasers.add(haz)
            self.obstacles.add(haz.head)
            self.obstacles.add(haz.tail)
            self.all_sprites.add(haz.head)
            self.all_sprites.add(haz.tail)

#Game loop
            self.timeCounter = 0
            self.font = pygame.font.Font('res/New Athletic M54.ttf', 36)
            self.score = 0
            self.frameCounter = 0
            self.randomHazardSpawnTime = 7



            self.startGame = pygame.image.load("res/menu/menuFrame.png").convert_alpha()
            self.startGame = pygame.transform.scale_by(self.startGame, st.scaleFactor)
            self.cursor = Cursor(st.SCREEN_WIDTH/2, st.SCREEN_HEIGHT/2)
            self.cursorGroup = pygame.sprite.Group()
            self.cursorGroup.add(self.cursor)

            self.menu = True
            self.running = True
            self.game = False

        def execution(self):
            while self.running:
                while self.menu:
                    self.menu = self.menuLoop()
                while self.game:
                    self.game = self.run()

        def menuLoop(self):
            for event in pygame.event.get():
                # check for closing window
                if event.type == pygame.QUIT:
                    self.running = False
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        self.keyPressedSpace = True
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        return False
                    if event.key == pygame.K_UP:
                        self.cursor.rect.y -= 1.5 * self.startGame.get_height()
                    if event.key == pygame.K_DOWN:
                        self.cursor.rect.y += 1.5 * self.startGame.get_height()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        self.keyPressedSpace = False

            if self.cursor.rect.centery < st.SCREEN_HEIGHT/2:
                self.cursor.rect.centery = st.SCREEN_HEIGHT/2
            elif self.cursor.rect.centery > st.SCREEN_HEIGHT/2 + 3 * self.startGame.get_height():
                self.cursor.rect.centery = st.SCREEN_HEIGHT/2 + 3 * self.startGame.get_height()

            if self.keyPressedSpace:
                if self.cursor.rect.centery <= st.SCREEN_HEIGHT/2:
                    self.startTime = time.time()
                    self.missleStartTime = time.time()
                    self.missleInterval = randint(3, 7)
                    self.game = True
                    return False

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.startGame, (st.SCREEN_WIDTH/2 - self.startGame.get_width()/2, st.SCREEN_HEIGHT/2 - self.startGame.get_height()/2))
            self.screen.blit(self.startGame, (st.SCREEN_WIDTH/2 - self.startGame.get_width()/2, st.SCREEN_HEIGHT/2 + self.startGame.get_height()))
            self.screen.blit(self.startGame, (st.SCREEN_WIDTH/2 - self.startGame.get_width()/2, st.SCREEN_HEIGHT/2 + self.startGame.get_height()* 2.5))
            self.cursorGroup.draw(self.screen)
            pygame.display.flip()
            return True

        def run(self):
            self.timeSinceStart = time.time() - startTime
            self.player.speedUpdate(1)

            if self.timeSinceStart > self.randomHazardSpawnTime:
                self.startTime = time.time()
            self.randomHazardSpawnTime = randint(5, 10)
            match(randint(0, 3)):
                case _:
                    tempHaz = Gun([self.all_sprites, self.obstacles])
                    self.all_sprites.add(tempHaz)
                    self.obstacles.add(tempHaz)
            self.clock.tick(st.FPS)

while running:


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
