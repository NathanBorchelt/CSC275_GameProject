import pygame
import random
import MenuEntities
import Player

WIDTH = 1600
HEIGHT = 900
FPS = 30
#define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

        
# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
#create sprite group and add the player sprite to it
all_sprites = pygame.sprite.Group()
menuCursor = MenuEntities.MenuCursor() 
startButton = MenuEntities.MenuButton(HEIGHT/2, "res/startText.png")
endButton = MenuEntities.MenuButton(HEIGHT/2+80, "res/endText.png")

all_sprites.add(menuCursor)
all_sprites.add(startButton)
all_sprites.add(endButton)
prevCursorPos = []


#Game loop
running = True
game = False
menu = True

while running:
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
        pygame.display.flip()
    while game:
        clock.tick(FPS)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    cursor.rect.y -= 100
                elif event.key == pygame.K_a:
                    cursor.rect.x -= 100
                elif event.key == pygame.K_s:
                    cursor.rect.y += 100
                elif event.key == pygame.K_d:
                    cursor.rect.x += 100
                elif event.key == pygame.K_SPACE:
                    prevCursorPos.append(cursor.pos)

                elif event.key == pygame.K_ESCAPE:
                    running = False
                    game = False

        
        all_sprites.update()       
        screen.fill(BLACK)
        boardImage = pygame.image.load("res/chessBoard.png")
        boardImage = pygame.transform.scale(boardImage, (800,800))
        screen.blit(boardImage, (400, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
pygame.quit() 
