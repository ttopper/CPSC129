# Median by Partitioning: Version 0

Based on the insight that the median value will be in the middle of a
list of sorted values, plus the hint that we may be able to find it
without completely sorting the list, we find the median by successive
partitions of the list.

Our strategy will be to partition as in quicksort initially, but then to
further partition only the portion that will contain the median.

We could do this with indices or by building new lists. Let's start by
building new lists, because it is much easier to write. Let's set our
initial pivot value to index 0 and build the first two sublists: one
with values smaller than the pivot and one with values larger than the
pivot.

``` python
# median_by_partn.py

def median(lst):
    # Start by partitioning the list into a list of values smaller than
    # the pivot and a list of values larger than the pivot.
    pivot = lst[0]
    smaller = []
    larger = []
    for value in lst:
        if value < pivot:
            smaller.append(value)
        else:
            larger.append(value)
    return str(smaller) + ' + ' + str(larger)

if __name__ == '__main__':
    lst = [37, 61, 42, 21, 19, 86, 95, 78, 54]
    print(lst)
    print(median(lst))
```

After implementing this algorithm we get a smaller list `[19, 21]` and
the larger list `[37, 61, 42, 86, 95, 78, 54]`. The list larger list has
more elements, so on the next iteration of our partitioning we will
focus on that larger list.