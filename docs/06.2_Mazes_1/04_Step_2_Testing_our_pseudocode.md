# Step 2: Testing our pseudocode

Let's walk through our algorithm. First we have to `generate a new maze 
with all the walls standing`.

```python
 --------------
|  |  |  |  |  |
|--+--+--+--+--|
|  |  |  |  |  |
|--+--+--+--+--|
|  |  |  |  |  |
|--+--+--+--+--|
|  |  |  |  |  |
|--+--+--+--+--|
|  |  |  |  |  |
 --------------
```

The next step is to `select an entrance cell`. We will also add an 
asterisk to mark our current location

```python
 ---  ---------
|  | *|  |  |  |
|--+--+--+--+--|
|  |  |  |  |  |
|--+--+--+--+--|
|  |  |  |  |  |
|--+--+--+--+--|
|  |  |  |  |  |
|--+--+--+--+--|
|  |  |  |  |  |
 --------------
```

In general a maze cell only has 4 neighbours, but our starting cell has 
just 3 (one on the left, one below, and one on the right). None of our 
cell's neighbours have been visited. So we will begin the virst loop 
`while there are univisited cells` and the inner loop `while not all 
this cell's neighbours have been visited`. Then we will `pick a random 
direction` which will be to the right.

We `move to the adjoining cell in that direction` and `add the previous 
cell to the list of visited cells`. Then we need to `knock down the wall 
between the cell you came from`.

```python
 ---  ---------
|  | v  *|  |  |
|--+--+--+--+--|
|  |  |  |  |  |
|--+--+--+--+--|
|  |  |  |  |  |
|--+--+--+--+--|
|  |  |  |  |  |
|--+--+--+--+--|
|  |  |  |  |  |
 --------------
```

Now we have reached the end of our inner while loop so we will loop back 
to our logic and check to see if `not all this cell's neighbours have 
been visited`. Interestingly, this cell now refers to our new location. 
Not all of our current cells have been visited, so we will pick a random 
neighbour, if we picked our left neighbour the if condition would not 
let us execute, so we would select again. Let us imagine we picked the 
cell below.

```python
 ---  ---------
|  | v  v|  |  |
|--+--+  +--+--|
|  |  | *|  |  |
|--+--+--+--+--|
|  |  |  |  |  |
|--+--+--+--+--|
|  |  |  |  |  |
|--+--+--+--+--|
|  |  |  |  |  |
 --------------
```

I will walk this algorithm several times until we first exit the inner 
while loop because we reach a cell where all its neighbours have been 
visited.

```python
 ---  ---------
|  | v  v| *  v|
|--+--+  +--+  |
|  |  | v  v  v|
|--+--+--+--+--|
|  |  |  |  |  |
|--+--+--+--+--|
|  |  |  |  |  |
|--+--+--+--+--|
|  |  |  |  |  |
 --------------
```

At this stage we need to `Work your way back through the list of visited 
cells until you find one that does have an unvisited neighbor`.

I'm not sure what should happen to the cell at the deadend, so I will 
leave it as a question mark, and trace back to the most recent cell that 
still has an unvisited neighbour.

```python
 ---  ---------
|  | v  v| ?  v|
|--+--+  +--+  |
|  |  | v  v  *|
|--+--+--+--+--|
|  |  |  |  |  |
|--+--+--+--+--|
|  |  |  |  |  |
|--+--+--+--+--|
|  |  |  |  |  |
 --------------
```

Now we reenter the inner while loop and I will trace it until our next 
deadend.

```python
 ---  ---------
|  | v  v| ?  v|
|--+--+  +--+  |
|  |  | v  v  v|
|--+--+--+--+  |
|  |  | v  v  v|
|--+--+  +--+--|
|  |  | v| *  v|
|--+--+  +--+  |
|  |  | v  v  v|
 --------------
```
Now we trace back to the most recent cell that still has an unvisited 
neighbour.

```python
 ---  ---------
|  | v  v| ?  v|
|--+--+  +--+  |
|  |  | v  v  v|
|--+--+--+--+  |
|  |  | v  v  v|
|--+--+  +--+--|
|  |  | v| ?  v|
|--+--+  +--+  |
|  |  | *  v  v|
 --------------
```

We pick some more random directions until we hit a deadend.

```python
 ---  ---------
|  | v  v| ?  v|
|--+--+  +--+  |
|  |  | v  v  v|
|--+--+--+--+  |
|  |  | v  v  v|
|--+--+  +--+--|
| v  v| v| ?  v|
|  +  +  +--+  |
| *| v  v  v  v|
 --------------
```

So we backtrack.

```python
 ---  ---------
|  | v  v| ?  v|
|--+--+  +--+  |
|  |  | v  v  v|
|--+--+--+--+  |
|  |  | v  v  v|
|--+--+  +--+--|
| *  v| v| ?  v|
|  +  +  +--+  |
| ?| v  v  v  v|
 --------------
```

And we pick some more random directions until we hit a deadend.

```python
 ---  ---------
| *| v  v| ?  v|
|  +--+  +--+  |
| v|  | v  v  v|
|  +--+--+--+  |
| v|  | v  v  v|
|  +--+  +--+--|
| v  v| v| ?  v|
|  +  +  +--+  |
| ?| v  v  v  v|
 --------------
```

Then we backtrack.

```python
 ---  ---------
| ?| v  v| ?  v|
|  +--+  +--+  |
| *|  | v  v  v|
|  +--+--+--+  |
| v|  | v  v  v|
|  +--+  +--+--|
| v  v| v| ?  v|
|  +  +  +--+  |
| ?| v  v  v  v|
 --------------
```

And we pick some more random directions until we hit a deadend.

```python
 ---  ---------
| ?| v  v| ?  v|
|  +--+  +--+  |
| v  v| v  v  v|
|  +  +--+--+  |
| v| *| v  v  v|
|  +--+  +--+--|
| v  v| v| ?  v|
|  +  +  +--+  |
| ?| v  v  v  v|
 --------------
```

Then we backtrack. At this point there are no unvisited cells, so our 
backtracking will take us all the way back to our entrance. This changes 
our perception of the outer while loop a little. Instead of saying 
`while there are univisited cells` we can instead say `while the list of 
visited cells is not empty`. This means we will also need to add a cell 
to our list of visited cells before the loop.

```python
Generate a new maze with all walls standing.
Select an "entrance" cell, 
opening the outside wall
Put the entrance cell into visited list
while list of visited cells is not empty
    while not all this cell's neighbours have been visited
        Pick a random direction,
        if the cell in that direction hasn't been visited
            move to the adjoining cell in that direction
            Add the previous cell location to the list of visited cells.
            Knock out the wall between the cell you came from
    Work your way back through the list of visited cells
    until you find one that does have an unvisited neighbor, 
```

This generates a pretty cute little maze.

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
 --------------
```

The last missing piece to our maze is the exit. So the last line of our 
pseudocode should be to `randomly choose an exit point for the maze`. We 
don't want the entrance and exit to be too close to each other, so we 
will choose the entrance from the top and the exit from the bottom row.


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