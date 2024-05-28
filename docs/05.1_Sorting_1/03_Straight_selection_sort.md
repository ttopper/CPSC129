# Straight Selection Sort

Like insertion sort, straight selection sort proceeds through the list
one position at a time, and like linear insertion it leaves a sorted
list behind it as it proceeds. However it behaves quite differently at
each position. Where linear insertion sort asks,

> Where in the already sorted portion of the list on my left should I
> insert this value?

Straight selection asks,

> Which of the unsorted values on my right belongs here in this
> location.

So where insertion sort scans to the left looking for the correct
location for this value, selection sort scans to the right looking for
the right value for this location.

So,

-   It begins by considering the first position in the list. Which value
    should go here, i.e. which value should come first in the list? Well
    since the list is to be sorted in ascending order the smallest value
    in the list should come first. So straight selection needs to find
    the smallest value in the list and place it here in the first
    position. To find the smallest value it scans the entire list
    looking for the smallest value. Once it has found it, it places it
    in the first position in the list. What does it do with the value
    that was in the first position? The most common solution is to swap
    it with the smallest value.

-   Next it considers the second position in the list. Which value
    should go here? The second smallest value in the list. Since the
    smallest value has been placed in the first position the second
    smallest value will be the smallest value in the remainder of the
    list, i.e. from the second position to the end of the list. To find
    it, straight selection scans the remainder of the list for the
    smallest value and swaps it with the value currently in the second
    position.

-   Then it considers the third position in the list, scans the
    remainder of the list (positions 3 through `n`) for the smallest
    remaining value and swaps it with the value currently in the third
    position.

The algorithm proceeds in this way up to the second last position in the
list. It need not explicitly consider the last position, because the
last number left should be the largest. (Another difference from
insertion sort. Linear insertion did not need to consider the first
value, but straight selection doesn’t need to consider the last value.)

We can summarize this algorithm as follows:

    for each position in the list
        find the smallest item in the remainder of the list
        swap it with the value in the current position

The second line implies another loop which scans the remainder of the
list looking for the smallest element. So we can expand the description
above to:

    for each position in the list
        set smallest position to be the current position
        for each remaining position in the list
            if the element at this position is smaller than the one at smallest position
                set smallest position to this position
        swap the values in the current position and the smallest position

Introducing variables into our description we get (and assuming we have
a list `lst` with `n` elements):

    for current_posn ← 0 to n-2
        smallest_posn ← current_posn
        for posn ← current_posn+1 to n-1
            if lst[posn] < lst[smallest_posn]
                smallest_posn ← posn
        swap lst[current_posn], lst[smallest_posn]

*Question*: If the current value in the list is also the smallest in the
remainder of the list this will perform an unnecessary swap. The
unnecessary swap could be avoided by changing the final line to,

        if l[current_posn] > l[smallest_posn]
            swap l[current_posn], l[smallest_posn]
     

Would this change make the program more efficient?

*Exercise*: Simulate the pseudocode above on the list `lst` below. Draw
the state of the list at the end of each iteration of the main loop.
Does the pseudocode work?

     
    lst: 34 11 23 86 51 94 4
