# Assignment 2

## Problems

1.  Complete the search code begun in the screencasts. Specifically:
    a.  Add a `bin_search_i` function.

    b.  Add an `interp_search` function.

    c.  Add an `interp_search_i` function.

    d.  Ensure **all** the functions work correctly. (Hint: Don’t
        forget to ensure that they work on very short lists.)

2.  A pencil and paper” exercise on algorithmic complexity. Submit
    your answers to the following in a text file.

    a.  An O(n) algorithm takes 13ms (milliseconds) to process an array
        of 300 elements. How long will it take to process an array with
        900 elements?

    b.  An O(n<sup>3</sup>) algorithm takes 5 seconds to process a file with
        3,000 entries. How long will it take it to process a file with
        8,000 entries?

    c.  An O(log n) algorithm takes 1 second to process a list of 1,000
        elements. How long will it take to process a list with 4,000,000
        elements?

    d.  An O(n<sup>2</sup>) algorithm takes 2 minutes to process a 100x100 pixel
        image. How long will it take to process a 600x600 pixel image?

    e.  An O(2<sup>n</sup>) algorithm takes 4μs (microseconds) to process a list
        with 100 elements. How long will it take to process a list with
        12,000 elements?

3.  Write a pygame program that produces the output below:

    ![Image of life
    universe.](../02.3_PyGame_1_Drawing/pygame_test_life_0.png)

    Tip 1: The program that produced this built upward from the lines:

        u_rows = 25
        u_cols = 40

    (In a few weeks we’ll use this to display our life universes
    instead of text output to the shell window.)

    Tip 2: The 100 cells are placed randomly so you don’t have to
    recreate this _exact_ image.

    Tip 3: The 16x16 cell image is ![Blue
    cell.](../04.3_PyGame_2_Animation/Aqua-Ball-icon.png){width="16"
    height="16"}. Right-click the image and do a save-as to get it.

    Tip 4: `screen.blit()` is your friend for pasting images onto the
    screen.

## Logistics

-   Use the following naming scheme for your program files:,
    `a`*assignment#*`p`*problem#*`v`*version#*`.py` . So your first
    attempt at problem 1 on this assignment will be named `a2p1v1.py`
    and your second attempt (should there be one) will be named
    `a2p1v2.py` .
