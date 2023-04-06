import tkinter as tk

root = tk.Tk()
SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = SCREEN_WIDTH * 9/16
FPS = 60
SPEED = 10
PLAYER_ACC = 1
#define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BASE_WIDTH = 1600
BASE_HEIGHT = 900
scaleFactor = SCREEN_WIDTH/BASE_WIDTH

playerSpeed = 4.0