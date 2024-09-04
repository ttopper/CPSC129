# Quicksort

The portion of the film 
[_Sorting out Sorting_](https://youtu.be/plAi7kcqMNU?t=117) provides 
fairly detailed instructions for Quicksort:

    Set the first element to be the pivot
    Separate all the smaller values from all the larger values by
       Scanning forward from the front of the list look for a value larger than the pivot
       Scanning backwards from the end of the list look for a value smaller than the pivot
       if the larger value is to the left of the smaller value:
           Exchange the two values
       Continue this until the scanners cross (which means the values are separated)
    Move pivot into the "middle"
    Call recursively on both parts of the list

This sounds precise enough to be translated into Python, so let’s give
it a try.

`Set the first element to be the pivot`

If we call our list `lst`, this is just:

    ``` python
    pivot = lst[0]
    ```

`Scanning forward from the front of the list look for a value larger than the pivot`

This is a loop starting at the front of the list and moving toward
    the back looking for values larger than the pivot:

    ``` python
    lo = 1
    while lst[lo] < pivot:
        lo = lo + 1
    ```

    Why start `lo` at 1? Because we do not want to consider the pivot
    element itself which is in position 0. Note that this loop will stop
    at values greater than or equal to the pivot (not just greater
    than). Is this right? Hard to tell right now, but we’ll keep it in
    mind as a possible problem.

`Scanning backwards from the end of the list look for a value smaller than the pivot`

This is similar to above, but starting at the end of the list, and
    moving toward the front.

    ``` python
    hi = len(lst) - 1
    while lst[hi] > pivot:
        hi = hi - 1
    ```

`if the larger value is to the left of the smaller value:`

If the larger value is to the left of the smaller value, it’s
    index, `lo`, will be smaller than the smaller value’s index, `hi`:

    ``` python
    if lo < hi:
    ```

`Exchange the two values`

We can use the old tuple trick” to swap the values,

    ``` python
    (lst[lo], lst[hi]) = (lst[hi], lst[lo])
    ```

`Continue this until the scanners cross (which means the values are separated)`

    _Continue_ and _until_ indicate we need to loop. Python does not
    support _until_ loops so we’ll have to reverse the logic to express
    it as a `while` loop. This means that _until_ the scanners cross”
    becomes, _While_ the scanners _haven’t_ crossed”. This while
    statement goes at the top of the loop body:

    ``` python
    while lo < hi:
    ```

Let’s put these pieces together and see what we have so far:

``` python
    pivot = lst[0]
    while lo < hi:

        lo = 1
        while lst[lo] < pivot:
            lo = lo + 1

        hi = len(lst) - 1
        while lst[hi] > pivot:
            hi = hi - 1

        if lo < hi:
            (lst[lo], lst[hi]) = (lst[hi], lst[lo])
```

Obviously the initialization of `lo` and `hi` should be moved outside
the loop,

``` python
    pivot = lst[0]
    lo = 1
    hi = len(lst) - 1
    while lo < hi:
        while lst[lo] < pivot:
            lo = lo + 1
        while lst[hi] > pivot:
            hi = hi - 1
        if lo < hi:
            (lst[lo], lst[hi]) = (lst[hi], lst[lo])
```

The last bits to complete the function are to exchange the pivot into
position and call the function again. Watching the film we can see that
the pivot is exchanged with the element where the index `hi` ends up.
And calling the sort on each part of the list just requires us to
package our code into a function and call it on each part:

``` python
# quicksort_v1.py

def quicksort(lst):
    print('Before:', lst)
    pivot = lst[0]
    lo = 1
    hi = len(lst) - 1
    while lo < hi:
        while lst[lo] < pivot:
            lo = lo + 1
        while lst[hi] > pivot:
            hi = hi - 1
        if lo < hi:
            (lst[lo], lst[hi]) = (lst[hi], lst[lo])
    if lst[0] > lst[hi]:
        (lst[0], lst[hi]) = (lst[hi], lst[0])
    print('After:', lst)
    quicksort(lst[0:hi])
    quicksort(lst[lo:])
    
l = [49, 12, 67, 87, 21, 94, 24, 73, 69, 34]
print(quicksort(l))
```

The first problem on the assignment asks you to get this code working
because it doesn’t quite work as written above. Not because I have
intentionally introduced errors, but because English descriptions just
aren’t as precise as programs --- if they were we’d be able to program
in English instead of learning new languages! No the code above just
needs to be tightened up a bit. After all this code has not been created
to lead you astray, but to lead you toward a working program. The key is
to test it on different kinds of lists and tackle the bugs that each
reveals. I believe that I made four smallish changes to the program to
get it to work on all lists.

Hint: The first problem is that it does not have an end condition to
stop the recursive calls. Once you see the error message think about
what lists do not need sorting and add in an appropriate condition to
halt the recursion.

(I have left in the `print` statements I used during my own debugging
since I found them helpful.)
