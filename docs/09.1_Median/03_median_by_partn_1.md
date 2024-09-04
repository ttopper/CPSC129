# Median by Partitioning: Version 1

The next step of our median by partition approach is to call median
again on one of the sub partitions. To do this we need to figure out
which list contains the median value. To do this we want to check to see
if the position of the median value would fall in the smaller or larger
list. To do that we need a new variable posn to store the position of
the list. Initially the position of the median will be `len(lst)//2`,
but that will change as we do recursive calls.

```python
    ...
    # < < < < < < P > >
    #         M
    if len(smaller) > posn:
        return median(smaller, posn)
    # < < P > > > > > >
    #         M
    else:
        return median(larger, posn-len(smaller))
    ...
```

Because we don't want to include a position argument in our initial call
to `median`, we are going to create a helper function `_median` with has
two arguments. According to PEP 8 [http://www.python.org/dev/peps/pep-0008/]
we should use one leading underscore in the names of non-public methods,
i.e. ones that are for internal use only. Also notice that `posn` needs
to be adjusted when `larger` is the longer list. This is because we have
have to subtract the list positions that are in the smaller list.

```python
    def median(lst):
    return _median(lst, len(lst)//2)

def _median(lst, posn):
    print(lst, posn) # Debugging
    pivot = lst[0]
    smaller = []
    larger = []
    for value in lst:
        if value < pivot:
            smaller.append(value)
        else:
            larger.append(value)

    # If we are hunting for the value that will end up in posn 3
    # and there are 5 elements in smaller, then we better look in smaller.
    if len(smaller) > posn:
        return _median(smaller, posn)

    # But if we are looking for position 8 and there are only 5
    # elements in smaller, we better look in larger.
    # But we are no longer looking for position 8 in larger.
    # Since there are 5 elements in smaller we are now looking for
    # posn = 8 - 5 = 3 in larger.
    else:
        return _median(larger, posn-len(smaller))

if __name__ == '__main__':
    lst = [37, 61, 42, 21, 19, 86, 95, 78, 54]
    print(lst)
    print(median(lst))
```

If you run the above code you'll find that it gives an infinite loop.
Looking at the print statement that we included for debugging we see 
that it gets stuck after the first partition. The problem seems to be
that it is trying to partition with the same value it used in the first
call (`[37, 61, 42, 86, 95, 78, 54] 2') This tells me that we should
have removed our partition value from the list. We will do that in the
next iteration of our solution.


   