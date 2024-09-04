# Step 2: Review existing code

Let's look at the graphical code for making the Game of Life. This code 
draws the universe and populates some random cells for the initial 
generation of our universe.

```python
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

pygame.init()

U_ROWS = 25 # rows in the Life universe.
U_COLS = 40 # cols in the Life universe.

live_cell = pygame.image.load("Aqua-Ball-icon.png")
cell_size = 16            # matches the size of the Aqua-Ball-icon
grid_size = cell_size + 1 # + 1 allows for 1 pixel border on LHS of cell.

SCREEN_HEIGHT = U_ROWS*grid_size + 1 # + 1 allows for 1 pixel border on RHS of screen.
SCREEN_WIDTH = U_COLS*grid_size + 1
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(BLACK)
pygame.display.flip()

# Draw horizontal lines.
for y in range(0, U_ROWS+1):
    pygame.draw.line(screen, GREY, (0, y*grid_size), (SCREEN_WIDTH, y*grid_size))
#             0                          SCREEN_WIDTH
# 
# 0*grid_size ----------------------------------
#
# 1*grid_size ----------------------------------
#
# 2*grid_size ----------------------------------
# 
# ...

# Draw vertical lines.
for x in range(0, U_COLS+1):
    pygame.draw.line(screen, GREY, (x*grid_size, 0), (x*grid_size, SCREEN_WIDTH))
pygame.display.flip()

for i in range(1,100):
    # + 1s offset below move past LH borderline, below upper borderline.
    screen.blit(live_cell, (random.randint(0, U_COLS)*grid_size+1,
                            random.randint(0, U_ROWS)*grid_size+1))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
```