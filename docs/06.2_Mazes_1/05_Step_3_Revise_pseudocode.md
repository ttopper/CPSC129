# Step 3: Revising our pseudocode

Let's look at the pseudocode and tidy it up a bit more. We are going to 
focus on increasing the efficiency of the instructions 
`Pick a random direction`, which will result in us picking an already 
visited cell (especially as we increase the amount of the maze that has 
already been visited).


```python
Generate a new maze with all walls standing.
Select an "entrance" cell in the top outer wall
opening the outside wall # unclear language what does opening mean?
# we need to make a visited list before we can add to it
Put the entrance cell into visited list
while list of visited cells is not empty:
    # this is wasteful, because we often pick a cell that has been visitied
    # instead we want to pick from a set of possible directions
    while not all this cell's neighbours have been visited
        Pick a random direction 
        if the cell in that direction hasn't been visited
            move to the adjoining cell in that direction
            Add the previous cell location to the list of visited cells.
            Knock out the wall between the cell you came from
    # this next steps will be triggered when the list of visited neighbours is empty
    Work your way back through the list of visited cells
    until you find one that does have an unvisited neighbor,
Randomly choose an exit point for the maze in the bottom outer wall
```

We are going to create a list of the current cell's vistiable neighbours 
and choose our next cell from that. If the list isn't empty we will 
select from it and continue through the inner loop, otherwise if it is 
empty we will backtrack to a neighbour that has unvisited neighbours.

```python
Generate a new maze with all walls standing.
Select an "entrance" cell in the top outer wall
break the exterior wall of the entrance cell
visited_cells = []
Add entrance cell to visited list
while list of visited cells is not empty
    build a list of the current cell's visitable neighbours
       check the four neighbours
          if cell is inside the maze and the cell hasn't been visited
              add cell to the visitable list
    if list is not empty
        pick a cell randomly from the list
        make chosen cell be the current cells
        add previous cell to visited list
        break wall between cells
    else # if the list is empty
        # we need to back up, pop would be helpful
        set current cell to be be visited_cells[index-1]
Randomly choose an exit point for the maze in the bottom outer wall
```

The list of visited cells should also store the order that we visited 
them. We did this naturally when we walked through the algorithm, but it 
should be explicit in our code. We are going to change our variable name 
from visited_cells to visited_path. When it is time to backtrack on our 
path we will use pop to remove the last cell from the path, so that we 
can continue back to a new branching point in our maze (a cell with an 
unvisited neighbour).


```python
Generate a new maze with all walls standing.
Select an "entrance" cell in the top outer wall
break the exterior wall of the entrance cell
visited_path = []
Add entrance cell to visited list
while visited_path is not empty
    build a list of the current cell's visitable neighbours
       check the four neighbours
          if cell is inside the maze and the cell hasn't been visited
              add cell to the visitable list
    if list is not empty
        pick a cell randomly from the list
        make chosen cell be the current cells
        add previous cell to visited list
        break wall between cells
    else # if the list is empty
        pop this cell off visited_path
        and use one at end of visited_path as current cell
Randomly choose an exit point for the maze in the bottom outer wall

# Some thoughts about how we will tell if a cell has been visited
How to tell is a cell has been visited:
    1) "Calculate" it by checking how many walls it has.
    2) Remember it, i.e. store that fact somewhere in cell (object).

```