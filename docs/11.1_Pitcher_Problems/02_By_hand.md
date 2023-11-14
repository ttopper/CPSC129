# First: Do it by hand

Thinking back to CPSC 128 the first step in writing a program to solve a
problem is to be sure we know how to solve it ourselves. A good way to
ensure we do is to do the problem by hand first, so let’s try solving
some pitcher problems. (Hopefully the pitcher problems tweaked your
interest and you tried solving one or more of them already.)

The first one is,

> You are at the side of a river. You have a three-litre pitcher and a
> seven-litre pitcher. The pitchers do not have markings to allow
> measuring smaller quantities. You need four liters of water. How can
> you measure four liters?”

The answer to this one pops out to most people because they notice that
the difference between seven and three is four, so:

1.  Fill the seven-litre pitcher from the river.

2.  Fill the three-litre pitcher form the seven-litre pitcher.

This leaves four liters of water in the seven-litre pitcher.

The second problem is,

> You are at the side of a river. You have a two-litre pitcher, a
> five-litre pitcher, and a ten-litre pitcher. The pitchers do not have
> markings to allow measuring smaller quantities. You need one litre of
> water. How can you measure one litre?”

We can use the same strategy as before, i.e. fill a big pitcher and then
pour out known amounts leaving the amount we are after:

1.  Fill the five-litre pitcher from the river.

2.  Fill the two-litre pitcher from the five-litre pitcher.

3.  Empty the two-litre pitcher into the river.

4.  Fill the two-litre pitcher from the five-litre pitcher (again).

Now there is one litre of water left in the five-litre pitcher.

What about the third problem?

> You are at the side of a river. You have a three-litre pitcher and a
> seven-litre pitcher. The pitchers do not have markings to allow
> measuring smaller quantities. You need two liters of water. How can
> you measure two liters?”

The exact same strategy won’t work this time because if we fill the
larger seven-litre pitcher we can only empty by three liters at a time
enabling us to get four liters (after one emptying) or one litre (after
the second emptying). So how do we get two liters? A little trial and
error should lead us to a solution:

1.  Fill the three-litre pitcher from the river.

2.  Pour from the three-litre pitcher into the seven-litre pitcher.

3.  Fill the three-litre pitcher from the river.

4.  Pour from the three-litre pitcher into the seven-litre pitcher.

5.  Fill the three-litre pitcher from the river.

6.  Pour from the three-litre pitcher into the seven-litre pitcher.

Now there are two liters left in the three-litre pitcher.
