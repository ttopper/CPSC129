# Introduction

One of the most common operations software has to perform is to search
for something in a list. It may be a phone number, a userid, the
definition of a word, an IP address, a credit card number, the amount of
an invoice, a search term (e.g. in Google), or, even more commonly but
less visibly, it may be searching internal data structures within the
software. Because of its ubiquity, and because it is slow when done
poorly, search algorithms have received a lot of attention from computer
scientists, with the result that the best algorithms can, on large data
sets, be thousands to millions of times faster than poor (but still
correct) ones.

There are many kinds of search problems. The one we will deal with in
this unit is that of searching a list of items for one matching a key,
or target, value. We will work with lists of integers because they are
simple and thus won’t distract us from the algorithm itself, but the
techniques generalize trivially to support any object type that supports
the ==, < and > operators [^*].

We will see four search algorithms of increasing efficiency, and
complexity. The increase in efficiency is realized by using more and
more information about the values in the list. While the complexity does
increase even the longest algorithm is only a dozen or so lines of
Python. Although they are not long they have subtle aspects and require
precision in their construction. Think of them as miniature clockworks
in which the gears have to mesh *just so*.

1.  The first method is a linear search of an unordered list. This the
    simplest to write, but also the least efficient.

2.  The second is a linear search of an ordered list[^***]. This is
    faster than the first because it can make use of the fact that
    the list is sorted.

3.  The third is a binary search of an ordered list. This uses the fact
    that list is sorted, and that we can tell if one value is greater
    than another.

4.  The fourth, an interpolative search of an ordered list. This uses
    the relative magnitude of values to interpolate between them to find
    the likely location of the key.

One important lesson to take away is that the more information about
your data you can leverage, the better the algorithm you can develop.

------------------------------------------------------------------------

[^*] What other kinds of search are there? Well one common is searching
for one string within another, e.g. searching for all occurrences of the
word “all” on this web page. In that case we do not begin with a list
of items[^**], but with an extended string of characters. Another type
of search problem arises when we search a problem space for the solution
to a problem. For example we may search for the solution to an equation,
or search a game-space for the next move in tic-tac-toe or chess. In
these cases we are not usually searching for a fixed key, but for
something that evaluates better than the alternatives, and the search
space may be infinite, or, if not infinite, still too large to allow for
an exhaustive search that considers all possibilities. We will look at a
problem of this type near the end of the term.

[^**] Though now that we have mastered `split` we could use it to
divide the page into a list of words and then search that list using the
techniques we are about to see. So many ways to solve any problem!

[^***] Note that ordering a list can lead to such an improvement in
search speed that if a list has to be searched more than a few times it
is often worth taking the time to sort it just to improve the search
speeds. Of course it is only worth doing so if one uses a very fast
sorting algorithms, so search and sorting are often taught hand in hand.
We will do pretty much that in the coming weeks.
