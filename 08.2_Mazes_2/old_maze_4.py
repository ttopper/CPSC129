# maze_3.py
#
# A Maze is an array of Cells,
# each of which has four Walls,
# and may or may not have been visited.
import pygame
import random
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TEAL = (0, 128, 128)
YELLOW = (255, 255, 0)
GREY = (128,128,128)
SILVER = (192, 192, 192)

(INT, EXT, DOOR) = range(3)
class Wall:
    def __init__(self, s):
        self.state = s

    def __str__(self):
        s = ''
        if self.state == INT:
            s += 'I'
        elif self.state == EXT:
            s += 'E'
        elif self.state == DOOR:
            s += 'D'
        return s
            

class Cell:
    def __init__(self, n, e, s, w):
        self.north = n
        self.east = e
        self.south = s
        self.west = w
        self.visited = False

    def __str__(self):
        s = ''
        s += str(self.north)
        s += str(self.east)
        s += str(self.south)
        s += str(self.west)
        if self.visited: s += 'V'
        else: s += 'U'
        s += ' '
        return s

class Maze:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        
        # Build matrix of cells.
        self.cells = []
        for r in range(self.height):
            # Build a row of cells and append it to self.cells
            row = []
            for c in range(self.width):
                if r == 0: # Top row
                    if c == 0:
                        row.append( Cell(Wall(EXT), Wall(INT), Wall(INT), Wall(EXT)))
                    elif c == self.width - 1:
                        row.append( Cell(Wall(EXT), Wall(EXT), Wall(INT), row[c-1].east))                       
                    else:
                        row.append( Cell(Wall(EXT), Wall(INT), Wall(INT), row[c-1].east))
                elif r == self.height - 1: # Bottom row
                    if c == 0:
                        row.append( Cell(self.cells[r-1][c].south, Wall(INT), Wall(EXT), Wall(EXT)))
                    elif c == self.width - 1:
                        row.append( Cell(self.cells[r-1][c].south, Wall(EXT), Wall(EXT), row[c-1].east))                       
                    else:
                        row.append( Cell(self.cells[r-1][c].south, Wall(INT), Wall(EXT), row[c-1].east))
                else: # Interior row
                    if c == 0:
                        row.append( Cell(self.cells[r-1][c].south, Wall(INT), Wall(INT), Wall(EXT)))
                    elif c == self.width - 1:
                        row.append( Cell(self.cells[r-1][c].south, Wall(EXT), Wall(INT), row[c-1].east))                       
                    else:
                        row.append( Cell(self.cells[r-1][c].south, Wall(INT), Wall(INT), row[c-1].east))
            self.cells.append(row)

        # Initialize graphic parameters and display.
        pygame.init()

        self.player = pygame.image.load("Aqua-Ball-icon.png")
        self.cell_size = 16
        self.grid_size = self.cell_size + 1

        self.screen_height = self.height*self.grid_size + 1
        self.screen_width = self.width*self.grid_size + 1
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen.fill(BLACK)
        pygame.display.flip()

    def __str__(self):
        s = ''
        for r in range(self.height):
            for c in range(self.width):
                s += str(self.cells[r][c])
            s += '\n'
        return s

    def carve(self):
##        Generate a new maze with all walls standing.
##        Select an "entrance" cell in the top outer wall.
##        Break the exterior wall of entrance cell.
##        visited_path = []
##        Add entrance cell to visited_path
##        while visited_path isnot empty:
##            build list of current cell's visitable neighbours
##                check four neighbours
##                    if cell is inside the maze
##                    and cell hasn't already been visited
##                        Add cell to visitable list
##            if visitable list is not empty:
##                pick a cell randomly from the list
##                make chosen cell be the current cell
##                add previous cell to visited list
##                break wall between cells
##            else: # list is empty
##                pop this cell off visited_path
##                and use one at end of visited_path as current cell
##        Randomly choose an exit point for the maze in bottom outer wall
        pass

    def display(self):
        # Draw entire grid then draw doors as black lines over top.
        # Draw horizontal lines.
        for r in range(0, self.width + 1):
            pygame.draw.line(self.screen, GREY, (0, r*self.grid_size), (self.screen_width, r*self.grid_size))
        # Draw vertical lines.
        for c in range(0, self.height + 1):
            pygame.draw.line(self.screen, GREY, (c*self.grid_size, 1), (c*self.grid_size, self.screen_width))
        pygame.display.flip()
        
##        for r in range(self.height):
##            for c in range(self.width):
##                # Always check for top and left doors.
##                # Sometimes draw others too, see comments below for when.
##                if r == self.height - 1: # check for bottom door.

##                else: 
                        

if __name__ =='__main__':
    # Prepare maze.
    m = Maze(5,5)
    print(m)
    m.cells[1][1].east.state = DOOR
    m.cells[0][2].north.state = DOOR
    m.cells[2][3].south.state = DOOR
    print(m)
    
    m = Maze(25, 25)
    m.carve()
    m.display() # Using Pygame.

    # Begin interactive portion of program.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif (event.type == pygame.KEYUP) or (event.type == pygame.KEYDOWN):
                print(event)
   
        
##  ==============
##||  |  |  |  |  ||
##||--+--+--+--+--||
##||  |  D  |  |  ||
##||--+--+--+--+--||
##||  |  |  |  |  ||
##||--+--+--+--+--||
##||  |  |  |  |  ||
##||--+--+--+--+--||
##||  |  |  |  |  ||
##  ==============
