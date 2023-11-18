# Interlude: Bitwise operations (really just `&`)

Bitwise-and is like doing a logical `and` on two values bit by bit. When
the bits in the two values are both 1 the result will be 1, and when
they are not both 1 (i.e. they are 0,0 or 0,1 or 1,0) it will be 0. It
makes sense if you think of 1 as `True` and 0 as `False` (which Python
does!).

| Decimal       | Binary |
|---------------|--------|
| 6             | 110    |
| 3             | 011    |
| 6 &amp; 3 = 2 | 010    |
We can verify that 6 `&` 3 is 2 using the Python shell:

    >>> 6 & 3
    2
    >>>

So, bitwise-and tells us what bits are 1 in both values.

How can we use this in our problem? Well we want to know which of the
elements in the full set [A, B, C] to include in a subset, and the 1
bits in the binary representation of the subset number tell us which
ones those are, and bitwise-and lets us read those bits. Here’s how,

``` python
fullset = ['A', 'B', 'C']
subset_num = 6 # i.e. 110 or the subset with B and C*
subset = []
for i in range(len(fullset)): # i.e. i in [0, 1, 2]
    if subset_num & (2**i): # i.e. 6 & 2^0=1 then 6 & 2^1=2 and finally 6 & 2^2=4
        subset.append(fullset[i])
print subset
```

Output:

``` python
>>> 
['B', 'C']
>>> 
```

And here’s how that works, showing the values each time through the
loop:

| i | subset_num | 2**i | subset_num &amp; (2**i)            | fullset[i] |
|---|------------|------|------------------------------------|------------|
| 0 | 6          | 1    | 110 &amp; 001 = 000 = 0 i.e. False | -          |
| 1 | 6          | 2    | 110 &amp; 010 = 010 = 2 i.e. True  | B          |
| 2 | 6          | 4    | 110 &amp; 100 = 100 = 4 i.e. True  | C          |

So `&` gives us a way of asking Is the bit corresponding to this
element set (i.e. 1), or not (i.e. 0)?” And then appending the element
when it is set, since 0 is considered False, but all non-zero numbers
are considered True.

------------------------------------------------------------------------

The careful reader will have noticed that I have pulled a fast one here.
According to our original table the code sample above should return A
and B instead of B and C. The reason we get B and C is that lists and
binary numbers are read in opposite directions. Lists are read left to
right, but numebrs are read right to left, that is the first item in a
list is the leftmost one, but the first bit in a binary number is the
rightmost one. This means they map onto each other like this:

        -------------------- 
       |     -------------  |
       |    |     ------  | |
       |    |    |      | | |
    [ 'A', 'B', 'C' ]   1 1 0

And that’s why 110 gives us B and C, not A and B. I didn’t introduce
this final complication earlier because it would have made the mapping
from number to list harder to understand, but since we want to test all
possible subsets this difference doesn’t matter because we will loop
through all of them.
