# Introduction: median()

The focus this week is on a single function: `median()`. `median`’s job
is to find the median value in a list of numbers. The median is defined
to be the number in a set of numbers that separates the larger “half”
of the values from the lower “half” of the values, i.e. if you take
the set of numbers and sort them, the median will be the number in the
middle position. For example if your set of numbers is [37, 61, 42, 21,
19, 86, 95, 78, 54] then the median is 54 because when you sort the
list you get [19, 21, 37, 42, 54, 61, 78, 86, 95] and 54 is the middle
entry in that list[^*].

This suggests one straightforward way of finding the median value: sort
the list and extract the item at the middle index,

     
    def median(l):
        l.sort()
        return l[len(l)//2]

This code is blessedly short, and since the good sorts, e.g. quicksort,
Shellsort and heapsort, are O(_n_ log _n_) so is this algorithm. But can
we do better? Can we find the median without sorting the entire list?

## Median by partition

One possibility is to do just enough sorting to identify the median. The
idea would be not to sort the whole list, but just to sort the area in
the middle. But how can we identify that area before beginning? The
quicksort provides one approach if we successively partition just the
partitions that contain the median. For example, if our first
partitioning of the list produces two ranges one with 60% of the list
and other with the remaining 40% we know the median must be in 60%
portion, so we then repartition just that “half” and ignore the 40%
portion. We continue in this way until we have worked our way down to a
single element partition containing the median. Thus we very partially
sort the entire list as we partition and only ever completely sort the
tiny sublist that contains the median itself.

## Median by bounding

Of course all that partitioning will involve a lot of element swapping
which could take time, and it will scramble the list which might not be
allowable in some applications. Perhaps the whole sorting approach was a
wrong turn. Looking back to the original definition The median is
defined to be the number in a set of numbers that separates the larger
“half” of the values from the lower “half” of the values, so another
possibility suggests itself. The median will be the value in the list
that has the same number of values larger than it as smaller than it. So
we could find the median by considering each value in the list and
counting the number of values smaller than it and the number of values
larger that it. If they are equal, then this value is the median.
(Excluding **temporarily** the possibilities that there are an even
number of items in the list, or that the median value may occur more
than once in the list).

If it is done just as described in the previous paragraph this approach
is **O(_n_<sup>2</sup>/2)**. **_n_<sup>2</sup>** because we must scan the list of _n_
values for each of the _n_ values in it, thus making _n_ &times; _n_ or _n_<sup>2</sup>
operations. **/2** because we will on average find the median halfway
through the list.

We can do better than _n_<sup>2</sup>/2 if we realize that each value we examine
that fails to be the median provides some information about the actual
median value. For example, if we check the value 72 and discover that
there are 11 values smaller than it in the list and 18 values larger
than it in the list, we know the median must be larger than 72. This
means that if we later get to the value 58 we will not count smaller and
larger values for it because we already know it cannot be the median
because it is not larger than 72. This suggests that we maintain a pair
of values (I will use `lo` and `hi`) denoting the current range within
which we know the median must lie. If a value is outside this range we
will not consider it. If a value is inside this range, we will test it,
but if it proves not to be the median, we will use it to refine the
range, thus narrowing the range each time we count, and allowing us to
consider even fewer values in the future.

## Next

The remaining video resources will step you through the development of
two modules `median_by_partn.py` and `median_by_bounding.py` that
implement each of these approaches.

On the assignment you will measure their performance and extend them to
handle all possible lists.

------------------------------------------------------------------------

[^*] You may be wondering what happens if there an even number of values
in the set, since then there may not be a middle value, e.g. [32, 19,
84, 56] sorted is [19, 32, 56, 84] and there is no middle value.
Conventional practice is to take the mean (average) of the two values on
either side of the “middle”, i.e. in this case we say the median is
(32 + 56)/2 = 44, even though 44 isn’t even a value in the set. Note
that sets with an even number of values may have a median value that
does occur in the set when it contains duplicate values, e.g. [42, 19,
84, 42] sorted is [19, 42, 42, 84] and we get a median of 42. For our
development of `median()` we will begin by working with lists with odd
numbers of values, and you will extend this to lists with even numbers
of values on the assignment.
