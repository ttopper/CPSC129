# Drawing something

![Image of pygame_test_3.py source code.](05_pygame2.png)

## Sample output:

![Sample output.](05_pygame2_output.png)

## Note

Note that the pygame coordinate system (and most other graphics
libraries too) places the origin in the upper left corner, has an x-axis
that runs horizontally to the right, and a y-axis that runs vertically
downward.

![The pygame coordinate
system.](05_pygame_coordinate_system.png)

This means that a pygame coordinate (x,y) refers to column x and row y
which is the opposite of the way lists of lists are addressed which is
(row, column) and yes this irritating and leads to bugs, so **be
aware!**
