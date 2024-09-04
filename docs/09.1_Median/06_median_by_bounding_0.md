# Median by Bounding: Version 0

Median by bounding is based on the insight that the median is the value
that has the same number of values larger than it and smaller than it.
We will assume for the moment that we don't need a wrapper/helper
function for median. We don't know what the median value is, so we will
need to check each element in the list. Then for each element we will
count how many items are smaller and how many are larger. If the number
of items that are smaller and larger are equal, then we have found the
median.

```python
def median(lst):
    # It could be any item in the list, so we check each one.
    for item in lst:
        # Check if this item is the median.
        # Count smaller and larger values.
        count_smaller = 0
        count_larger = 0
        for value in lst:
            if value < item:
                count_smaller += 1
            elif value > item:
                count_larger += 1
        # Test: If it is the median then the same number of values
        # will be smaller than it as will be larger than it.
        if count_smaller == count_larger:
            return item

if __name__ == '__main__':
    print(median([37, 61, 42, 21, 19, 86, 95, 78, 54]))
    print(median([1]))
    print(median([1, 42, 99]))
    print(median([1, 42, 42, 42, 99]))
    print(median([1, 5, 42, 42, 99]))
    print(median([42, 42, 42, 42, 99]))
```

This algorithm seems to work well on some of our test cases, but it
fails on the last two tests. If you look closely at those two tests you
can see that the smaller count and the larger count can't be equal
because of the duplicate values.
