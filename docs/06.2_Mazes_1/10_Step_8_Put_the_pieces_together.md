# Step 8: Putting the pieces together

Here is the last version of the code before you finish the program for 
your assignment. We've added some comments, and included the pseudocode 
for the carve method. The display method in pygame will look very 
similar to our initialization code for the maze, in that you will need 
to loop through each cell and decide when to draw lines and when not to. 
There will also be a bit of arithmetic to decide the size of the cells.

```python
# maze_3.py
#
# A Maze is an array of Cells, each of which has four Walls,
# and may or may not have been visited.

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
        # Four walls:
        self.north = n
        self.east = e
        self.south = s
        self.west = w
        # Flag for whether it has been visited or not.
        self.visited = False

    def __str__(self):
        ''' Display to aid in development and debugging,
            NOT meant for users' eyes. '''
        s = ''
        s += str(self.north)
        s += str(self.east)
        s += str(self.south)
        s += str(self.west)
        if self.visited: s += 'V'
        else: s += 'U'
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
                    if c == 0: # Leftmost cell
                        #                 North       East       South      West
                        row.append( Cell(Wall(EXT), Wall(INT), Wall(INT), Wall(EXT)))
                    elif c == self.width - 1: # Rightmost cell
                        row.append( Cell(Wall(EXT), Wall(EXT), Wall(INT), row[c-1].east))                       
                    else: # Middle cells
                        row.append( Cell(Wall(EXT), Wall(INT), Wall(INT), row[c-1].east))
                elif r == self.height - 1: # Bottom row
                    if c == 0: # Leftmost cell
                        row.append( Cell(self.cells[r-1][c].south, Wall(INT), Wall(EXT), Wall(EXT)))
                    elif c == self.width - 1: # Rightmost cell
                        row.append( Cell(self.cells[r-1][c].south, Wall(EXT), Wall(EXT), row[c-1].east))                       
                    else: # Middle cells
                        row.append( Cell(self.cells[r-1][c].south, Wall(INT), Wall(EXT), row[c-1].east))
                else: # Interior row
                    if c == 0: # Leftmost cell
                        row.append( Cell(self.cells[r-1][c].south, Wall(INT), Wall(INT), Wall(EXT)))
                    elif c == self.width - 1: # Rightmost cell
                        row.append( Cell(self.cells[r-1][c].south, Wall(EXT), Wall(INT), row[c-1].east))                       
                    else: # Middle cells
                        row.append( Cell(self.cells[r-1][c].south, Wall(INT), Wall(INT), row[c-1].east))
            self.cells.append(row)

    def __str__(self):
        ''' Display to aid in development and debugging,
            NOT meant for users' eyes. '''
        s = ''
        for r in range(self.height):
            for c in range(self.width):
                s += str(self.cells[r][c])
                s += ' '
            s += '\n'
        return s

    def carve(self):
##        Generate a new maze with all walls standing.
##        Select an "entrance" cell in the top outer wall.
##        Break the exterior wall of this entrance cell.
##        visited_path = []
##        Add the entrance cell to visited_path
##        while visited_path isn't empty:
##            build list of curent cell's visitable neighbours
##                check four neighbours
##                    if cell is inside the maze
##                    and cell hasn't already been visited
##                        Add cell to visitable list
##            if visitable list is not empty:
##                pick a cell randomly from the list
##                make chosen cell be the current cell
##                add previous cell to visited list
##                break wall between the previous cell and this one
##            else: # list is empty
##                pop this cell off visited_path
##                and use the one at end of visited_path as current cell
##        Randomly choose an exit point for the maze in bottom outer wall
        pass

    def display(self):
        ''' Pygame display of maze. '''
        pass

if __name__ == '__main__':
    m = Maze(5,5)
    print(m)

    # Now check that wall references are truly shared between cells
    # we'll manually create this:
    ##  =======D======
    ##||  |  |  |  |  ||
    ##||--+--+--+--+--||
    ##||  |  D  |  |  ||
    ##||--+--+--+--+--||
    ##||  |  |  |  |  ||
    ##||--+--+--+D-+--||
    ##||  |  |  |  |  ||
    ##||--+--+--+--+--||
    ##||  |  |  |  |  ||
    ##  ==============
    m.cells[1][1].east.state = DOOR
    m.cells[0][2].north.state = DOOR
    m.cells[2][3].south.state = DOOR
    print(m)
    
    m = Maze(25, 25)
    m.carve()
    m.display() # Using Pygame.
    
```