# Step 7: Sharing walls

There is one problem with our representation. The interior walls between 
adjacent cells are shared. Right now if we knocked down a wall between 
two adjacent cells we would have to adjust the walls in two different 
cells (either the north of on and the south of the other, or the east of 
one and the west of the other). If we think about our maze, what we 
would actually like if for those two walls to be the same wall. We can 
do that by using a shared reference to the same `Wall` object in the 
adjacent `Cell`s. Shared references are commonly used when formatting 
tables on webpages or in Microsoft Word. This is also needed when adding 
borders to cells in Excel spreadsheets.

To see this problem we're going to manually take the east wall from the 
cell at position (1,1).

```python
if __name__ == '__main__':
    m = Maze(5,5)
    m.carve()
    m.display()
    print(m)
    m.cells[1][1].east.state = DOOR
    print(m)

```

The output of this code will look like this...

```python
EIIEU EIIIU EIIIU EIIIU EEIIU 
IIIEU IIIIU IIIIU IIIIU IEIIU 
IIIEU IIIIU IIIIU IIIIU IEIIU 
IIIEU IIIIU IIIIU IIIIU IEIIU 
IIEEU IIEIU IIEIU IIEIU IEEIU

EIIEU EIIIU EIIIU EIIIU EEIIU 
IIIEU IDIIU IIIIU IIIIU IEIIU 
IIIEU IIIIU IIIIU IIIIU IEIIU 
IIIEU IIIIU IIIIU IIIIU IEIIU 
IIEEU IIEIU IIEIU IIEIU IEEIU
```

Because we have not set up shared references the door appears in the 
east wall of `cell[1][1]`, but does not show up in the west wall of 
`cell[1][2]`. The problem is that every time we initialized a cell we 
created 4 new walls. That had to happen for the first cell, but after 
that we should have begun to share our references. We are going to do 
that by accessing the walls we've built using the indexes of those 
cells. The west wall of each new cell added to our row will be equal to 
the east wall of the previous cell in the row. We will use the same 
logic for the north walls in each subsequent row will be equal to the 
south wall of the cell above it.

```python
# maze_2.py

# Define our wall states
(INT,EXT,DOOR) = list(range(3))
class Wall:
    def __init__(self,s):
        self.state = s # exterior, interior, or door

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
        if self.visited: s+= 'V'
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
                if r == 0: # top
                    if c == 0: # top left
                        row.append(Cell(Wall(EXT), Wall(INT), Wall(INT), Wall(EXT)))
                    elif c == self.width - 1: # top right
                        row.append(Cell(Wall(EXT), Wall(EXT), Wall(INT), row[c-1].east))
                    else: # top middle
                        row.append(Cell(Wall(EXT), Wall(INT), Wall(INT), row[c-1].east))
                elif r == self.height - 1: # bottom
                    if c == 0: # bottom left
                        row.append(Cell(self.cells[r-1][c].south, Wall(INT), Wall(EXT), Wall(EXT)))
                    elif c == self.width - 1: # bottom right
                        row.append(Cell(self.cells[r-1][c].south, Wall(EXT), Wall(EXT), row[c-1].east))
                    else: # bottom middle
                        row.append(Cell(self.cells[r-1][c].south, Wall(INT), Wall(EXT), row[c-1].east))
                else: # middle
                    if c == 0: # left
                        row.append(Cell(self.cells[r-1][c].south, Wall(INT), Wall(INT), Wall(EXT)))
                    elif c == self.width - 1: # right
                        row.append(Cell(self.cells[r-1][c].south, Wall(EXT), Wall(INT), row[c-1].east))
                    else: # middle
                        row.append(Cell(self.cells[r-1][c].south, Wall(INT), Wall(INT), row[c-1].east))
            self.cells.append(row)

    def __str__(self):
        s = ''
        for r in range(self.height):
            for c in range(self.width):
                s += str(self.cells[r][c])
                s += ' ' # add a space after each cell
            s += '\n' 
        return s

    def carve(self):
        pass

    def display(self):
        pass

if __name__ == '__main__':
    m = Maze(5,5)
    m.carve()
    m.display()
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

```

I've added some more wall breaks, one in an exterior wall and two in 
interior walls. Let's see how they show up.

```python
EIIEU EIIIU EIIIU EIIIU EEIIU 
IIIEU IIIIU IIIIU IIIIU IEIIU 
IIIEU IIIIU IIIIU IIIIU IEIIU 
IIIEU IIIIU IIIIU IIIIU IEIIU 
IIEEU IIEIU IIEIU IIEIU IEEIU 

EIIEU EIIIU DIIIU EIIIU EEIIU 
IIIEU IDIIU IIIDU IIIIU IEIIU 
IIIEU IIIIU IIIIU IIDIU IEIIU 
IIIEU IIIIU IIIIU DIIIU IEIIU 
IIEEU IIEIU IIEIU IIEIU IEEIU 
```

Looking at this closely it looks like we now have working shared 
references. We've created some really robust data structure, with some 
built in debugging with our str routine. The next steps are to program 
the carve to create the maze, as well as an elegeant display to show our 
final product in pygame.