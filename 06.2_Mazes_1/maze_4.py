# maze_3.py
#
# A Maze an array of Cells, each of which has four Walls, and may or may not have been visited.
import random
import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

BORDER_WIDTH = 20
WALL_COLOUR = WHITE
BACKGROUND_COLOUR = BLACK

(INT, EXT, DOOR) = list(range(3))
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

        # Initialize pygame
        pygame.init()

        self.player = pygame.image.load("Aqua-Ball-icon.png")
        self.cell_size = 16
        self.grid_size = self.cell_size + 1

        self.maze_height = self.height*self.grid_size + 1
        self.maze_width = self.width*self.grid_size + 1
        self.screen_width = self.maze_width + 2*BORDER_WIDTH
        self.screen_height = self.maze_height + 2*BORDER_WIDTH
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen.fill(BACKGROUND_COLOUR)
        pygame.display.flip()

    def __str__(self):
        s = ''
        for r in range(self.height):
            for c in range(self.width):
                s += str(self.cells[r][c])
            s += '\n'
        return s

    def carve(self):
        #Generate a new maze with all walls standing.
        #Select an "entrance" cell in the top outer wall.
        col = random.choice(range(self.width))
        #Break the exterior wall of entrance cell.
        self.cells[0][col].north.state = DOOR
        self.cells[0][col].visited = True
        visited_path = []
        #Add entrance cell to visited_path
        visited_path.append([0, col])
        #while visited_path is not empty:
        while visited_path:
            # Use cell at end of visited_path as current cell.
            row, col = visited_path[-1]
            #build list of current cell's visitable neighbours
            #check four neighbours
                #if cell is inside the maze
                #and cell hasn't already been visited
                    #Add cell to visitable list
            visitable = []
            # North
            if row-1 >= 0 and row-1 < self.height and not self.cells[row-1][col].visited:
                visitable.append([row-1, col])
            # South
            if row+1 >= 0 and row+1 < self.height and not self.cells[row+1][col].visited:
                visitable.append([row+1, col])
            # East
            if col+1 >= 0 and col+1 < self.width and not self.cells[row][col+1].visited:
                visitable.append([row, col+1])
            # West
            if col-1 >= 0 and col-1 < self.height and not self.cells[row][col-1].visited:
                visitable.append([row, col-1])
                
            #if visitable list is not empty:
            if visitable:
                #pick a cell randomly from the list
                new_row, new_col = random.choice(visitable)
                #make chosen cell be the current cell : not necessary
                #add current [XX] cell to visited list
                visited_path.append([new_row, new_col])
                # [XX] change status of new cell to visited
                self.cells[new_row][new_col].visited = True
                #break wall between cells
                if new_row == row-1: # New cell is to North of old cell
                    self.cells[new_row][new_col].south.state = DOOR
                elif new_row == row+1: # South
                    self.cells[new_row][new_col].north.state = DOOR
                elif new_col == col-1: # West
                    self.cells[new_row][new_col].east.state = DOOR
                else:
                    self.cells[new_row][new_col].west.state = DOOR
                    
            else: # list is empty
                #pop this cell off visited_path
                visited_path.pop()
                #and use one at end of visited_path as current cell
        #Randomly choose an exit point for the maze in bottom outer wall
        col = random.choice(range(self.width))
        #Break the exterior wall of entrance cell.
        self.cells[self.height-1][col].south.state = DOOR

    def display(self):
        # Draw entire grid then draw doors as BACKGROUND_COLOUR lines over top.
        # Draw horizontal lines.
        for r in range(0, self.width + 1):
            pygame.draw.line(self.screen, WALL_COLOUR,
                             (BORDER_WIDTH+0, BORDER_WIDTH+r*self.grid_size), # From (x, y)
                             (BORDER_WIDTH-1+self.maze_width, BORDER_WIDTH+r*self.grid_size) # To (x, y)
                             )
        # Draw vertical lines.
        for c in range(0, self.height + 1):
            pygame.draw.line(self.screen, WALL_COLOUR,
                             (BORDER_WIDTH+(c*self.grid_size), BORDER_WIDTH+1),
                             (BORDER_WIDTH+(c*self.grid_size), BORDER_WIDTH-1+self.maze_width)
                             )
        pygame.display.flip()

        # Now draw doors where necessary.
        for r in range(self.height):
            for c in range(self.width):
                # Always check for North and West doors.
                # Door in North wall?
                if self.cells[r][c].north.state == DOOR:
                    # print 'Found a North door at:', r, ',', c
                    # Draw a BACKGROUND_COLOUR line segment over the WALL_COLOUR wall line.
                    pygame.draw.line(self.screen, BACKGROUND_COLOUR,
                                     (BORDER_WIDTH+c*self.grid_size + 1, BORDER_WIDTH+r*self.grid_size),
                                     (BORDER_WIDTH+c*self.grid_size + 16, BORDER_WIDTH+r*self.grid_size)
                                     )
                if self.cells[r][c].west.state == DOOR:
                    # print 'Found a West door at:', r, ',', c
                    # Draw a BACKGROUND_COLOUR line segment over the WALL_COLOUR wall line.
                    pygame.draw.line(self.screen, BACKGROUND_COLOUR,
                                     (BORDER_WIDTH+c*self.grid_size, BORDER_WIDTH+r*self.grid_size + 1),
                                     (BORDER_WIDTH+c*self.grid_size, BORDER_WIDTH+r*self.grid_size + 16)
                                     )
                # Check for South doors only in bottom row (since South doors
                # above that are North doors for some higher cell).
                if r == self.height - 1:
                    if self.cells[r][c].south.state == DOOR:
                        # print 'Found a South door at:', r, ',', c
                        # Draw a BACKGROUND_COLOUR line segment over the WALL_COLOUR wall line.
                        pygame.draw.line(self.screen, BACKGROUND_COLOUR,
                                         (BORDER_WIDTH+c*self.grid_size + 1, BORDER_WIDTH+(r+1)*self.grid_size),
                                         (BORDER_WIDTH+c*self.grid_size + 16, BORDER_WIDTH+(r+1)*self.grid_size)
                                         )
                    
        pygame.display.flip()

if __name__ =='__main__':
    m = Maze(25,25)
    #print(m)
##    m.cells[1][1].east.state = DOOR
##    m.cells[0][2].north.state = DOOR
##    m.cells[2][3].south.state = DOOR
    
    #m = Maze(25, 25)
    m.carve()
    #print(m)
    m.display() # Using Pygame.
    
    # Begin interactive portion of program.
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
   
        
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
