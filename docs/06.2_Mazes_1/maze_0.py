Generate a new maze with all walls standing.
Select an "entrance" cell
opening the outside wall
Put entrance cell into visited list
while list of visited cells is not empty::
    while not all this cell's neighbours have been visited      
        Pick a random direction
        if the cell in that direction hasn't been visited
            move to the adjoining cell in that direction
            Add the previous cell location to the list of visited cells.
            Knock out the wall between the cell you came from
    Work your way back through the list of visited cells
    until you find one that does have an unvisited neighbor


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
