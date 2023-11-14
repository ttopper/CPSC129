# life_v0.py
# Conway's Game of Life Version 0
import random

# Create the universe
U_SIZE = 5

u = []
for row in range(U_SIZE):
    u.append(U_SIZE*[0])

# Initialize the universe
LIVE_PCT = 40
for row in range(U_SIZE):
    for col in range(U_SIZE):
        if random.randint(1,100) <= LIVE_PCT:
            u[row][col] = 1

# Forever: (or at least a while)
for generation in range(0,5):

    # Display the universe
    LIVE_CELL = '@'
    DEAD_CELL = '-'
    for row in range(U_SIZE):
        for col in range(U_SIZE):
            if u[row][col] == 1:
                print LIVE_CELL,
            elif u[row][col] == 0:
                print DEAD_CELL,
        print
    print
    print

    # Create next universe
    next_u = []
    for row in range(U_SIZE):
        next_u.append(U_SIZE*[0])

    # Age the universe:
    # Consider every cell in the universe
    for row in range(1, U_SIZE-1):
        for col in range(1, U_SIZE-1):    
            # Count its live neighbours
            #row-1, col-1      row-1, col     row-1 col+1
            #row, col-1                       row, col+1
            #row+1, col-1      row+1, col     row+1, col+1
            neighbours = 0
            for r in range(row-1, row+2):
                for c in range(col-1, col+2):
                    neighbours += u[r][c]
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
