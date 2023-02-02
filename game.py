import pygame
import random
import MenuEntities
import Player
import math

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
prevCursorPos = [Player.Vector2f(750, 750)]


#Game loop
running = True
game = False
menu = True
follow = False
deleteEnd = False
x = 0

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

        #prevents list from being 0 and stops the player follow loop
        if len(prevCursorPos) == 0:
            posx = cursor.pos.x
            posy = cursor.pos.y
            prevCursorPos.append(Player.Vector2f(posx, posy))
            follow = False
        #if current position is different than the last position, it will append the new position to the list
        if (cursor.pos.x != prevCursorPos[len(prevCursorPos) - 1].x or cursor.pos.y != prevCursorPos[len(prevCursorPos) - 1].y):
            posx = cursor.pos.x
            posy = cursor.pos.y
            prevCursorPos.append(Player.Vector2f(posx, posy))
            x = len(prevCursorPos)
            #tests each position in the list to determine if it is equal to any other index on the list
            #if it is then it will delete all of the indexes after it
            for i in prevCursorPos:
                if prevCursorPos[len(prevCursorPos) - 1].x == i.x and prevCursorPos[len(prevCursorPos) - 1].y == i.y:
                    x = prevCursorPos.index(i)+1
                    deleteEnd = True
                    break
            if deleteEnd:
                while x < len(prevCursorPos):
                    prevCursorPos.pop()
                deleteEnd = False
        #follow is the just the loop for following the coordinates in the array
        if follow:
            player.setPos(prevCursorPos[0])
            del prevCursorPos[0]


        all_sprites.update()       
        screen.fill(BLACK)
        #I don't know why the hell I put this here
        boardImage = pygame.image.load("res/chessBoard.png")
        boardImage = pygame.transform.scale(boardImage, (800,800))
        screen.blit(boardImage, (400, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
pygame.quit() 
