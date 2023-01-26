import pygame
import random

WIDTH = 1600
HEIGHT = 900
FPS = 30
#define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


class Player(pygame.sprite.Sprite):
    #sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/plane12alpha.png").convert()
        self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        
    def update(self):
        if self.rect.bottom < 0:
            self.rect.top = HEIGHT
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0
        if self.rect.right < 0:
            self.rect.left = WIDTH
        if self.rect.left > WIDTH:
            self.rect.right = 0

class MenuCursor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("res/menuCursor.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.top = HEIGHT/2
    def update(self):
        if self.rect.top < HEIGHT/2:
            self.rect.bottom = HEIGHT/2 + 140 
        if self.rect.bottom > HEIGHT/2 + 140:
            self.rect.top = HEIGHT/2

class MenuButton(pygame.sprite.Sprite):
    def __init__(self, p_y, p_tex):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(p_tex).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.top = p_y
        
# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
#create sprite group and add the player sprite to it
all_sprites = pygame.sprite.Group()
#player = Player()
menuCursor = MenuCursor() 
startButton = MenuButton(HEIGHT/2, "res/startText.png")
endButton = MenuButton(HEIGHT/2+80, "res/endText.png")
all_sprites.add(menuCursor)
all_sprites.add(startButton)
all_sprites.add(endButton)

#Game loop
running = True
game = False
menu = True
keyW = False
keyA = False
keyS = False
keyD = False

while running:
    #keep loop running at the right speed
    
    #Process input (events)
    while menu:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                menu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    menu = False
                if event.key == pygame.K_w:
                    menuCursor.rect.y -= 80
                if event.key == pygame.K_s:
                    menuCursor.rect.y += 80
                if event.key == pygame.K_SPACE:
                    if menuCursor.rect.y == startButton.rect.y:
                        menu = False
                        game = True
                        all_sprites.empty()
                        player = Player()
                        all_sprites.add(player)
                    if menuCursor.rect.y == endButton.rect.y:
                        running = False
                        menu = False
        screen.fill(BLACK)
        all_sprites.update()       
       
        all_sprites.draw(screen)
        pygame.display.flip()
    while game:
        clock.tick(FPS)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    keyW = True
                if event.key == pygame.K_a:
                    keyA = True
                if event.key == pygame.K_s:
                    keyS = True
                if event.key == pygame.K_d:
                    keyD = True
                if event.key == pygame.K_ESCAPE:
                    running = False
                    game = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    keyW = False
                if event.key == pygame.K_a:
                    keyA = False
                if event.key == pygame.K_s:
                    keyS = False
                if event.key == pygame.K_d:
                    keyD = False
        
        if keyW:
            player.rect.y -= 15
        if keyA:
            player.rect.x -= 15
        if keyS:
            player.rect.y += 15
        if keyD:
            player.rect.x += 15
        all_sprites.update()       
        screen.fill(BLACK)
        all_sprites.draw(screen)
        pygame.display.flip()
pygame.quit() 
