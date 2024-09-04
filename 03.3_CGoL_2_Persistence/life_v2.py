# life_v2.py
#
# Conway's Game of Life
#
# HISTORY
#   v0: Ring of death around outer border of universe.
#   v1: Supports Toroidal universe.
#   v2: Lightly OOPified
#
import random

class Universe:
    def __init__(self, r=25, c=80, live_cell='@', dead_cell='-'):
        self.rows = r
        self.cols = c
        self.live_cell = live_cell
        self.dead_cell = dead_cell
        self.cells = [[0 for c in range(self.cols)] for r in range(self.rows)]
        
    def randomly_seed(self, live_pct=0):
        ''' Randomly sets live_pct of cells in universe to be 1. '''
        self.cells = [[0 for c in range(self.cols)] for r in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                if random.randint(1,100) <= live_pct:
                    self.cells[row][col] = 1

    def __str__(self):
        ''' Return a string picture of the universe. '''
        uni_pic = ''
        if self.cells:
            for row in range(self.rows):
                for col in range(self.cols):
                    if self.cells[row][col] == 1:
                        uni_pic += self.live_cell
                    else:
                        uni_pic += self.dead_cell
                uni_pic += '\n'
        return uni_pic

    def age(self):
        # Create next universe
        next_cells = [[0 for c in range(self.cols)] for r in range(self.rows)]

        # Age the universe:
        # Consider every cell in the universe
        for row in range(0, self.rows):
            for col in range(0, self.cols):    
                # Count its live neighbours
                neighbours = 0
                for r in range(row-1, row+2):
                    for c in range(col-1, col+2):
                        if r >= self.rows: r = 0 # Handling toroidal universe.
                        if c >= self.cols: c = 0 # Handling toroidal universe.
                        neighbours += self.cells[r][c]
                neighbours -= self.cells[row][col]

                # Decide if it lives, dies or is born
                if (self.cells[row][col] == 1 and neighbours == 2) or neighbours == 3:
                    next_cells[row][col] = 1
        
        # Replace universe with next universe
        u.cells = next_cells
       
if __name__ == '__main__':

    # Welcome the user
    print("=====================")
    print("Conway's Game of Life")
    print("---------------------")

    # Initialize the universe
    u_rows = int(input('Number of rows in universe? '))
    u_cols = int(input('Number of columns in universe? '))
    u = Universe(u_rows, u_cols)
    live_pct = int(input('Initial percentage of live cells? '))
    u.randomly_seed(live_pct)

    # Display the initial state of the universe
    print(u)

    # Main event loop:
    while True:
        command = input('Age universe or quit (a|q)? ')
        if command == 'a' or command == 'A':
            u.age() # Age universe
            print(u) # Display universe               
        else:
            break
