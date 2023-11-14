# Pseudocode

Now how do we code this tree exploration process? Let’s focus first on
the process of extending the tree downward from one node or state:

    # Given a state:
    for every pitcher in the state
        take every possible action

or to be more explicit about those possible actions:

    # Given a state:
    for every pitcher in the state
        empty the pitcher --> new state
        Pour from the pitcher into the other pitcher --> new state
        fill the pitcher --> new state

I hear you, you’re already thinking some of those will be pointless,
e.g. emptying an empty pitcher, or filling a full one (and indeed those
pointless actions weren’t included in the tree diagram above). Let’s
add some logic so we avoid them,

    # Given a state:
    for every pitcher in the state
        If the pitcher isn't empty:
            empty the pitcher --> new state
        If the other pitcher isn't full:
            Pour from the pitcher into the other pitcher --> new state
        If the pitcher isn't full:
            fill the pitcher --> new state

The notation `--> new state` indicates that the action produces a new
state of the pitchers. What do we do with that new state? Well we need
to hold on to it until it’s time to grow downward from it, so we’ll
save it in a list.

    # Given a state:
    for every pitcher in the state
        If the pitcher isn't empty:
            empty the pitcher --> add new state to statelist
        If the other pitcher isn't full:
            Pour from the pitcher into the other pitcher 
                --> add new state to statelist
        If the pitcher isn't full:
            fill the pitcher --> add new state to statelist

To manage a breadth-first search we’ll add states to the end of the
list, and remove them from the front. If we added _and_ removed from the
end we’d get a depth-first search instead of breadth-first. In coding
terms the two are very close.

The whole process begins with a starting state 0,0 representing two
empty pitchers. When we consider this state we’ll add more states to
the statelist, and considering them will in turn add more states to the
list, and so on until we find the solution.

    statelist = [(0,0)]
    while len(statelist) > 0:
         state = statelist.pop(0) # remove first state from statelist
      for every pitcher in the state
          If the pitcher isn't empty:
              empty the pitcher --> add new state to statelist
          Pour from the pitcher into the other pitcher --> add new state to statelist
          If the pitcher isn't full:
              fill the pitcher --> add new state to statelist

Wait a second, what about noticing when we’ve got the solution?

    goal = 4
    statelist = [(0,0)]
    while len(statelist) > 0 and 4 not in statelist[0]: # BUG!
          # BUG above: misses multi-pitcher solutions!
          state = statelist.pop(0) # remove first state from statelist
        for every pitcher in state
           If the pitcher isn't empty:
               empty the pitcher --> add new state to statelist
        If the other pitcher isn't full:
            Pour from the pitcher into the other pitcher 
                --> add new state to statelist
           If the pitcher isn't full:
               fill the pitcher --> add new state to statelist
