# What Order is Linear Search?

Let’s try assessing the order or growth rate of our search algorithms.

First consider our algorithm for the linear search of an unordered list,

``` python
def lu_search(lst, target):
    for entry in lst:
        if entry == target:
            return True
    return False
```

When the target _isn’t_ in the list it has to search the whole list
before it finds out. If we double the length of the list, we double the
number of entries it has to check, and therefore we double the time it
will take. Similarly if we triple or quadruple the length of the list,
we triple or quadruple the time it will take to discover that an item is
not in the list. Because the time it takes is directly proportional to
the length of the list (_n_) we say that this algorithm is “_order
n_”, for which we write **O(_n_)**. (There’s the Big O.)

What about an item that _is_ in the list? Assuming the items we look for
are randomly distributed in the list then we will find some near the
beginning of the list, others in the middle section, and still others
toward the end. The early matches and late matches should balance out
though so that across a group of searches we will ***on average*** have
to check half the list. This means that on average we find out if an
item is in the list in around half the time it takes to find out that
one isn’t in the list, so hits are twice as fast as misses. When it
comes to characterizing our algorithm’s performance on hits it is
O(_n_/2). Notice that even though it is twice as fast as for misses, it
is still directly proportional to the length of the list, double the
list and we will have to check twice as many entries (on average).

Without knowing the relative frequency of hits and misses likely to
occur we would probably say that overall this algorithm is O(n).

One of the beauties of big O notation is that it allows for quick mental
estimates. For example if linear searches of a 20,000 item dataset takes
3.6 seconds on average, you would estimate that searches of a 100,000
item database would average 5 x 3.6 = 18 seconds. Nifty eh?

What about our algorithm for searching ordered lists? It takes the same
time searching for targets that are present since on average it will
find it after scanning half the list. But because the list is sorted it
also detects absences, on average, after checking half the list. In
absolute terms then it takes the same time to find things, but detects
absences twice as fast.

What about the order of this algorithm? Since it scans half the list (on
average) for both hits and misses, the time it will take depends on the
length of the list, and in fact varies directly as the length of the
list. Thus this algorithm is also O(_n_). To show its improved absolute
performance we will write this as O(_n_/2) that way we are reminded that
it is roughly twice as fast.
