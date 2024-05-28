# Step 4: Data structures (OOP)

Before we consider our algorithm further, we first need to think about 
how we are going to refer to things like cells and walls. Let's start 
with our maze and think about how we are going to represent it. It is 
time to consider our objects. A maze has a grid or array of cells, and 
each one of those cells can have up to four walls. Walls can be broken 
up into two types: interior walls that are broken all the time and 
exterior walls that are only broken at the very beginning and end of the 
algorithm. Cells also need to track whether they've been visited or not. 

```python
 ---  ---------
|  |     |     |
|  +--+  +--+  |
|     |        |
|  +  +--+--+  |
|  |  |        |
|  +--+  +--+--|
|     |  |     |
|  +  +  +--+  |
|  |           |
   ------------
```

A maze is an array of cells, each of which has four walls, and may or 
may not have been visited.

Walls can be exterior, interior, or doors (broken walls).

Let's start to build some classes for this description.

```python
# maze_2.py

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
        self.cells = [] # we will need to initialize an array of cells

    def carve(self):
        pass

    def display(self):
        pass

if __name__ == '__init__':
    m = Maze(5,5)
    m.carve()
    m = m.display()

```

Next we need to flesh out our classes.