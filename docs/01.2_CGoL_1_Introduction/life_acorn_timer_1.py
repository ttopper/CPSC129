# life_acorn_timer_1.py
# Conway's Game of Life
# Acorn timer.

# Version 1: Change from character by character output to line output.

import random
import time

start_t = time.time()
# Create the universe
U_ROWS = 25
U_COLS = 80

u = []
for row in range(U_ROWS):
    u.append(U_COLS*[0])

# Initialize the universe with acorn shape.
#                  *
#                   *
#                 **  ***
# Place it roughly in centre of universe.
centre_row = U_ROWS/2
centre_col = U_COLS/2
u[centre_row][centre_col] = 1
u[centre_row-1][centre_col-2] = 1
u[centre_row+1][centre_col-3] = 1
u[centre_row+1][centre_col-2] = 1
u[centre_row+1][centre_col+1] = 1
u[centre_row+1][centre_col+2] = 1
u[centre_row+1][centre_col+3] = 1

create_t = time.time()

# Time 50 generations.
display_t = 0
age_t = 0
for generation in range(0,50):

    start_display_t = time.time()
    # Display the universe
    LIVE_CELL = '@'
    DEAD_CELL = '-'
    for row in range(U_ROWS):
        line = ''
        for col in range(U_COLS):
            if u[row][col] == 1:
                line += LIVE_CELL
            elif u[row][col] == 0:
                line += DEAD_CELL
        print line
    print
    print
    display_t += time.time()-start_display_t

    start_age_t = time.time()
    # Create next universe
    next_u = []
    for row in range(U_ROWS):
        next_u.append(U_COLS*[0])

    # Age the universe:
    # Consider every cell in the universe
    for row in range(0, U_ROWS):
        for col in range(0, U_COLS):    
            # Count its live neighbours
            #row-1, col-1      row-1, col     row-1 col+1
            #row, col-1                       row, col+1
            #row+1, col-1      row+1, col     row+1, col+1
            neighbours = 0
            for r in range(row-1, row+2):
                for c in range(col-1, col+2):
                    neighbours += u[r%U_ROWS][c%U_COLS]
            neighbours -= u[row][col]

            # Based on its current state and its neighbours
            # Decide if it lives, dies or is born
            # Recording result in next universe
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
    age_t += time.time()-start_age_t

end_t = time.time()
print 'Total run time =', end_t-start_t
print 'Creation and initialization time =', create_t - start_t
print 'Display time =', display_t
print 'Aging time =', age_t

##Total run time = 203.90899992
##Creation and initialization time = 0.0
##Display time = 203.136000633
##Aging time = 0.772999286652

