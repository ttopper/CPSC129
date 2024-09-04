# life_gui_1.py
#
# It looks good onscreen, but I can't be sure it's drawing accurately.
# For example I can't tell by looking if it is drawing the outer lines of
# the universe grid(just too thin to tell around the edge of the window).
# Nor can I be sure it isn't drawing lines off the screen.
# To check I am going to try adding a blank border around the universe.
#
# Good thing I did, it revealed several bugs.

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

pygame.init()

BORDER_WIDTH = 10
CELL_ROWS = 25
CELL_COLS = 40

live_cell = pygame.image.load("Aqua-Ball-icon.png")
cell_size = 16
grid_size = cell_size + 1 # width of cell plus 1 for left-hand border line.

SCREEN_HEIGHT = CELL_ROWS*grid_size + 1 + 2*BORDER_WIDTH # + 1 to allow for the bottom border line.
SCREEN_WIDTH = CELL_COLS*grid_size + 1 + 2*BORDER_WIDTH  # + 1 for the right-hand border line.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(BLACK)
pygame.display.flip()

# Draw horizontal lines.
for y in range(0, CELL_ROWS+1):
    pygame.draw.line(screen, GREY, (BORDER_WIDTH, y*grid_size+BORDER_WIDTH),
                     (SCREEN_WIDTH-BORDER_WIDTH-1, y*grid_size+BORDER_WIDTH))
# Draw vertical lines.
for x in range(0, CELL_COLS+1):
    pygame.draw.line(screen, GREY, (x*grid_size+BORDER_WIDTH, BORDER_WIDTH),
                     (x*grid_size+BORDER_WIDTH, SCREEN_HEIGHT-BORDER_WIDTH-1))
pygame.display.flip()

# time.sleep(1)
for i in range(1,CELL_ROWS*CELL_COLS//10):
    screen.blit(live_cell, (random.randint(0, CELL_COLS-1)*grid_size+1+BORDER_WIDTH,
                            random.randint(0, CELL_ROWS-1)*grid_size+1+BORDER_WIDTH))
    # time.sleep(0.2)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
