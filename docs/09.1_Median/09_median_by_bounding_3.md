# Median by Bounding: Version 3

To find out if it is saving us time let's instrument our code, or count
the number of values we consider and the number of values we skip. We'll
start by adding new variables to track the number `considered` and the
number `skipped`. The value of `considered` should be incremented each
time the item is within the bound. To track the number of `skipped`
values we need to add an else block where `skipped` is incremented. A
print statement before the the return statement tells us what we saved.

```python
def median(lst):
    lo = min(lst)
    hi = max(lst)
    considered = 0
    skipped = 0
    for item in lst:
        if item >= lo and item <= hi:
            considered += 1
            count_smaller = 0
            count_larger = 0
            for value in lst:
                if value < item:
                    count_smaller += 1
                elif value > item:
                    count_larger += 1
            if count_smaller <= len(lst)//2 and count_larger <= len(lst)//2:
                print('Considered =', considered, 'Skipped =', skipped)
                return item
            elif count_smaller > count_larger:
                hi = item
            else:
                lo = item
        else:
            skipped += 1

if __name__ == '__main__':
    print(median([37, 61, 42, 21, 19, 86, 95, 78, 54]))
    print(median([1]))
    print(median([1, 42, 99]))
    print(median([1, 42, 42, 42, 99]))
    print(median([1, 5, 42, 42, 99]))
    print(median([42, 42, 42, 42, 99]))

```

What we see when we run it is the following...

    Considered = 4 Skipped = 5
    54
    Considered = 1 Skipped = 0
    1
    Considered = 2 Skipped = 0
    42
    Considered = 2 Skipped = 0
    42
    Considered = 3 Skipped = 0
    42
    Considered = 1 Skipped = 0
    42

We seem to save a lot of time on our longer list, but less time on our
shorter ordered lists. Let's build a longer list of values to try in on.
We'll import random, and append values from a larger range to our list.


```python
def median(lst):
    lo = min(lst)
    hi = max(lst)
    considered = 0
    skipped = 0
    for item in lst:
        if item >= lo and item <= hi:
            considered += 1
            count_smaller = 0
            count_larger = 0
            for value in lst:
                if value < item:
                    count_smaller += 1
                elif value > item:
                    count_larger += 1
            if count_smaller <= len(lst)//2 and count_larger <= len(lst)//2:
                print('Considered =', considered, 'Skipped =', skipped)
                return item
            elif count_smaller > count_larger:
                hi = item
            else:
                lo = item
        else:
            skipped += 1

if __name__ == '__main__':
    # Build a big random list to get sense of how many computations
    # our bounding trick is saving us.
    import random
    lst = []
    for i in range(1000):
        lst.append(random.randint(1,100000))
    print(median(lst))

```

When I ran this I got the following result...

    Considered = 15 Skipped = 104
    52562

So in a list with 1000 items, we only needed to consider 15 values, plus
the overhead of finding the min and max (2 more times). This might be a
bit lucky, because it found the median at position 119 of our list
(15 + 104). Let's create a loop and test this more thoroughly.

```python
def median(lst):
    lo = min(lst)
    hi = max(lst)
    considered = 0
    skipped = 0
    for item in lst:
        if item >= lo and item <= hi:
            considered += 1
            count_smaller = 0
            count_larger = 0
            for value in lst:
                if value < item:
                    count_smaller += 1
                elif value > item:
                    count_larger += 1
            if count_smaller <= len(lst)//2 and count_larger <= len(lst)//2:
                print('Considered =', considered, 'Skipped =', skipped)
                return item
            elif count_smaller > count_larger:
                hi = item
            else:
                lo = item
        else:
            skipped += 1

if __name__ == '__main__':
    # Build a big random list to get sense of how many computations
    # our bounding trick is saving us.
    import random
    for _ in range(10):
        lst = []
        for i in range(1000):
            lst.append(random.randint(1,100000))
        print(median(lst))

```

That gives the following output...

    Considered = 13 Skipped = 563
    48329
    Considered = 11 Skipped = 590
    49325
    Considered = 8 Skipped = 52
    46175
    Considered = 13 Skipped = 261
    48863
    Considered = 12 Skipped = 490
    49424
    Considered = 9 Skipped = 385
    48842
    Considered = 12 Skipped = 602
    48113
    Considered = 4 Skipped = 0
    45933
    Considered = 10 Skipped = 12
    50159
    Considered = 14 Skipped = 770
    49216

The number of values we consider in the list is never very large, even
when the median is found later in the list and the number of skipped
values is very large. It would be interesting to graph the number of
items considered relative to the length of the list. If we did that we
would see that this would look like a log(n) relationship. In the
assignment you will have the opportunity to compare the partition
approach to the bounding approach to see which one is faster.