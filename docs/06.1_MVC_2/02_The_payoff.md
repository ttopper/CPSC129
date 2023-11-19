# The Payoff: An ObjectServer

Solving the issue (remember:_ How can we free our controller from having
to know about the innards of the objects it processes?_) by separating
our controller code from our Quote class will make it easier to work on
our code by letting us work on each piece independently, but there is
also a much bigger payoff.

If we are able to completely separate the controller from the quote
class (as we did the model last time around) then it should be easy to
add new object types to the system, and instead of having a single
purpose QuoteServer we should get, for free as it were, an ObjectServer
that can store and retrieve any and all types of Python objects we might
create. So as we disentangle the controller from the Quote class, let’s
keep the goal of being able to generalize to any type of object at all
in mind.
