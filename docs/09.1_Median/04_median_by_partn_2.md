# Median by Partitioning: Version 2

Let's tackle the infinite loop in the previous version of our code.
Because of our if-else structure the pivot is added to the larger list.
One way to fix this would be to add an `elif` to collect the values that
are equal to the pivot, this will of course include the pivot, but may
also include duplicate values from elsewhere in the partition.

```python
def median(lst):
    return _median(lst, len(lst)//2)

def _median(lst, posn):
    print(lst, posn) # Debugging
    pivot = lst[0]
    smaller = []
    larger = []
    equal = []
    for value in lst:
        if value < pivot:
            smaller.append(value)
        elif value == pivot:
            equal.append(value)
        else:
            larger.append(value)

    # If we are hunting for the value that will end up in posn 3
    # and there are 5 elements in smaller, then we better look in smaller.
    if len(smaller) > posn:
        return _median(smaller, posn)

    # On the other hand if we are looking for position 8 and there are
    # 5 in smaller and less than 9 values in smaller and equal together
    # then our value lies in equal and since all the values in equal are
    # the same we can return any of them, like equal[[0], and be done.
    # (N.B. this test assumes that we've already eliminated smaller above.)
    elif len(smaller) + len(equal) > posn:
        return equal[0]

    # But if we are looking for position 11 and there are only 9
    # elements in smaller and equal together, we better look in larger.
    # But we are no longer looking for position 8 in larger.
    # Since there are 9 elements accounted for in smaller and equal
    # we are now looking for posn = 11 - 9 = 2 in larger.
    # (I had to draw a picture to sort that out -- you might need to too
    # to understand it).
    else:
        return _median(larger, posn-(len(smaller)+len(equal)))

if __name__ == '__main__':
    lst = [37, 61, 42, 21, 19, 86, 95, 78, 54]
    print(lst)
    print(median(lst))
```

The new recursive call, that now takes the equal list into account, also
gives us our stop condition for our recursion.