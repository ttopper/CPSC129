# Where to Begin?

Let’s try and speed up our Game of Life program. We knew from our first
versions that displaying the game universe takes up a large majority of
the program’s running time, and on the previous assignment we found
that using Pygame is faster than displaying to the terminal. This moved
our program bottleneck from being the display of the universe to being
the aging portion of our program. Let’s turn our attention to this part
of the algorithm.

The source below shows a main loop of the program---the part that
matters most for speed because it is the only part executed more than
once. I have presented it as one monolithic code segment (i.e. no
functions) and removed class mechanisms to make the structure of the
algorithm as brief and clear as possible.

``` python
generations = int(input('How many generations to time? '))

for generation in range(0, generations):

    # Create next universe
    next_u = []
    for row in range(u_rows):
        next_u.append(u_cols*[0])

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

    # Replace universe with next universe
    u = next_u
    
    # Display the new universe
    # display(u)
```

Looking at the source we can see that the loop consists of four blocks
of code:

1.  Create the next universe,
2.  Age the universe,
3.  Replace the universe with the next universe, and
4.  Display the universe.

I’ve commented the display block out since we’ve already investigated
it.

Our experience with cryptarithms in CPSC 128 taught us to look first to
the most deeply nested loops to try and speed our code up. This makes
sense since the code in the innermost loops is the code executed the
most times, but it can be misleading when that nested code in fact runs
quickly and there is some very slow but unnested code elsewhere. In this
case that might be either of the other blocks which could plausibly take
a significant amount of time.

Which brings us to a key optimization guideline: **If you’re not
measuring, you’re guessing**. Since we’re supposed to be more like
pocket-protector-wearing engineers than Vegas gamblers (sorry if you
were hoping otherwise) let’s measure.
