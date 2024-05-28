# Assignment 2

## Problems

1. ### Complete the search code begun in the lecture.

    Specifically:

    a.  Fix the errors in the binary search function.

    b.  Create a binary search_i function.

    c.  Create an interpolativae search function.

    d.  Create an interpolativae search_i function.

    Ensure **all** the functions work correctly. (Hint: Don't forget to 
    ensure that they work on very short lists.)

2. ### A "pencil and paper"* exercise on algorithmic complexity.

    Submit your answers to the following in a text file.

    a.  An O(n) algorithm takes 13ms (milliseconds) to process an array 
    of 300 elements. How long will it take to process an array with 900 
    elements?

    b.  An O(n3) algorithm takes 5 seconds to process a file with 3,000 
    entries. How long will it take it to process a file with 8,000 
    entries?

    c.  An O(log n) algorithm takes 1 second to process a list of 1,000 
    elements. How long will it take to process a list with 4,000,000 
    elements?

    d.  An O(n2) algorithm takes 2 minutes to process a 100x100 pixel 
    image. How long will it take to process a 600x600 pixel image?

    e.  An O(2n) algorithm takes 4μs (microseconds) to process a list 
    with 100 elements. How long will it take to process a list with 
    12,000 elements?

    * "Pencil and paper" does not mean that it has to be done with 
    pencil and paper, it just points out that it can be and doesn't 
    require a program as an answer. The Python shell might provide a 
    convenient way of doing the calculations and you could submit the 
    Python expressions that calculate the answers, e.g. an answer for 
    a2p2e might be print((2**12000//2**100)*4, 'microseconds')

3. ### Write a pygame program that produces the output below:

    ![Conway's Game of Life Board.](../02.3_PyGame_1_Drawing/cgol_window.png)

    Tip 1: The program that produced this built upward from the lines:

        u_rows = 25
        u_cols = 40

    (In a few weeks we'll use this to display our life universes instead 
    of text output to the shell window.)

    Tip 2: The 100 cells are placed randomly so you don't have to 
    recreate this exact image.

    Tip 3: The 16x16 cell image is Blue cell.. Right-click on the image 
    below and do a save-as to get it.

    ![Blue Cell.](Aqua-Ball-icon.png)

    Tip 4: screen.blit() is your friend for pasting images onto the 
    screen.

## Logistics

-   Use the following naming scheme for your program files:
    `a`assignment#`p`problem#name`.py` . So Bob's solution to problem 1 on this assignment will be named `a2p1bob.py`.