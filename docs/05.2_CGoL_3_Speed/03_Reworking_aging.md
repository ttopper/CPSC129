# Reworking Aging

This provides dramatic evidence that we should focus our attention on
the block of code responsible for aging the universe,

``` python
    # Age the universe:
    # Consider every cell in the universe
    for row in range(0, u_rows):
        for col in range(0, u_cols):    
            # Count its live neighbours
            neighbours = 0
            for r in range(row-1, row+2):
                for c in range(col-1, col+2):
                    if r >= u_rows: r = 0 # Handle toroidal universe
                    if c >= u_cols: c = 0 # Handle toroidal universe
                    neighbours += u[r][c]
            neighbours -= u[row][col]

            # Decide if it lives, dies or is born.
            if (u[row][col] == 1 and neighbours == 2) or neighbours == 3:
                next_u[row][col] = 1
```

Looking it over we see some quadruply nested code (in the innermost
`for` loop) and since cryptarithms in CPSC 128 we’ve known that nested
loops can be slow. Let’s see what we can do about them.

We take our lead from a second optimization guideline: **the fastest
code is code that isn’t there**, since if it isn’t there it takes no
time to run. Is there a way we can eliminate the innermost pair of
loops? (And it is important that we truly eliminate their computations,
not just push them into functions or class methods, or hide them via
calls to built-in functions like `count` or `find` which will still
involve iteration.) At first it might seem impossible since we do need
to know the number of live neighbours each cell has to correctly age the
universe, and it is true that we need to know this. But is looping over
each cell’s neighbourhood the only way to find it?

Consider the moment at which we discover that a cell dies. At that
instant we already know that each of its neighbours will have one fewer
live neighbour _in the next generation_. If we could record that right
then so we could remember it next time around we wouldn’t need to loop
over their neighbourhoods in the next generation. Now, where to record
this information? In a 2-D array of counts of each cell’s neighbours.
We’d have to initialize this neighbour array before beginning the main
loop, but then inside the loop we could just refer to it to determine if
cells live or die without having to loop over their neighbourhoods. We
won’t have done away with _all_ looping, since when a cell changes
state, we will have to loop over its neighbours in the neighbour array
changing their counts for the next generation, but since only a fraction
of the cells in the universe change state each generation this should be
much faster than looping over every cell in the universe’s
neighbourhoods.

## There’s always a complication

If you’ve thought about that long enough to make it clear in your mind
there is one complication to keep in mind, but it is not a new one: We
can’t change the neighbour array as we loop through the universe
because that could lead to incorrect aging, we have to change the
neighbour array _for the next generation_. I say this is not a new
complication because it is the same issue we faced when changing the
universe. The solution is also the same: we need two copies of the
neighbour array, just as we did for the universe array, one current one,
and one for the next generation.
