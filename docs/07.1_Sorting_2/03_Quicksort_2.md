# A more Pythonic Quicksort

The first version of Quicksort we developed followed Sorting out
Sorting’s directions closely and so referred to portions of the list
using index ranges (the `lo` and `hi` variables in the code). This is
the approach that has to be taken in most traditional high level
languages, e.g. Pascal, or C and its descendants. It works though it
takes some careful testing to make sure it works on all types of lists
(as you will find on Problem 1 of the assignment). The film Sorting Out
Sorting presented the algorithm in terms of swapping values by index
because that was how the languages of the day worked.

Python on the other hand has language constructs that make creating and
combining lists very easy and these can simplify the process of writing
the program and of getting it working.

Recall our pseudocode for the Quicksort:

    Set the first element to be the pivot
    Separate all the smaller values from all the larger values by
       Scanning forward from the front of the list for a larger value
       Scanning from the back of the list for a smaller value
       if lo < hi: Interchange the two values
       Continue until lo > hi (all values are separated)
    Swap pivot with hi value (Move pivot into "middle")
    Call recursively on both sides of list

We can restate this to be less index focussed:

    Set the first element to be the pivot
    Separate all the smaller values from all the larger values by
    Scanning through the entire list and
       Placing values smaller than the pivot into a list called smaller
       And the values larger than the pivot into a list called larger
    Then call Quicksort on smaller
    And on Larger
    And finally return the concatenation of smaller, the pivot, and larger

Translated into Python this gives us,

``` python
# quicksort_v2.py

def qsort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    smaller = []
    larger = []
    for item in lst[1:]:
        if item <= pivot:
            smaller.append(item)
        else:
            larger.append(item)
    # print(smaller, '+', pivot, '+', larger)
    return qsort(smaller) + [pivot] + qsort(larger)

l = [49, 12, 67, 87, 21, 94, 24, 73, 69, 34]
print(qsort(l))
```

Notes:

-   I have left my debugging `print` statement in. It is quite
    instructive to study the output it produces on different types of
    lists.

-   Note that it is not a drop-in replacement for our earlier version
    because it _returns_ a sorted version of the list rather than
    sorting the list *in-place*. To create a drop-in replacement you
    would need to add a wrapper function around this one to call it and
    assign its return value to the original list.

## Magic can be dangerous

Given that this one is easier to get working and more readable than our
first version why would we ever use the first approach? One reason is
that not all languages allow the second approach. Another is that the
second approach is somewhat opaque. We don’t know exactly what is
happening in memory when we whip the smaller and larger lists into
being. Are they taking up more memory? A lot or a little? Does it take
very long to create them? The only way to find out is to time the
competing versions and see what the cost of easier programming is. You
will be doing that as part of the assignment.
