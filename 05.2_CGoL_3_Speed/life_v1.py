# life_v1.py
# Conway's Game of Life
# (Supports Toroidal universe.)
#
# v1: Stripped down to engine for timing.
import random

def display(u):
    for row in u:
        for cell in row:
            if cell == 1:
                print('*', end = ' ')
            else:
                print('-',end=' ')
        print()
    print()

# Get size of universe.
u_rows = int(input('Number of rows in universe? '))
u_cols = int(input('Number of columns in universe? '))

# Initialize empty universe.
u = []
for row in range(u_rows):
    u.append(u_cols*[0])

# Initialize random state of universe.
live_pct = int(input('Initial percentage of live cells? '))
for row in range(u_rows):
    for col in range(u_cols):
        if random.randint(1,100) <= live_pct:
            u[row][col] = 1

# Length of simulation?
generations = int(input('How many generations to time? '))

for generation in range(0, generations):

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
    
    # Display the new universe
    display(u)
