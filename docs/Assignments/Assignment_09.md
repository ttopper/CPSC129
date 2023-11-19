# Assignment 9

## Problems

1.  (_10 marks_) Complete the implementation of
    [median_by_partn.py](../09.1_Median/05_m_by_p_3_terse.py.png) and
    [median_by_bounding.py](../09.1_Median/09_m_by_b_3.py.png).

    -   Ensure both functions work on all lists (Hint: During
        development they weren’t tested on lists with even numbers of
        entries). Be sure to include your tests in the file you submit
        so I can see them.

    -   Time them on random, ascending and descending lists of varying
        lengths. What order does each algorithm seem to be? What lists
        produce the best and worst case performances? Add this
        information to a docstring for each function so prospective
        users will know what to expect.

2.  (_10 marks_) Since it doesn’t move the values in the list around,
    the median by bounding approach can’t find the median until it
    reaches it as it works its way through the list. We saw this in the
    test code where the number of values considered depended on where in
    the list the median occurred (i.e. near the front or near the back).
    Does this make the running time of `median_by_bounding` more
    variable than that of `median_by_partn`? Show me some data to
    convince me of your answer.

3.  (_20 marks_) Write the spelling bee administration software
    described in [this week’s
    notes](../09.2_Data_Processing/02_Spelling_bee_The_problem.md).
    Try to make your code bullet proof, and use EasyGUI for user
    interactions.

## Logistics

-   Use the following naming scheme for your program files:,
    `a`_assignment#_`p`_problem#_`v`_version#_`.py` .
