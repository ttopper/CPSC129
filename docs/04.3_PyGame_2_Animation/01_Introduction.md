# Introduction

Last time around we saw how to use PyGame to draw static shapes into a
window. This time we’ll see how to make those shapes move, or at least
at how to produce the illusion of movement!

This unit is aimed at showing you _how_ animation can be done from
scratch. It’s a fundamental technique that every programmer should
understand. Of course since it is fundamental most of it has been
encapsulated into libraries that are available. The moving objects
we’ll be creating in this unit are usually referred to as _sprites_.
PyGame does provide libary routines to manage sprites and those are what
you would use were you creating a an actual arcade game. On the other
hand sprites can be used badly[^*] if you are unaware of what is behind
them so to become aware of what is behind them we’ll be implementing
ours from scratch.

With great power comes great responsibility :-) The goal of this unit is
to give you the awareness to use your power well.

------------------------------------------------------------------------

[^*] in the same way that if we want to find the first 5 that occurs in a list after the first 3 we might write the compact expression `lst[lst.index(3):].index(5)` without realizing that that is an O(_n_<sup>2</sup>) operation!
