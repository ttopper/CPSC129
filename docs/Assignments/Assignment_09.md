# Assignment 9

## Problems

1.  (*10 marks*) Complete the implementation of
    [median_by_partn.py](../09.1_Median/05_m_by_p_3.py.) and
    [median_by_bounding.py](../09.1_Median/09_m_by_b_4.py).

    -   Ensure both functions work on all lists (Hint: During
        development they weren’t tested on lists with even numbers of
        entries). Be sure to include your tests in the file you submit
        so I can see them.

    -   Time them on random, ascending and descending lists of varying
        lengths. What order does each algorithm seem to be? What lists
        produce the best and worst case performances? Add this
        information to a docstring for each function so prospective
        users will know what to expect.

2.  (*10 marks*) Since it doesn’t move the values in the list around,
    the median by bounding approach can’t find the median until it
    reaches it as it works its way through the list. We saw this in the
    test code where the number of values considered depended on where in
    the list the median occurred (i.e. near the front or near the back).
    Does this make the running time of `median_by_bounding` more
    variable than that of `median_by_partn`? Show me some data to
    convince me of your answer.

3.  (*20 marks*) Write the spelling bee administration software
    described in [this week’s
    notes](../09.2_Data_Processing/02_Spelling_bee_The_problem.md).
    Try to make your code bullet proof, and use EasyGUI for user
    interactions.

## Logistics

-   Use the following naming scheme for program files: 
    `a`assignment#`p`problem#name`.py` . So Bob's solution to problem 1 
    on this assignment will be named `a9p1bob.py`
