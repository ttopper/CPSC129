# What Order is Binary Search?

What about the binary search? It’s harder at first to see what the
relationship is between search time and list size here. Remember from
the screencast that it seemed linear for a bit when our list lengths
were in the low hundreds, but we discovered when we increased the
lengths that the increase in time didn’t remain constant. Instead it
climbed very slowly as _n_ got larger, because each additional guess
doubled the length of the list we could handle.

guesses  | list length
---------|-------------
1        | 2
2        | 4
3        | 8
4        | 16
5        | 32
6        | 64
7        | 128
8        | 256
9        | 512
10       | 1024
11       | 2048


This pattern of values should be familiar to you. The list length is “2
to the power of” the number of guesses, or mathematically
_n_=2<sup>_guesses_</sup>. How do we describe the number of guesses though? If
you think back to Grade 11 math you will recall that the word logarithm
is used to describe exactly that, i.e. the power to which one number
must be raised to equal another number. In this case then _guesses_ =
log<sub>2</sub>_n_. Since the number of guesses is proportional to the time it
takes our code to execute we say in this case that the algorithm is
O(log<sub>2</sub>_n_) or, because computer scientistis almost always work with
logs to the base 2, we will just write O(log n).
