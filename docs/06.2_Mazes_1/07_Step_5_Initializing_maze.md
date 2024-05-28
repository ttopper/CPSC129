# Step 5: Initializing the maze

The maze will need to be initialized at the beginning or our program. It 
will have only interior and exterior walls (no doors). The exterior 
walls will only be associated with our first and last rows and columns. 
That means that the interior cells will be initialized slightly 
differently than our outside cells. The interior cells will all have 4 
interior walls. The corners will have 2 exterior walls and 2 interior 
walls. The rest of the exterior cells will have 3 interior walls and 1 
exterior wall. We are going to consider the top, bottom, and middle rows 
as separate cases. In each of those cases we will consider the left, 
right, and middle columns separately.


```python
 ==============
||  |  |  |  |  ||
||--+--+--+--+--||
||  |  |  |  |  ||
||--+--+--+--+--||
||  |  |  |  |  ||
||--+--+--+--+--||
||  |  |  |  |  ||
||--+--+--+--+--||
||  |  |  |  |  ||
 ==============
```


```python
# maze_2.py

# Define our wall states
(INT,EXT,DOOR) = list(range(3))
class Wall:
    def __init__(self,s):
        self.state = s # exterior, interior, or door

class Cell:
    def __init__(self, n, e, s, w):
        self.north = n
        self.east = e
        self.south = s
        self.west = w
        self.visited = False

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

    def carve(self):
        pass

    def display(self):
        pass

if __name__ == '__main__':
    m = Maze(5,5)
    m.carve()
    m.display()

```

To test that this code is working we are going to need to work on our display.