# life_gui_6.py
#
# Graphical user interface for Conway's Game of Life.
#
# Search for XXX to find main places in need of changes and/or additions.
#
import pygame
import sys
import random

class Rectangle:
    ''' Defines a rectangular area onscreen:
                    |      |
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

#...............................................................................
# Configuration constants
U_ROWS = 25 # rows in the Life universe.
U_COLS = 40 # cols in the Life universe.
CELL_SIZE = 16
GRID_SIZE = CELL_SIZE + 1 # + 1 allows for 1 pixel border on LHS of cell.
MENU_HEIGHT = 16
BORDER_WIDTH = 10
SCREEN_HEIGHT = U_ROWS*GRID_SIZE + 1 + 2*BORDER_WIDTH + MENU_HEIGHT # + 1 allows for 1 pixel border on RHS of screen.
SCREEN_WIDTH = U_COLS*GRID_SIZE + 1 + 2*BORDER_WIDTH
LIVE_CELL = pygame.image.load("Aqua-Ball-icon.png")

# Game States:
(PAUSE, STEP, PLAY) = list(range(3))

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

#...............................................................................
# XXX Game Functions
#
def load():
    # Set state to PAUSE,
    # conduct a dialogue about what file to load,
    # and load it.
    #
    # What to do if the size of the universe in the file is not the same
    # as ours? If it is smaller? If it is larger?
    print('Running load') # For debugging.
    
def save():
    # Set state to PAUSE,
    # conduct a dialogue about what file to save to,
    # and save it.
    print('Running save') # For debugging.
    
def pause():
    # Set state to PAUSE.
    print('Running pause') # For debugging.
    
def step():
    # Set state to STEP.
    print('Running step') # For debugging.
    
def play():
    # Set state to PLAY.
    print('Running play') # For debugging.
    
def edit():
    # Set state to PAUSE.
    # Watch for mouse clicks in game region and kill and birth cells accordingly.
    #     Get mouse click coords.
    #     Convert to cell coords.
    #     Flip state of cell in universe AND onscreen.
    print('Running edit') # For debugging.
    
def clear():
    # Set state to PAUSE.
    # Clear the universe, i.e. make all cells dead.
    # Clear the screen.
    print('Running clear') # For debugging.
    
def null():
    print('Doing nothing') # For debugging.
    pass

#...............................................................................
# Initialize the universe.
# XXX

game_state = PAUSE

#...............................................................................
# Initialize the Pygame screen.
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(BLACK)
pygame.display.flip()

#...............................................................................
# Define the game menu.
#
# The menu is a list of functions, icon file names, and icon images.
menu = [ [load, "folder.png"],
         [save, "folder_add.png"],
         [null, "black_separator.png"],
         [pause, "control_pause_blue.png"],
         [step, "control_play_blue.png"],
         [play, "control_fastforward_blue.png"],
         [null, "black_separator.png"],
         [edit, "pencil.png"],
         [clear, "picture_empty.png"]
       ]

# Define the onscreen menu area.
menu_area = Rectangle(BORDER_WIDTH, BORDER_WIDTH, BORDER_WIDTH + MENU_HEIGHT,
                      SCREEN_WIDTH - BORDER_WIDTH)

# Load the icon images from the files, appending them to the menu list entries,
# and drawing them on the screen.
for i in range(len(menu)):
    menu[i].append(pygame.image.load(menu[i][1]))
    screen.blit(menu[i][2], (menu_area.left + i*GRID_SIZE + 1, menu_area.top))
    
#...............................................................................
# Define the game area.
#
game_area = Rectangle(BORDER_WIDTH + MENU_HEIGHT, BORDER_WIDTH,
                      SCREEN_HEIGHT - BORDER_WIDTH - 1, SCREEN_WIDTH - BORDER_WIDTH - 1)
# Draw the Universe grid.
#
# Draw the horizontal lines:
for y in range(0, U_ROWS+1):
    pygame.draw.line(screen, GREY, (game_area.left, game_area.top + y*GRID_SIZE),
                     (game_area.right, game_area.top + y*GRID_SIZE))

# Draw the vertical lines:
for x in range(0, U_COLS+1):
    pygame.draw.line(screen, GREY, (game_area.left + x*GRID_SIZE, game_area.top ),
                     (game_area.left + x*GRID_SIZE, game_area.bottom))
    
pygame.display.flip()

#...............................................................................
# Left in for debugging:
#
# Sprinkle some random live cells around for testing.
#
# for i in range(1,100):
#     # + 1s below move past LH borderline, below upper borderline.
#     screen.blit(LIVE_CELL, (game_area.left + random.randint(0, U_COLS-1)*GRID_SIZE+1,
#                             game_area.top + random.randint(0, U_ROWS-1)*GRID_SIZE+1))
# pygame.display.flip()

#...............................................................................
# Main Event Loop:
#
while True:
    #
    # Part I: Handle events (if any):
    #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            # Note imperfection of considering only position of button up and
            # ignoring position of button down.
            x = event.pos[0]
            y = event.pos[1]
            # print "mouse at (%d, %d)" % (x, y) # For debugging
            # print menu_area.inside(x, y) # For debugging
            if menu_area.inside(x, y):
                menu_position = (x - menu_area.left)//GRID_SIZE
                # print 'Menu item: ', menu_position # For debugging
                if menu_position < len(menu):
                    # Invoke the function at this position in the menu.
                    menu[menu_position][0]()
    #
    # Part II: Simulate one generation of Game of Life (if not paused)
    #
    if game_state != PAUSE:
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

        # XXX Missing display code here, or maybe up above while aging
        # and cells are born or killed?
        
        if game_state == STEP:
            state = PAUSE
            
