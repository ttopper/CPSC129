# Step 1: From English to Pseudocode

We are going to start by implementing the second approach. The first 
thing we are going to do is try and translate the english description to 
pseudocode. Here is my first pass.

```python
Generate a new maze with all walls standing.
The maze carving algorithm begins by selecting an "entrance" cell, 
opening the outside wall, and then following this algorithm:
    Pick a random direction, 
    move to the adjoining cell in that direction
    if you haven’t visited it before.
    Add the previous cell location to the list of visited cells.
    Knock out the wall between the cell you came from and the one you’re in, 
    then move to another randomly-selected adjacent cell.
    Repeat the process until you reach a place that is surrounded by cells that have all already been visited.
    At this point, work your way back through the list of visited cells
    until you find one that does have an unvisited neighbor, 
    and start carving again.
```

This has started to break the code into distinct actions, but they don't 
sound like python code. In particular there are some issues with how 
we've described the loops. The algorithm is actually a double loop, one 
loop until we find a cell that is surrounded, and then working back 
until we find a cell with an unvisited. Let's clean it up a little.

```python
Generate a new maze with all walls standing.
Select an "entrance" cell, 
opening the outside wall
while there are cells with unvisited neighbours
    while not all this cell's neighbours have been visited
        Pick a random direction, 
        move to the adjoining cell in that direction
        if you haven’t visited it before.
        Add the previous cell location to the list of visited cells.
        Knock out the wall between the cell you came from and the one you’re in, 
        then move to another randomly-selected adjacent cell.
    Work your way back through the list of visited cells
    until you find one that does have an unvisited neighbor, 
```

This tells us we have to keep carving as long as we have some cells that 
have never been reached. While at a given cell with unvisited neighbours 
pick a random direction that hasn't been visited. We are going to need 
to add some instructions to handle the cases where we accidentally pick 
a neighbour that has already been visited.


```python
Generate a new maze with all walls standing.
Select an "entrance" cell, 
opening the outside wall
while there are unvisited cells
    while not all this cell's neighbours have been visited
        Pick a random direction,
        if the cell in that direction hasn't been visited
            move to the adjoining cell in that direction
            Add the previous cell location to the list of visited cells.
            Knock out the wall between the cell you came from
    Work your way back through the list of visited cells
    until you find one that does have an unvisited neighbor, 
```

The added indentation gives us a better idea of the structure of the 
algorithm.