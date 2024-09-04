# life_gui_0.py
#
# Graphical user interface for Conway's Game of Life.
import pygame
import time
import random

# Colour definitions.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TEAL = (0, 128, 128)
YELLOW = (255, 255, 0)
GREY = (128,128,128)
SILVER = (192, 192, 192)

class Rectangle:
    '''             |      |
                    | top  |
                    |      | bottom
        +--------+  -      |
        |        |         |
        +--------+         -

--------| left
-----------------| right

    '''
    def __init__(self, top, left, bottom, right):
        self.top = top
        self.left = left
        self.bottom = bottom
        self.right = right
    def inside(self, x, y):
        return x >= self.left and x <= self.right and y >= self.top and y <= self.bottom
    
U_ROWS = 25 # rows in the Life universe.
U_COLS = 40 # cols in the Life universe.
CELL_SIZE = 16
GRID_SIZE = CELL_SIZE + 1 # + 1 allows for 1 pixel border on LHS of cell.
MENU_HEIGHT = 16
BORDER_WIDTH = 10
SCREEN_HEIGHT = U_ROWS*GRID_SIZE + 1 + 2*BORDER_WIDTH + MENU_HEIGHT # + 1 allows for 1 pixel border on RHS of screen.
SCREEN_WIDTH = U_COLS*GRID_SIZE + 1 + 2*BORDER_WIDTH

def load(): print('Running load')
def save():  print('Running save')
def pause():  print('Running pause')
def step():  print('Running step')
def play():  print('Running play')
def edit():  print('Running edit')
def clear():  print('Running clear')
def null(): print('Doing nothing')

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(BLACK)
pygame.display.flip()

live_cell = pygame.image.load("Aqua-Ball-icon.png")

# Define menu
menu = [ [load, "folder.png"], [save, "folder_add.png"],
         [null, "black_separator.png"],
         [pause, "control_pause_blue.png"], [step, "control_play_blue.png"],
         [play, "control_fastforward_blue.png"],
         [null, "black_separator.png"],
         [edit, "pencil.png"],  [clear, "picture_empty.png"]
         ]
menu_area = Rectangle(BORDER_WIDTH, BORDER_WIDTH, BORDER_WIDTH + MENU_HEIGHT,
                      SCREEN_WIDTH - BORDER_WIDTH)
for i in range(len(menu)):
    menu[i].append(pygame.image.load(menu[i][1]))
    screen.blit(menu[i][2], (menu_area.left + i*GRID_SIZE + 1, menu_area.top))

game_area = Rectangle(BORDER_WIDTH + MENU_HEIGHT, BORDER_WIDTH,
                      SCREEN_HEIGHT - BORDER_WIDTH - 1, SCREEN_WIDTH - BORDER_WIDTH - 1)
                      
# Draw horizontal lines.
for y in range(0, U_ROWS+1):
    pygame.draw.line(screen, GREY, (game_area.left, game_area.top + y*GRID_SIZE),
                     (game_area.right, game_area.top + y*GRID_SIZE))

# Draw vertical lines.
for x in range(0, U_COLS+1):
    pygame.draw.line(screen, GREY, (game_area.left + x*GRID_SIZE, game_area.top ),
                     (game_area.left + x*GRID_SIZE, game_area.bottom))
pygame.display.flip()

for i in range(1,100):
    # + 1s below move past LH borderline, below upper borderline.
    screen.blit(live_cell, (game_area.left + random.randint(0, U_COLS-1)*GRID_SIZE+1,
                            game_area.top + random.randint(0, U_ROWS-1)*GRID_SIZE+1))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            x = event.pos[0]
            y = event.pos[1]
            print(f"mouse at {x:d}, {y:d}")
            print(menu_area.inside(x, y))
            if menu_area.inside(x, y):
                menu_position = (x - menu_area.left)//GRID_SIZE
                print('Menu item: ', menu_position)
                if menu_position < len(menu):
                    menu[menu_position][0]()
pygame.quit()        
