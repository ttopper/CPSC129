# life_v3.py
#
# Conway's Game of Life
#
# HISTORY
#   v0: Ring of death around outer border of universe.
#   v1: Supports Toroidal universe.
#   v2: Lightly OOPified
#   v3: Persistence: Store and load universe states from files.
#
# TODO: Support three file formats for saving and loading universe configurations:
#
#   1) A screenshot of the universe, one row per line.
#
#   2) Python literal of the u cells array.
#
#   3) List of locations of live cells.
#      File format:
#      Line 1: universe_height universe_width
#      Lines > 1: row col # coords of live cell
#
#   The user is prompted for the format in which to save.
#   The format of existing files is autodetected when read.
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
        self.cells = next_cells
       
    def load(self, filename):
        ''' Load universe state from file filename. '''
        # TODO write method body here
        pass

    def save(self, filename):
        ''' Save universe state to file filename. '''
        # TODO write method body here
        pass

if __name__ == '__main__':
    import sys

    BANNER = '''
    ================================
    Welcome to Conway's Game of Life
    --------------------------------
    '''
    MENU = '''Options:
        a : Age universe one generation
        m : Age universe multiple generations
        s : Save universe to disk
        l : Load universe from disk
        q : Quit program
    '''

    # Welcome the user
    print(BANNER)

    # Initialize the universe
    init_type = input('Initialize randomly (r) or from file (f)? ')

    if init_type == 'r':
        u_rows = int(input('Number of rows in universe? '))
        u_cols = int(input('Number of columns in universe? '))
        u = Universe(u_rows, u_cols)
        live_pct = int(input('Initial percentage of live cells? '))
        u.randomly_seed(live_pct)
                    
    elif init_type == 'f':
        u = Universe() # Create empty universe.
        fname = input('Name of file to read from? ')
        u.load(fname)

    else:
        print('Fatal Error: Choice not recognized. Universe not created.')
        sys.exit(1)

    # Display the initial universe
    print(u)

    # Main event loop:
    done = False
    while not done:
        # Get user command
        print(MENU)
        command = input('Command (a|m|s|l|q): ')

        # Age universe one or more generations
        if command == 'a' or command == 'm':
            if command == 'a':
                generations = 1
            else:
                generations = int(input('How many generations? '))

            for generation in range(0, generations):
                u.age()
                print(u)

        # Save state of universe to a file
        elif command == 's':
            fname = input('Name of file to save to? ')
            u.save(fname)

        # Load a saved  universe from a file
        elif command == 'l':
            fname = input('Name of file to load from? ')
            u.load(fname)
            print(u)

        # Quit
        elif command == 'q':
            done = True

        # PEBKAC
        else:
            print('Command not recognized. Please try again.')
