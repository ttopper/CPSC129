# life_v1.py
# Conway's Game of Life
import random

print('''
================================
Welcome to Conway's Game of Life
--------------------------------
''')
# Initialize the universe
init_type = input('Initialize (r) randomly or (f) from file? ')

if init_type == 'r':
    u_rows = int(input('Number of rows in universe? '))
    u_cols = int(input('Number of columns in universe? '))
    u = []
    for row in range(u_rows):
        u.append(u_cols*[0])
    live_pct = int(input('Initial percentage of live cells? '))
    for row in range(u_rows):
        for col in range(u_cols):
            if random.randint(1,100) <= live_pct:
                u[row][col] = 1
                
elif init_type == 'f':
    fname = input('Name of file to read from? ')
    infile = open(fname, 'r')
    u = eval(infile.read())
    u_rows = len(u)
    u_cols = len(u[0])
    infile.close()

# Display the initial universe
LIVE_CELL = '@'
DEAD_CELL = '-'
for row in range(u_rows):
    for col in range(u_cols):
        if u[row][col] == 1:
            print(LIVE_CELL,end='')
        elif u[row][col] == 0:
            print(DEAD_CELL,end='')
    print()
print()

MENU = '''Options:
    a : Age universe one generation
    m : Age universe multiple generations
    s : Save universe to disk
    l : Load universe from disk
    q : Quit program
'''

done = False
while not done:
    print(MENU)
    command = input('Command (a|m|s|l|q): ')

    if command == 'a' or command == 'm':
        if command == 'a':
            generations = 1
        else:
            generations = int(input('How many generations? '))

        for generation in range(0, generations):

            # Create next universe
            next_u = []
            for row in range(u_rows):
                next_u.append(u_cols*[0])

            # Age the universe:
            # Consider every cell in the universe
            for row in range(1, u_rows-1):
                for col in range(1, u_cols-1):    
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
            
            # Display the new universe
            for row in range(u_rows):
                for col in range(u_cols):
                    if u[row][col] == 1:
                        print(LIVE_CELL,end='')
                    elif u[row][col] == 0:
                        print(DEAD_CELL,end='')
                print()
            print()

            
    elif command == 's':
        fname = input('Name of file to save to? ')
        outfile = open(fname, 'w')
        outfile.write(str(u))
        outfile.close()
        
    elif command == 'l':
        fname = input('Name of file to load from? ')
        infile = open(fname, 'r')
        u = eval(infile.read())
        u_rows = len(u)
        u_cols = len(u[0])
        infile.close()
        # Display the newly loaded universe
        for row in range(u_rows):
            for col in range(u_cols):
                if u[row][col] == 1:
                    print(LIVE_CELL,end='')
                elif u[row][col] == 0:
                    print(DEAD_CELL,end='')
            print()
        print()
        
    elif command == 'q':
        done = True
        
    else:
        print('Command not recognized. Please try again.')
