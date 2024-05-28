# Step 6: Adding debugging output

To debug this we are going to need to be able to dispay the current 
maze. That doesn't necessarily look like the pretty display we will 
eventually do with pygame, where we might not want to track things like 
exterior vs interior walls, or whether a cell has been visited. The 
display for debugging won't necessarily even look like a maze. We are 
going to do this by writing an `__str__` method. We will need to write 
an `__str__` method for the Maze, which call the `__str__` method of the 
Cell, which will call the `__str__` method of the Wall.


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
                        row.append(Cell(Wall(EXT), Wall(EXT), Wall(INT), Wall(INT)))
                    else: # top middle
                        row.append(Cell(Wall(EXT), Wall(INT), Wall(INT), Wall(INT)))
                elif r == self.height - 1: # bottom
                    if c == 0: # bottom left
                        row.append(Cell(Wall(INT), Wall(INT), Wall(EXT), Wall(EXT)))
                    elif c == self.width - 1: # bottom right
                        row.append(Cell(Wall(INT), Wall(EXT), Wall(EXT), Wall(INT)))
                    else: # bottom middle
                        row.append(Cell(Wall(INT), Wall(INT), Wall(EXT), Wall(INT)))
                else: # middle
                    if c == 0: # left
                        row.append(Cell(Wall(INT), Wall(INT), Wall(INT), Wall(EXT)))
                    elif c == self.width - 1: # right
                        row.append(Cell(Wall(INT), Wall(EXT), Wall(INT), Wall(INT)))
                    else: # middle
                        row.append(Cell(Wall(INT), Wall(INT), Wall(INT), Wall(INT)))
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

```

The output of this code will look like this...

```python
EIIEU EIIIU EIIIU EIIIU EEIIU 
IIIEU IIIIU IIIIU IIIIU IEIIU 
IIIEU IIIIU IIIIU IIIIU IEIIU 
IIIEU IIIIU IIIIU IIIIU IEIIU 
IIEEU IIEIU IIEIU IIEIU IEEIU
```