import random
# Create the universe
U_SIZE = 15
LIVE_PCT = 20
LIVE_CELL = '@'
DEAD_CELL = '-'

u = []
for row in range(U_SIZE ):
    u.append(U_SIZE *[0])
# Initialize the universe

for row in range(U_SIZE):
    for col in range(U_SIZE):
        if random.randint(1,100) <= LIVE_PCT:
            u[row][col] = 1
for generation in range(10):
#Display the universe

    for row in range(U_SIZE):
        for col in range(U_SIZE):
            if u[row][col] == 1:
                print(LIVE_CELL,end='')
            elif u [row][col] == 0:
                print(DEAD_CELL, end='')
        print()
    print('\n')

    next_u = []
    for row in range(U_SIZE ):
        next_u.append(U_SIZE *[0])

    for row in range(1,U_SIZE-1):
        for col in range(1,U_SIZE-1):
            #Count its live neighbours
            neighbours = 0
            for r in range(row-1,row+2):
                for c in range(col-1,col+2):
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
    u = next_u
