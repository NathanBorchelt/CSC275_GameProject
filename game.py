import pygame
import time
from Player import *
import pickle



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
            with open("highscore.bin", "rb") as file:
                try:
                    self.highscore = pickle.loads(file.readline())
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
            self.starsGroup = []
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
            self.keyPressedUp = False
            self.keyPressedDown = False
            self.keyPressedLeft = False
            self.keyPressedRight = False
            self.keyPressedSpace = False

            self.title = pygame.image.load("res/menu/title.png").convert_alpha()
            self.title = pygame.transform.scale2x(self.title)
            self.menuButton = pygame.image.load("res/menu/menuFrame.png").convert_alpha()
            self.menuButton = pygame.transform.scale_by(self.menuButton, st.scaleFactor)
            self.cursor = Cursor(st.SCREEN_WIDTH/2 -150, st.SCREEN_HEIGHT/2)
            self.cursorGroup = pygame.sprite.Group()
            self.cursorGroup.add(self.cursor)
            self.cursorIndex = 0
            self.cursorPos = [st.SCREEN_HEIGHT/2, st.SCREEN_HEIGHT/2 + 1.5 * self.menuButton.get_height(),st.SCREEN_HEIGHT/2  + 3 * self.menuButton.get_height()]

            self.menu = True
            self.running = True
            self.game = False

            maxY = st.SCREEN_WIDTH + st.SCREEN_HEIGHT
            #self.item = [x, y, xRef, width, height, speed, reset]
            self.mercury = [-16, 100, 0, 16, 16, 1, 100]
            self.venus = [-28, 300, 16, 28, 28, 1.5, 300]
            self.earth = [-28, 500, 44, 28, 28, 2, 500]
            self.mars = [-16, 700, 72, 16, 16, 2, 700]
            self.jupiter = [-160, maxY/3 + 160, 88, 160, 160, 1, maxY/3 + 160]
            self.saturn = [-242, maxY/2 + 150, 248, 242, 106, 1.5, maxY/2  + 150]
            self.uranus = [-94, maxY*3/4, 490, 94, 150, 1.5, maxY*3/4]
            self.neptune = [-94, maxY - 94, 584, 94, 94, 2.5, maxY - 94]
            self.planets = [self.mercury, self.venus, self.earth, self.mars, self.jupiter, self.saturn, self.uranus, self.neptune]

        def execution(self):
            while self.running:
                while self.menu:
                    self.menu = self.menuLoop()
                while self.game:
                    self.game = self.run()

        def menuLoop(self):
            self.clock.tick(st.FPS)
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
                        self.cursorIndex -= 1
                    if event.key == pygame.K_DOWN:
                        self.cursorIndex += 1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        self.keyPressedSpace = False

            if self.cursorIndex < 0:
                self.cursorIndex = 2
            elif self.cursorIndex > 2:
                self.cursorIndex = 0

            if self.keyPressedSpace:
                if self.cursorIndex == 0:
                    self.startTime = time.time()
                    self.missleStartTime = time.time()
                    self.missleInterval = randint(3, 7)
                    self.game = True
                    return False
                elif self.cursorIndex == 1:
                    print("Options")
                elif self.cursorIndex == 2:
                    self.menu == False
                    self.running = False
                    return False

            self.sun = pygame.image.load("res/menu/sun.png").convert_alpha()
            self.planetSheet = pygame.image.load("res/menu/planetsSheet.png").convert_alpha()
            self.planetSheet = pygame.transform.scale2x(self.planetSheet)
            
            self.screen.fill((0, 0, 0))
            if self.frameCounter % 30 == 0:
                self.stars()
            for star in self.starsGroup:
                self.screen.fill((255, 255, 255), star)
            self.screen.blit(self.sun,(0,0))
            for planet in self.planets:
                planet[0] += planet[5]
                planet[1] -= planet[5]
                if planet[1] < -planet[4]:
                    planet[0] = -planet[3]
                    planet[1] = planet[6]
                self.screen.blit(self.planetSheet, (planet[0], planet[1]), (planet[2], 0, planet[3], planet[4]))
            self.screen.blit(self.cursor.image, (st.SCREEN_WIDTH*3/8, self.cursorPos[self.cursorIndex] - 25 * st.scaleFactor))
            self.screen.blit(self.menuButton, (st.SCREEN_WIDTH/2 - self.menuButton.get_width()/2, st.SCREEN_HEIGHT/2 - self.menuButton.get_height()/2))
            self.screen.blit(self.menuButton, (st.SCREEN_WIDTH/2 - self.menuButton.get_width()/2, st.SCREEN_HEIGHT/2 + self.menuButton.get_height()))
            self.screen.blit(self.menuButton, (st.SCREEN_WIDTH/2 - self.menuButton.get_width()/2, st.SCREEN_HEIGHT/2 + self.menuButton.get_height()* 2.5))
            self.screen.blit(self.title, (st.SCREEN_WIDTH/2 - 450, st.SCREEN_HEIGHT/6))
            pygame.display.flip()
            self.frameCounter += 1
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
                            with open("highscore.bin", "wb") as file:
                                file.write(pickle.dumps(self.highscore))
                            self.new()
                            return
                for bul in self.bullets:
                    if abs(i.rect.x - bul.rect.x) < 150:
                        if pygame.sprite.collide_mask(bul, i):
                            if i in self.lasers:
                                i.image = pygame.image.load("res/transparent.png").convert_alpha()
                                self.obstacles.remove(i.head)
                                self.obstacles.remove(i.tail)
                            elif type(i) == LazerEnd:
                                curr = i.parent
                                curr.image = pygame.image.load("res/transparent.png").convert_alpha()
                                self.obstacles.remove(curr.head)
                                self.obstacles.remove(curr.tail)
                            else:
                                i.kill()
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

            text_surface = self.font.render(str(int(self.score/300)) + " M", True, (170,170,170))
            highscore_surface = self.font.render("Highscore " + str(self.highscore) + " M", True, (170, 170, 170))
            self.score += st.playerSpeed
            self.all_sprites.update()
            self.screen.fill((12, 12, 12))

            if self.frameCounter % 30 == 0:
                self.stars()
            for star in self.starsGroup:
                self.screen.fill((255, 255, 255), star)
            self.all_sprites.draw(self.screen)
            for i in self.obstacles:
                if type(i) == Gun:
                    self.screen.blit(i.image, i.rect.topleft)
            self.screen.blit(text_surface, (25, 25))
            self.screen.blit(highscore_surface, (25, 75))
            pygame.display.flip()
            self.frameCounter += 1
            return True
        def stars(self):
            self.starsGroup.clear()
            for i in range(0, 80):
                size = randint(0,3)
                self.tempRect = pygame.Rect(randint(0,st.SCREEN_WIDTH), randint(0, st.SCREEN_HEIGHT), size, size)
                self.starsGroup.append(self.tempRect)


g = Game()
g.load()
g.new()
g.execution()

pygame.quit()
