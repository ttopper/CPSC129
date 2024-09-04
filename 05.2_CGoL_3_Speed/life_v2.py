# life_v2.py
# Conway's Game of Life
# (Supports Toroidal universe.)
#
# v1: Stripped down to engine for timing.
# v2: Now instrumented for timing.
#     display() removed.
import random
import time

# Get size of universe.
# u_rows = int(input('Number of rows in universe? '))
# u_cols = int(input('Number of columns in universe? '))
u_rows = u_cols = 100
# Initialize empty universe.
u = []
for row in range(u_rows):
    u.append(u_cols*[0])

# Initialize random state of universe.
# live_pct = int(input('Initial percentage of live cells? '))
live_pct = 42
for row in range(u_rows):
    for col in range(u_cols):
        if random.randint(1,100) <= live_pct:
            u[row][col] = 1

# Length of simulation?
# generations = int(input('How many generations to time? '))
generations = 100

creation_time = 0.0
aging_time = 0.0
copying_time = 0.0
for generation in range(0, generations):

    start = time.time()
    # Create next universe
    next_u = []
    for row in range(u_rows):
        next_u.append(u_cols*[0])
    end = time.time()
    creation_time += end - start

    start = time.time()
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
    end = time.time()
    aging_time +=  end - start

    start = time.time()
    # Replace universe with next universe
    u = next_u
    end = time.time()
    copying_time += end - start
    
    # Display the new universe
    # display(u)

total_time = creation_time + aging_time + copying_time
print(f'total_time    : {total_time:5.2f}')
print(f'creation_time : {creation_time:5.2f} = {creation_time*100.0/total_time:5.2f}%')
print(f'aging_time    : {aging_time:5.2f} = {aging_time*100.0/total_time:5.2f}%')
print(f'copying_time  : {copying_time:5.2f} = {copying_time*100.0/total_time:5.2f}%')
