# Assignment 5

## Problems

1. Translate the pseudocode for the straight selection and bubble sort 
algorithms into working Python programs. Include tests to ensure they 
are working!

2. Create a module that imports and times all four of this week's 
sorting methods. Your code should time them on ascending, descending 
and random ordered lists of lengths 1, 2, 4, 8, 16, 32, 64, 128, 256, 
512, 1024, 2048, 4096, and 8192 and output neatly tabulated results 
(for easy importing into Excel or other graphing programs). You can 
use even longer lists if the code isn't taking too long to run (it 
all depends on your computer). Submit graphs of your results. Do they 
confirm those in the film Sorting Out Sorting?

3. The New Hacker's Dictionary defines Bogosort as follows:

    Bogo-sort: Repeatedly throw a hand of cards in the air, picking 
    them up at random, and stopping the process when examining the 
    hand reveals the cards are in order.

We can approximate the Bogosort method by taking our unsorted list, 
randomly swapping two values and checking to see if the list is now 
in order. If it is, we are done, if it isn't, we make another random 
swap and check again.

The pseudocode might look like this:

    bogosort(lst) 
        while  not is_sorted(lst)
            swap two randomly chosen items in lst

As you can see it is a blessedly brief procedure. But is it any good?

- Write a working bogosort function.

- What is the fewest swaps required to sort a list?

- What is the most swaps required?

- How would you characterize the performance of this algorithm, i.e. 
what order, O(), is this procedure? (including the computations 
within the calls to is_sorted()).

Answer the questions in the comments.

4. Speed up your simulation of Conway's Game of Life by implementing a 
neighbours array or universe to reduce the time spent in aging the 
universe. How much faster does this make the aging portion of your code? 
Answer in the comments.

## Logistics

-   Since they are single-file applications Problems 2, 3, and 4 can use 
    our usual naming scheme for program files: 
    `a`assignment#`p`problem#name`.py` . So Bob's solution to problem 3 
    on this assignment will be named `a5p3bob.py`. For Problem 1 you can 
    use the names straight_sort_name.py and bubble_sort_name.py where 
    name is your name. Please also submit an excel spreadsheet with your 
    graph for problem 2 called `a`assignment#`p`problem#name`.xlsx`.