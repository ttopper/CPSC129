# Linear Insertion Sort

As you saw in the video, linear insertion sort moves through the list
one position at a time, and leaves behind it a sorted list, so that at
any moment the portion of the list before the current position is
sorted, and the portion after the current position is unsorted.

<table border="1">
  <tbody>
    <tr>
      <td>These elements have been sorted</td>
      <td>These haven't</td>
    </tr>
  </tbody>
</table>

At each step it takes the next value, i.e. the first value in the
unsorted portion, and looks backward to insert it where it should go in
the already sorted portion of the list:

    for each position in the list
        insert the current element at the appropriate place in
        the already sorted (front) portion of the list

Not surprisingly this first description is not quite correct or
complete. A minor correction, and an expansion are required.

-   The minor correction is that we do not need to consider the first
    position in the list because there is no sorted list preceding it.
    Instead, we begin with the second element, asking if it is in the
    correct position relative to the first, and then continue on from
    there.

-   The expansion is to elaborate on how we insert the current element
    at the appropriate place in the already sorted portion of the
    list”. This can be broken into two steps, first finding its
    appropriate location, and second placing it there, leading us to
    this revised description:

    for each position in the list after the first
        find out where this value should be in the already sorted portion of the list
        place it there

Now the location of the current value we are considering should be
between a value smaller than it and one larger than it. We can find such
a location by scanning backward from the current position looking for a
value smaller than it. Either we will find one, or we will bump into the
front of the list (if the current value is smaller than any we have in
the list so far). In pseudocode we could write this (where the left
arrow, ←, means assignment and our list is called `lst` and has `n`
elements):

     
    proper_posn ← current_posn
    while proper_posn ≥ 0 and lst[proper_posn]<lst[proper_posn-1]
        proper_posn ← proper_posn - 1

When this loop ends `proper_posn` holds the index of the location where
we should place the current value. But how to place it there?

We cannot just swap it with whatever is there because this would upset
the ordering of the first part of the list. Instead we have to shift
everything down to and including `proper_posn` forwards one position to
make a spot for the current value and then we can insert the current
value in its proper position. This is the procedure shown in the video.
Of course before shifting everything forward we have to remove the
current value to a safe temporary location until its proper position has
been cleared, and when we shift things we have to do it from the back
rather than from the front, i.e. first we move the item behind the
current position into the current position, then move the one behind it
and so on.

In pseudocode this procedure can be represented as:

    tmp ← lst[current_posn]
    for posn ← current_posn down to proper_posn+1
        lst[posn] ← lst[posn-1]
    lst[proper_posn] ← tmp

Putting all the pseudocode together (and filling in the first statement)
gives:

    for current_posn ← 1 to n-1
        proper_posn ← current_posn
        while proper_posn ≥ 0 and lst[proper_posn] < lst[proper_posn-1]
            proper_posn ← proper_posn - 1
        tmp ← lst[current_posn]
        for posn ← current_posn down to proper_posn+1
            lst[posn] ← lst[posn-1]
        lst[proper_posn] ← tmp

_Exercise_: Simulate the pseudocode above on the list `lst` below. Draw
the state of the list at the end of each iteration of the main loop.
Does the pseudocode work?

     
    lst: 34 11 23 86 51 94 4

_Exercise_: What would happen if we tried to move elements out of the
way from front to back instead of back to front? That is starting from
the proper position and moving forward to the current position? In this
case the moving pseudocode might be:

        tmp ← lst[current_posn]
        for posn ← proper_posn to current_posn-1
            lst[posn] ← lst[posn-1]
        lst[proper_posn] ← tmp

Simulate the effect by hand on the data below. Fill in `proper_posn`
yourself.

    lst: 11 37 62 78 19 48 94 6
    current_posn: 4
    proper_posn: 

We can simplify our code a bit if we combine the steps so that we
immediately set aside the current value, then start shifting values
forward until we find one smaller than the current value (or bump into
the front of the list) and then insert the current value.

The resulting Python program is:

```python
# ins_sort.py
# Sorts list into ascending order.

def ins_sort(lst):
    ''' Sorts a list into ascending order.

    It does this by considering each value after the first one,
    and inserting it into the front (sorted) part of the list
    where it belongs. '''
    for i in range(1, len(lst)):
        tmp = lst[i]
        j = i-1
        while j >= 0 and tmp < lst[j]:
            lst[j+1] = lst[j]
            j = j-1
        lst[j+1] = tmp

if __name__=='__main__':
    l = [ 8, 3, 1, 9, 5, 6, 2, 4 ]
    print('Before: ', l)
    ins_sort( l )
    print('After: ', l)

    l = [ 8, 3 ]
    print('Before: ', l)
    ins_sort( l )
    print('After: ', l)

    l = [ 8 ]
    print('Before: ', l)
    ins_sort( l )
    print('After: ', l)

    l = [ ]
    print('Before: ', l)
    ins_sort( l )
    print('After: ', l)

    l = [ 8, 3, 8, 9, 8, 6, 3, 3 ]
    print('Before: ', l)
    ins_sort( l )
    print('After: ', l)
```
