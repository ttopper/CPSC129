# life_gui_2.py
#
# Now a little refactoring:
# 1. A function for the cell drawing. Thinking ahead I know that
#    sooner rather than later I will need to be drawing dead cells
#    as well, and I want to hide that coordinate calculation
#    away in a function.
# 2. Move the grid drawing into a single function.
import pygame
import sys
import time
import random

BORDER_WIDTH = 10
U_ROWS = 25
U_COLS = 40

def draw_cell(cell, row, col):
    # Draws the cell at location row, col in life universe coordinates
    # onto matching location onscreen.
    x_coord = col * grid_size + 1 + BORDER_WIDTH
    y_coord = row * grid_size + 1 + BORDER_WIDTH
    screen.blit(live_cell, (x_coord, y_coord))

def draw_grid():
    # Draw horizontal lines.
    for y in range(0, U_ROWS+1):
        pygame.draw.line(screen, GREY, (BORDER_WIDTH, y*grid_size+BORDER_WIDTH),
                         (SCREEN_WIDTH-BORDER_WIDTH-1, y*grid_size+BORDER_WIDTH))
    # Draw vertical lines.
    for x in range(0, U_COLS+1):
        pygame.draw.line(screen, GREY, (x*grid_size+BORDER_WIDTH, BORDER_WIDTH),
                         (x*grid_size+BORDER_WIDTH, SCREEN_HEIGHT-BORDER_WIDTH-1))

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

pygame.init()

live_cell = pygame.image.load("Aqua-Ball-icon.png")
cell_size = 16
grid_size = cell_size + 1 # width of cell plus 1 for left-hand border line.

SCREEN_HEIGHT = U_ROWS*grid_size + 1 + 2*BORDER_WIDTH
SCREEN_WIDTH = U_COLS*grid_size + 1 + 2*BORDER_WIDTH
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(BLACK)
# pygame.display.flip()

draw_grid()
# pygame.display.flip()
# Randomly place some live cells.
for i in range(1, U_ROWS*U_COLS//5):
    draw_cell(live_cell, random.randint(0, U_ROWS-1),
                          random.randint(0, U_COLS-1))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
