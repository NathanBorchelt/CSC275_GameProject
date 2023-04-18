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

            self.all_sprites.add(self.haz)

            self.all_sprites.add(self.player)
            self.obstacles.add(self.haz)
            self.lasers.add(self.haz)
            self.obstacles.add(self.haz.head)
            self.obstacles.add(self.haz.tail)
            self.all_sprites.add(self.haz.head)
            self.all_sprites.add(self.haz.tail)

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
            self.timeSinceStart = time.time() - self.startTime
            self.player.speedUpdate(1.001)

            if self.timeSinceStart > self.randomHazardSpawnTime:
                self.startTime = time.time()
                self.randomHazardSpawnTime = randint(5, 10)
                match(randint(0, 3)):
                    case _:
                        tempHaz = Gun([self.all_sprites, self.obstacles])
                        self.all_sprites.add(tempHaz)
                        self.obstacles.add(tempHaz)
            self.clock.tick(st.FPS)
            for event in pygame.event.get():
                # check for closing window
                if event.type == pygame.QUIT:
                    self.running = False
                    return False
                if event.type == pygame.KEYDOWN:
                    match (event.key):
                        case pygame.K_SPACE:
                            self.keyPressedSpace = True
                        case pygame.K_ESCAPE:
                            self.running = True
                            self.menu = True
                            self.frameCounter = 0
                            return False
                        case pygame.K_RIGHT:
                            self.keyPressedRight = True
                        case pygame.K_LEFT:
                            self.keyPressedLeft = True
                        case pygame.K_UP:
                            self.keyPressedUp = True
                        case pygame.K_DOWN:
                            self.keyPressedDown = True
                if event.type == pygame.KEYUP:
                    match (event.key):
                        case pygame.K_SPACE:
                            if len(self.bullets) < 3:
                                bullet = Bullet(self.player.rect.centerx + self.player.rect.width/2, self.player.rect.centery)
                                self.all_sprites.add(bullet)
                                self.bullets.add(bullet)
                            self.keyPressedSpace = False
                        case pygame.K_RETURN:
                            self.keyPressedSpace = False
                        case pygame.K_RIGHT:
                            self.keyPressedRight = False
                        case pygame.K_LEFT:
                            self.keyPressedLeft = False
                        case pygame.K_UP:
                            self.keyPressedUp = False
                        case pygame.K_DOWN:
                            self.keyPressedDown = False

            if self.keyPressedUp:
                self.player.vely += st.PLAYER_ACC
                if self.player.vely > 15:
                    self.player.vely = 15

                self.player.flying = True
            elif self.keyPressedDown:
                self.player.vely -= st.PLAYER_ACC
                if self.player.vely < -15:
                    self.player.vely = -15
                self.player.flying = False
            else:
                self.player.vely *= 15/16
                self.player.flying = False
            if self.keyPressedLeft:
                self.player.velx -= st.PLAYER_ACC
                if self.player.velx < -15:
                    self.player.velx = -15
            elif self.keyPressedRight:
                self.player.velx += st.PLAYER_ACC
                if self.player.velx > 15:
                    self.player.velx = 15
            else:
                self.player.velx *= 15/16
            self.player.rect.y -= self.player.vely
            self.player.rect.x += self.player.velx

            if self.player.rect.top > st.SCREEN_HEIGHT:
                self.player.rect.bottom = 0
            if self.player.rect.bottom < 0:
                self.player.rect.top = st.SCREEN_HEIGHT
            if self.player.rect.left < 0:
                self.player.rect.left = 0
            if self.player.rect.right > st.SCREEN_WIDTH:
                self.player.rect.right = st.SCREEN_WIDTH

            for warning in self.warnings:
                warning.rect.y += (self.player.rect.y - warning.rect.y)/60
            if time.time() - self.missleStartTime > self.missleInterval:
                self.missleStartTime = time.time()
                self.missleInterval = randint(5, 7)
                warning = MissleWarning(randint(0, st.SCREEN_HEIGHT))
                self.all_sprites.add(warning)
                self.warnings.add(warning)

            for warning in self.warnings:
                if warning.spawn > 3:
                    missle = Missle(warning.rect.y)
                    self.obstacles.add(missle)
                    self.missles.add(missle)
                    self.all_sprites.add(missle)
                    warning.kill()

            for i in self.obstacles:
                if abs(i.rect.x - self.player.rect.x) < 150:
                    if pygame.sprite.collide_mask(self.player, i):
                            self.new()
                            with open("highscore.txt", 'w') as file:
                                file.write(str(self.highscore))
                for bul in self.bullets:
                    if abs(i.rect.x - bul.rect.x) < 150:
                        if pygame.sprite.collide_mask(bul, i):
                            if i in self.lasers:
                                i.image = pygame.image.load("res/transparent.png").convert_alpha()
                                self.obstacles.remove(i.head)
                                self.obstacles.remove(i.tail)
                            elif type(i) == LazerEnd:
                                i.parent.image = pygame.image.load("res/transparent.png").convert_alpha()
                            else:
                                i.image = pygame.image.load("res/transparent.png").convert_alpha()
                            bul.kill()



            if int(self.score/300) > self.highscore:
                self.highscore = int(self.score/300)

            for i in self.lasers:
                spawnPlatform = i.rect.centerx < st.SCREEN_WIDTH/2
                if spawnPlatform and i.mother:
                    i.mother = False
                    self.haz2 = Hazard(True, 0)
                    self.lasers.add(self.haz2)
                    self.obstacles.add(self.haz2)
                    self.all_sprites.add(self.haz2)
                    self.obstacles.add(self.haz2.head)
                    self.obstacles.add(self.haz2.tail)
                    self.all_sprites.add(self.haz2.head)
                    self.all_sprites.add(self.haz2.tail)
                    if (bool(randint(0,1))):
                        self.haz3 = Hazard(False, randint(200 , round(st.SCREEN_WIDTH/4 )*2))
                        self.lasers.add(self.haz3)
                        self.obstacles.add(self.haz3)
                        self.all_sprites.add(self.haz3)
                        self.obstacles.add(self.haz3.head)
                        self.obstacles.add(self.haz3.tail)
                        self.all_sprites.add(self.haz3.head)
                        self.all_sprites.add(self.haz3.tail)

            text_surface = self.font.render(str(int(self.score/300)) + " M", True, (0,0,0))
            highscore_surface = self.font.render("Highscore " + str(self.highscore) + " M", True, (0, 0, 0))
            self.score += st.playerSpeed
            self.all_sprites.update()
            self.screen.fill((50, 50, 200))
            self.all_sprites.draw(self.screen)
            self.screen.blit(text_surface, (25, 25))
            self.screen.blit(highscore_surface, (25, 75))
            pygame.display.flip()
            self.frameCounter += 1
            return True


g = Game()
g.load()
g.new()
g.execution()

pygame.quit()
