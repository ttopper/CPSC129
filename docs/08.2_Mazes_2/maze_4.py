# maze_4.py
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

BORDER_WIDTH = 20
WALL_COLOR = WHITE
BACKGROUND_COLOR = BLACK

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

    def display(self):
        # Draw entire grid then draw doors as black lines over top.
        # Draw horizontal lines.
        for r in range(0, self.width + 1):
            pygame.draw.line(self.screen, GREY,
                             (0, r*self.grid_size), # From (x, y)
                             (self.screen_width, r*self.grid_size) # To (x, y)
                             )
        # Draw vertical lines.
        for c in range(0, self.height + 1):
            pygame.draw.line(self.screen, GREY,
                             (c*self.grid_size, 1),
                             (c*self.grid_size, self.screen_width)
                             )
        pygame.display.flip()

        # Now draw doors where necessary.
        for r in range(self.height):
            for c in range(self.width):
                # Always check for North and West doors.
                # Door in North wall?
                if self.cells[r][c].north.state == DOOR:
                    # print 'Found a North door at:', r, ',', c
                    # Draw a black line segment over the grey wall line.
                    pygame.draw.line(self.screen, BLACK,
                                     (c*self.grid_size + 1, r*self.grid_size),
                                     (c*self.grid_size + 16, r*self.grid_size)
                                     )
                if self.cells[r][c].west.state == DOOR:
                    # print 'Found a West door at:', r, ',', c
                    # Draw a black line segment over the grey wall line.
                    pygame.draw.line(self.screen, BLACK,
                                     (c*self.grid_size, r*self.grid_size + 1),
                                     (c*self.grid_size, r*self.grid_size + 16)
                                     )
                # Check for South doors only in bottom row (since South doors
                # above that are North doors for some higher cell).
                if r == self.height - 1:
                    if self.cells[r][c].south.state == DOOR:
                        # print 'Found a South door at:', r, ',', c
                        # Draw a black line segment over the grey wall line.
                        pygame.draw.line(self.screen, BLACK,
                                         (c*self.grid_size + 1, (r+1)*self.grid_size),
                                         (c*self.grid_size + 16, (r+1)*self.grid_size)
                                         )
                    
        pygame.display.flip()
                   
    def carve(self):
        # Select an "entrance" cell in the top outer wall.
        entrance_col = random.choice(range(self.width))
        # Remember where entrance is for later interaction.
        self.entrance = [0, entrance_col]
        # Break the exterior wall of entrance cell.
        self.cells[0][entrance_col].north.state = DOOR
        visited_path = []
        # Add entrance cell to visited_path
        visited_path.append([0, entrance_col])
        self.cells[0][entrance_col].visited = True
        # while visited_path is not empty:
        while visited_path:
            # print 'visited_path =', visited_path #  Debug
            # build list of current cell's visitable neighbours
            current_r, current_c = visited_path[-1]
            # print 'Current cell is', current_r, current_c # Debug
            # check four neighbours
            neighbour_coords = [[current_r-1, current_c], # North
                                [current_r, current_c+1], # East
                                [current_r, current_c-1], # West
                                [current_r+1, current_c]  # South
                               ]
            visitable = []
            for r, c in neighbour_coords:
                # if cell is inside the maze
                # and cell hasn't already been visited
                if r >= 0 and r < self.width and c >= 0 and c < self.height \
                   and not self.cells[r][c].visited:
                    # Add cell to visitable list
                    visitable.append([r, c])
            # print 'visitable =', visitable # Debug
            # if visitable list is not empty:
            if visitable:
                # pick a cell randomly from the list
                new_r, new_c = random.choice(visitable)
                print('Moving into', new_r, new_c)
                # [TT: moved upwards] break wall between cells
                if (new_r, new_c) == (current_r-1, current_c):
                    self.cells[current_r][current_c].north.state = DOOR
                elif (new_r, new_c) == (current_r, current_c+1):
                    self.cells[current_r][current_c].east.state = DOOR
                elif (new_r, new_c) == (current_r, current_c-1):
                    self.cells[current_r][current_c].west.state = DOOR
                elif (new_r, new_c) == (current_r+1, current_c):
                    self.cells[current_r][current_c].south.state = DOOR
                else:
                    print('BIG error: Invalid coords!')
                # make chosen cell be the current cell
                # add this [TT: was "previous"] cell to visited list
                visited_path.append([new_r, new_c])
                self.cells[new_r][new_c].visited = True
            else: # list is empty
                # pop this cell off visited_path
                dummy = visited_path.pop()
                # and use one at end of visited_path as current cell
        # Randomly choose an exit point for the maze in bottom outer wall
        exit_col = random.choice(range(self.width))
        # Break the exterior wall of exit cell.
        self.cells[self.height-1][exit_col].south.state = DOOR
        # Remember where exit is for later interaction.
        self.entrance = [self.height-1, exit_col]
        

def break_walls(m):
    m.cells[0][0].east.state = DOOR
    m.cells[0][1].north.state = DOOR
    m.cells[1][1].north.state = DOOR
    m.cells[2][1].north.state = DOOR
    m.cells[2][1].east.state = DOOR
    m.cells[2][1].west.state = DOOR
    m.cells[2][2].south.state = DOOR
    m.cells[3][2].south.state = DOOR
    m.cells[4][2].south.state = DOOR
    m.cells[4][2].south.state = DOOR
    m.cells[4][2].south.state = DOO

if __name__ =='__main__':
    # Prepare maze.
    m = Maze(25, 25)
    # break_walls(m)
    # print m
    m.carve()
    m.display() # Using Pygame.
    
##    m = Maze(25, 25)
##    m.carve()
##    m.display() # Using Pygame.

    # Begin interactive portion of program.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
##            elif (event.type == pygame.KEYUP) or (event.type == pygame.KEYDOWN):
##                print event
   
        
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
