# Assignment 1

## Problems

1. ### Game of Life

    Complete the Game of Life program begun in the screencasts and make the following improvements:

-   Allow the user to choose between the current random display or starting with a predefined shape. 
    You should include at least the following shapes for the user to choose between: Block, Blinker, 
    Beacon, Glider, and Acorn. (This feature is mostly to simplify debugging.)
-   Try to express the aging logic more compactly than the current cascade of if-elif-elif-elif-else.
-   Implement a toroidal universe where the top boundary of the universe is attached to the bottom 
    boundary and the left boundary is attached to the right boundary.
    Hint: You may recall that because of the way it deals with negative indices Python is making half 
    of each of these connections already, e.g. it has connected the top edge to the bottom edge (but 
    not the bottom to the top) and the left to the right (but not vice versa).
-   In the current implementation we have to create a new next universe (next_u) every generation. 
    This must take some time. Try to have your code reuse the existing u and next_u objects instead of 
    creating new ones.

2. ### Establish a Baseline

    One of the key themes of this course is algorithm refinement and this is one of the algorithms we 
    will be revisiting and refining. Let's establish a baseline against which we can compare our 
    refinements. Submit a second version of your program that is instrumented to record and display 
    the time it takes your program to,

-   Initialize the universe.
-   Display the universe
-   Age the universe
-   Run, i.e. the total run time (this should be approximately the sum of the first three values).

    As well as your program submit a sample output run for the first 50 generations of the Acorn 
    starting configuration using a 25x80 universe. This will let us compare implementations and 
    our computers — which is always fun.

    You may want to refresh your memory about timing by consulting [Timing Programs](https://ttopper.github.io/CPSC128/04_Repetition/30_Timing_programs/) from CPSC 128.

## Logistics

-   Use the following naming scheme for your program files:
    `a`assignment#`p`problem#name`.py` . So Bob's solution to problem 1 on this assignment will be named `a1p1bob.py`.