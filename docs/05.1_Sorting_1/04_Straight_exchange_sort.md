# Bubble Sort

The straight exchange sort, or Bubble Sort, operates by exchanging
neighbouring elements of the list if they are out of order. It keeps
scanning through the list making exchanges until the list is ordered. A
single pass through the list looks like this:

    for current_posn ← 0 to n-1
        if lst[current_posn] > lst[current_posn+1]
            swap lst[current_posn], lst[current_posn+1]

_Exercise_: Simulate this loop on the list:

    lst: 34 11 23 86 51 94 4

Notice that the largest value (94) is moved into the last position in
the list. This will always occur. How would you explain to someone why
it **must** happen?

Since after the first pass through the list the largest value is where
it belongs at the end of the list, the second pass only needs to loop to
the second last element, and since it will move the second largest
element into the second last position, the third iteration of the loop
only needs to loop to the third last position, and so on

So the complete bubble sort algorithm just places the single pass above
into an outer loop that controls the limit of the current scan.

    for end_posn ← n-1 down to 1
        for current_posn ← 0 to end_posn
            if lst[current_posn] > lst[current_posn+1]
                swap lst[current_posn], lst[current_posn+1]

_Exercise_: Simulate the pseudocode above on the list `lst` below. Draw
the state of the list at the end of each iteration of the main loop.
Does the pseudocode work?

    lst: 34 11 23 86 51 94 4

The video suggested an optimization. As expressed above the algorithm
will continue even after the list is sorted, but it could notice if the
list is sorted and stop. How could it notice? It could use a boolean
flag variable to remember if it made a swap on the last pass. If it
didn’t then all the elements of the list are in order and it can stop.
