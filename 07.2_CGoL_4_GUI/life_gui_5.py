# life_gui_0.py
#
# Graphical user interface for Conway's Game of Life.
import pygame
import sys
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
SCREEN_BORDER = 10
SCREEN_HEIGHT = U_ROWS*GRID_SIZE + 1 + 2*SCREEN_BORDER + MENU_HEIGHT # + 1 allows for 1 pixel border on RHS of screen.
SCREEN_WIDTH = U_COLS*GRID_SIZE + 1 + 2*SCREEN_BORDER

def load(): print 'Running load'
def save():  print 'Running save'
def pause():  print 'Running pause'
def step():  print 'Running step'
def play():  print 'Running play'
def edit():  print 'Running edit'
def clear():  print 'Running clear'
def null(): print 'Doing nothing'

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
menu_area = Rectangle(SCREEN_BORDER, SCREEN_BORDER, SCREEN_BORDER + MENU_HEIGHT,
                      SCREEN_WIDTH - SCREEN_BORDER)
for i in range(len(menu)):
    menu[i].append(pygame.image.load(menu[i][1]))
    screen.blit(menu[i][2], (menu_area.left + i*GRID_SIZE + 1, menu_area.top))

game_area = Rectangle(SCREEN_BORDER + MENU_HEIGHT, SCREEN_BORDER,
                      SCREEN_HEIGHT - SCREEN_BORDER - 1, SCREEN_WIDTH - SCREEN_BORDER - 1)
                      
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

while True:
    # Handles events (if any).
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            x = event.pos[0]
            y = event.pos[1]
            print "mouse at (%d, %d)" % (x, y)
            print menu_area.inside(x, y)
            if menu_area.inside(x, y):
                menu_position = (x - menu_area.left)/GRID_SIZE
                print 'Menu item: ', menu_position
                if menu_position < len(menu):
                    menu[menu_position][0]()

    # Simulate Game of Life:
    
    # Create next universe
    next_u = []
    for row in range(u_rows):
        next_u.append(u_cols*[0])

    # Age the universe:
    # Consider every cell in the universe
    for row in range(0, u_rows):
        for col in range(0, u_cols):    
            neighbours = 0
            for r in range(row-1, row+2):
                for c in range(col-1, col+2):
                    if r >= u_rows: r = 0
                    if c >= u_cols: c = 0
                    neighbours += u[r][c]
            neighbours -= u[row][col]

            if u[row][col] == 1 and neighbours < 2:
                next_u[row][col] = 0
            elif u[row][col] == 1 and neighbours == 2 or neighbours == 3:
                next_u[row][col] = 1
            elif u[row][col] == 1 and neighbours > 3:
                next_u[row][col] = 0
            elif u[row][col] == 0 and neighbours == 3:
                next_u[row][col] = 1
            else:
                next_u[row][col] = 0

    # Replace universe with next universe
    u = next_u
            
