
Generate a new maze with all walls standing.
Select an "entrance" cell in the top outer wall.
Break the exterior wall of entrance cell.
visited_path = []
Add entrance cell to visited_path
while visited_path isnot empty:
    build list of curent cell's visitable neighbours
        check four neighbours
            if cell is inside the maze
            and cell hasn't already been visited
                Add cell to visitable list
    if visitable list is no empty:
        pick a cell randomyl from the list
        make chosen cell be the current cell
        add previous cell to visited list
        break wall between cells
    else: # list is empty
        pop this cell off visited_path
        and use on at end of visited_path as current cell
Randomly choose an exit point for the maze in bottom outer wall

How to tell is a cell has been visited:
    1) "Calculate" it by checking how many walls it has.
    2) Remember it, i.e. store that fact in the cell.
       
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
