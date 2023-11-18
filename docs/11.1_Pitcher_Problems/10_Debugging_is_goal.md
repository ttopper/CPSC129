# Debugging `is_goal()`

Now there’s one bug we’re aware of in `is_goal`: it doesn’t consider
solutions involving more than one pitcher (there may also be other bugs
of course!). For example given 3 and 7 litre pitchers and the goal of
measuring 10 litres it won’t notice that filling both pitchers meets
this goal. It is easy to extend `is_goal` to handle exactly two
pitchers, we just add another `if`:

``` python
    if len(state) == 2:
        # Check total contents of both pitchers against goal
        if state[0].contents + state[1].contents == goal:
            return True
```

We could extend to include three pitchers by adding tests for each pair
of pitchers and for all three pitchers:

``` python
    if len(state) == 3:
        # Check total contents of all pairs of pitchers against goal
        if state[0].contents + state[1].contents == goal or \
           state[0].contents + state[2].contents == goal or \
           state[1].contents + state[2].contents == goal:
            return True
        # Check total contents of all three pitchers against goal
        if state[0].contents + state[1].contents + state[2].contents = goal:
            return True
```

But you should have good enough programming instincts by now that you
have a sinking feeling that this is not a general approach and that
things will get very unwieldy with more pitchers.

What might a general approach be? Well we need some way of generating
all possible subsets of the `Pitchers` in `state`. The key to doing that
is to appreciate the 2-ness of the problem. What 2-ness? Well any given
subset either does, or does not, include each `Pitcher` in `state`, i.e.
there are 2 possibilities. Thus for three items there are 2<sup>3</sup>, or 8,
possible subsets. Here are all possible subsets of the items
`[A, B, C] `together with a binary list showing which elements of
`[A, B, C]` are in the subset (using 1 for presence and 0 for absence)
and then a binary number representation of the binary list, and finally
the binary number’s decimal equivalent.

  Subset      Binary List   Binary Number   Decimal Number
  ----------- ------------- --------------- ----------------
  []        0,0,0         000             0
  [C]       0,0,1         001             1
  [B]       0,1,0         010             2
  [B,C]     0,1,1         011             3
  [A]       1,0,0         100             4
  [A,C]     1,0,1         101             5
  [A,B]     1,1,0         110             6
  [A,B,C]   1,1,1         111             7

Now let’s read this from right to left, i.e. starting with the Decimal
Number and working our way across. If you ask me for subset 3, I can
give it to you by looking at the binary representation of 3, which is
011, which tells me that subset 3 should contain the elements B and C
from the full set, because the bits in the B and C positions are 1s, but
the bit for the A position is 0. In other words each of the bits acts as
a switch telling us whether or not to include one specific set member.
So given a subset number we can build the subset by looking at the
binary representation of that number and adding the appropriate set
members to the subset

But how do we look at binary representations in Python? Using its
bitwise operators. Wait, what? Bitwise operators?” Yes indeedy.
Python provides a full set of [bitwise operators and
operations](http://docs.python.org/2/reference/expressions.html#binary-bitwise-operations).
We only need one of them for this problem, bitwise and” implemented
by the operator `&`.
