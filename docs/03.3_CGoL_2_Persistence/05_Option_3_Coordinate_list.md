# Option 3: Store only the coordinates of live cells

You will have noticed when playing the online games of life (you did
play them didn’t you?) that the universe is usually “sparse”, that is
there are usually relatively few live cells among a great many dead
ones. This is a consequence of Conway’s rules: cells die easily of
overcrowding so if an area becomes densely populated the cells in it
quickly die off keeping overall densities low. This suggests that we may
be wasting space storing all those dead cells in Options 1 and 2.
Instead we should just store the locations of live cells. Our file
format for the universe above would then be:

    8 8
    2 3
    3 4
    4 2
    4 3
    4 4

where each row after the first one records the location of a live cell
in `row col` form, i.e.the first number gives the row of the cell and
the second gives its column. What about the 8s in the first row? With
this representation the file does not directly convey the size of the
universe as it did in the first two options so we must explicitly state
the size of the universe, it’s the job of the first line of data to
give the height and width of the universe.

## Evaluation

How is this format?

You will have the chance to evaluate the difficulty of reading and
writing this format when you do it for this week’s assignment.

Evaluating the size of the representation on disk is interesting because
the storage requirement of this option depends not on the size of the
universe but on the number of live cells in it. For a universe less than
11 × 11 in size it uses 4 bytes per live cell (1 for row, 1 for
separating space, 1 for col and 1 for line end), plus another 4 for the
universe size. Generalizing: 4_n_ + 4 bytes where _n_ gives the number
of live cells.

(Note that the memory storage is _affected_ by the size of the universe
just not solely determined by it. This is because more bytes are
required to represent the row and column coordinates the larger the
universe is. In a 1,000 × 1,000 universe most coordinates will be 3
digit numbers, e.g. (148, 763) so most lines will be 8 bytes long and
the formula will become 8_n_ + 8 bytes).

How does this compare with the first two options? For this specific
example it uses 24 bytes. As long as the universe is sparse it will be
more efficient, but for a crowded universe it will be less efficient. We
can calculate the point at which it ceases to become more efficient by
finding the number of live cells at which the storage for two schemes is
equal. Assuming a 1,000 × 1,000 universe Option 1 will require 2,001,000
bytes, Option 2 will require 1,001,000 bytes, and Option 3’s
requirements will vary with the percentage of live cells:

| % live cells     | 0 | 5       | 10      | 15        | 20        | 25        |
|------------------|---|---------|---------|-----------|-----------|-----------|
| Storage in bytes | 8 | 400,008 | 800,008 | 1,200,008 | 1,600,008 | 2,000,008 |


You can see that for this size universe the break even point is around
25% live cells.
