# Median by Bounding: Version 2

Now let's update the code so that it can learn as it makes its way
through the list about the bounds on the possible values of the median.
We need to keep track of two values that act as bounds (boundaries) for
the possible value of the median. For example, once we've made the 
counts for 37 in our first test we can use 37 as the lower bound for our
median value. After that all items that are less than our lower bound
(ie 19 and 21) do not need to be considered. We will want to keep track
of this low value as well as a high value, to represent the upper bound.
The median will always fall between the low and high value. The bounds
will need initial values, we can't choose arbitrary values because we
don't know the range of our list. The solution is computationally
expensive, we are going to set them to the min and max values in the
list. It is computationally expensive because we have to search the
whole list twice to get the min and the max values (n+n). We also need
to add a condition that only considers items inside our range between lo
and hi. The final change we need to make is to update the value of lo
or hi for each item that isn't the medium.


```python
def median(lst):
    lo = min(lst)
    hi = max(lst)
    for item in lst:
        # Check if this item is the median,
        # but don't bother if it is outside the possible range.
        if item >= lo and item <= hi:
            count_smaller = 0
            count_larger = 0
            for value in lst:
                if value < item:
                    count_smaller += 1
                elif value > item:
                    count_larger += 1
            if count_smaller <= len(lst)//2 and count_larger <= len(lst)//2:
                return item
            # update our bounds
            elif count_smaller > count_larger:
                hi = item
            else:
                lo = item

if __name__ == '__main__':
    print(median([37, 61, 42, 21, 19, 86, 95, 78, 54]))
    print(median([1]))
    print(median([1, 42, 99]))
    print(median([1, 42, 42, 42, 99]))
    print(median([1, 5, 42, 42, 99]))
    print(median([42, 42, 42, 42, 99]))
    # < < < = = = >
    #       M
    # < < < = > > >
    # < < < < < > >
```

This looks good and still gives the right answer, but we should check to
see if we are saving time.