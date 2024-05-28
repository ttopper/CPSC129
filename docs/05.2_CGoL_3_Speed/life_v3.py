# life_v3.py
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
# Initialize empty arrays.
u = []
next_u = []
n = [] # Count of each cell's live neighbours.
next_n = []
for row in range(u_rows):
    u.append(u_cols*[0])
    next_u.append(u_cols*[0])
    n.append(u_cols*[0])
    next_n.append(u_cols*[0])

# Initialize random state of universe.
# live_pct = int(input('Initial percentage of live cells? '))
live_pct = 42
for row in range(u_rows):
    for col in range(u_cols):
        if random.randint(1,100) <= live_pct:
            next_u[row][col] = 1
# Initialize next_n:
for row in range(0, u_rows):
    for col in range(0, u_cols):    
        neighbours = 0
        for r in range(row-1, row+2):
            for c in range(col-1, col+2):
                if r >= u_rows: r = 0
                if c >= u_cols: c = 0
                neighbours += u[r][c]
        neighbours -= u[row][col]
        n[row][col] = neighbours

# Length of simulation?
# generations = int(input('How many generations to time? '))
generations = 100

aging_time = 0.0
copying_time = 0.0
for generation in range(0, generations):
  
    start = time.time()
    # Copy next_u into u and next_n into n.
    # (was "Create next universe." and "Replace universe with next universe.")
    for row in range(0, u_rows):
        for col in range(0, u_cols):    
            u[row][col] = next_u[row][col]
            n[row][col] = next_n[row][col]
    end = time.time()
    copying_time += end - start

    start = time.time()
    # Age the universe:
    # Consider every cell in the universe
    for row in range(0, u_rows):
        for col in range(0, u_cols):    

            if u[row][col] == 1 and (n[row][col] < 2 or n[row][col] > 3):
                next_u[row][col] = 0
                # Update next_n to reflect this death by subtracting 1 to the neighbour
                # count of each of this cell's eight neighbours.
                for r in range(row-1, row+2):
                    for c in range(col-1, col+2):
                        if r >= u_rows: r = 0
                        if c >= u_cols: c = 0
                        # Don't change this cell's neighbour count.
                        if r!= row and c!=col: 
                            next_n[r][c] -= 1
                
            elif u[row][col] == 0 and n[row][col] == 3:
                next_u[row][col] = 1
                # Update next_n to reflect this birth by adding 1 to the neighbour
                # count of each of this cell's eight neighbours.
                for r in range(row-1, row+2):
                    for c in range(col-1, col+2):
                        if r >= u_rows: r = 0
                        if c >= u_cols: c = 0
                        # Don't change this cell's neighbour count.
                        if r!= row and c!=col:
                            next_n[r][c] += 1
    end = time.time()
    aging_time +=  end - start

    # Display the new universe
    # display(u)

total_time = aging_time + copying_time
print('u_rows =', u_rows)
print('u_cols =', u_cols)
print('generations =', generations)
print('live_pct =', live_pct)
print()
print(f'total_time    : {total_time:5.2f}')
print(f'copying_time  : {copying_time:5.2f} = {copying_time*100.0/total_time:5.2f}%')
print(f'aging_time    : {aging_time:5.2f} = {aging_time*100.0/total_time:5.2f}%')
