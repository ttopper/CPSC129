# Median by Bounding: Version 1

The previous version failed because the median won't always have exactly
the same number of values smaller and larger than it. What is sufficient
to be the median is for the values smaller and the values larger to each
be less than or equal to half the length of the list.

```python
def median(lst):
    for item in lst:
        count_smaller = 0
        count_larger = 0
        for value in lst:
            if value < item:
                count_smaller = count_smaller + 1
            elif value > item:
                count_larger = count_larger + 1
        # Refined logic to account for duplicates.
        # Test: If it is the median then half or less of the values
        # will be smaller than it, and half or less will be larger than it,
        # i.e. the largest the "halves" could be is:
        # < < < < = > > > >
        # but it could also be
        # < < < = = = = > >
        # in which case the <s and >s each account for less than half
        # the values.
        if count_smaller <= len(lst)//2 and count_larger <= len(lst)//2:
            return item

if __name__ == '__main__':
    print(median([37, 61, 42, 21, 19, 86, 95, 78, 54]))
    print(median([1]))
    print(median([1, 42, 99]))
    print(median([1, 5, 42, 42, 42, 99]))
    print(median([42, 42, 42, 99]))
```

This code looks like it works, but it is not very efficient. The order
of this algorthm is n<sup>2</sup>. You can see that because of the
nested for loop, where we need to consider each element in the list, and
then consider each other element in relationship to it to get our
counts. If we think of the list length as being n, then for each of n
items we do n comparisons giving us nxn or n<sup>2</sup>. We can do
better than n<sup>2</sup> by keeping track of a range that the median
must fall in, so that we don't bother with values outside that range.
Consider the first test case, after we get the smaller and larger counts
for 37 we establish that there are more numbers that are larger than 37,
so the median must be higher than 37. After this we do not need to count
for any values less than 37.