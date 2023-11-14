# Further towards Python: Pseudocode translation

Now let’s try expressing our pseudocode using the objects and methods
we’ve defined. Differences of this code from our pseudocode, and coding
decisions, are numbered in the code and explained in the notes below it.

``` python
def solve_it(pitchers, goal):
    '''Solve the problem of measuring goal litres of water
       using the pitchers in the list pitchers.
    '''
    state_list = [pitchers] # Initialize the state list
    tried_states = [] # Initialize tried_states
    
    while True: # See note 1 #
        # Is it time to give up?
        # It is if there are no more states to try.
        if len(state_list) == 0:
            break

        # If not, get the next state to try.
        # Take it from the front of the list to do breadth-first traversal.
        state = state_list.pop(0)

        # Have we figured it out?
        # We have if this state is a solution.
        if is_goal(state, goal): # See note 2 #
            break
        
        # If we haven't, record that we are trying this state.
        tried_states.append(state) # See note 3 #
        #
        # Grow tree downward from this state by
        # trying every action for every pitcher in it.
        #
        # Emptying:
        for i in range(len(state)): # See note 4 # For every pitcher (by index).
            new_state = copy.deepcopy(state) # See note 4 #
            # Give new_state[i] a more meaningful name
            pitcher = new_state[i]
            if not pitcher.is_empty():
                pitcher.empty()
                # If this isn't a state we've tried and it isn't already in
                # state_list:
                if new_state not in tried_states \
                   and new_state not in state_list: # See notes 5 and 6 #
                    state_list.append(new_state)

        # Filling:
        for i in range(len(state)):
            new_state = copy.deepcopy(state)
            pitcher = new_state[i]
            if not pitcher.is_full():
                pitcher.fill()
                if new_state not in tried_states \
                   and new_state not in state_list:
                    state_list.append(new_state)

        # Pouring:
        # Try pouring from every pitcher into every other pitcher
        # (so nested loops to try all combinations).
        for src in range(len(state)): # index of source pitcher
            for dest in range(len(state)): # index of destination pitcher
                if src == dest: # Don't try to pour into ourself!
                    next        # See note 6 #
                new_state = copy.deepcopy(state)
                # Assign more meaningful names:
                (source, destination) = (new_state[src], new_state[dest])
                if not source.is_empty() and not destination.is_full():
                    pour(source, destination)
                    if new_state not in tried_states \
                       and new_state not in state_list:
                        state_list.append(new_state)

    # We end up here if it is solved, but also if it is unsolvable
    if is_goal(state, goal):
        print 'Figured it out!'
    else:
        print 'That’s an impossible problem!'
```

Notes:

0.  **`state_list = [pitchers]`** States aren’t just lists of numbers
    now, they are lists of `Pitchers`.

1.  **`while True:`** I don’t often use this construction (as you have
    probably noticed). I prefer to be explicit about the reasons a loop
    may end, or to at least use `while not done` and then assign to
    `done` inside the loop. In this case I opted for `while True` so
    you’d have see it at least once, and because it let me reduce the
    number of indentation levels in the body of the loop substantially.
    The thing to remember when you see a `while True` is that it is
    telling you to look for the `break` statements in the loop body
    because that is how the loop will be exited.

2.  **`if is_goal(state, goal):`** In the pseudocode this test was just
    `4 not in statelist[0]`, but `state_list` is no longer a list of
    integer values (see note 0) so we’ll have to look inside `Pitcher`
    objects to perform the test, plus we know we’re going to have to
    consider combinations of `Pitchers` down the road. That’s too much
    to fit in a test condition, so I created a function `is_goal`. The
    details will be hidden in there. At the moment it looks like this,

    ``` python
    def is_goal(state, goal):
        ''' Determines whether state meets goal.
            BUG: Misses multi-pitcher solutions!
        '''
        # Check each pitcher to see if it contains goal litres of water.
        for pitcher in state:
            if pitcher.contents == goal:
                return True
        return False
    ```

3.  **`tried_states.append(state)`** This comes earlier than it did in
    the pseudocode, but we need to put the state into `tried_states`
    ASAP so that we won’t add it more than once to `state_list`.

4.  **`for i in range(len(state)):`** This is the subtle one. Why not
    just say `for pitcher in state`? It would be certainly be easier to
    read. The problem is that the `empty`, `fill` and `pour` operations
    are going to change (mutate) the `Pitchers` in `state` so they
    won’t be the same for later operations as they are for earlier
    ones. Instead we have to make a copy of `state` for each operation
    and let that be changed into a modified state, which we may add to
    `state_list` for further investigation. And that means we have to
    loop through `state` by index rather than by direct object
    reference. Note that we use `copy.deepcopy` to make sure we get new
    member objects to mutate. Without `deepcopy` we would still mutate
    the states of the `Pitchers` in the original list.

5.  **`new_state not in tried_states`** This is the other subtle one!
    The `in` operator will loop through `tried_states` trying to see if
    `new_state` is in it or not. How will it tell? By comparing
    `new_state` to each item in `tried_states`. Now those items are
    lists, and Python knows how to compare two lists, it compares them
    itemwise, i.e. one pair of items at a time. But those items are
    `Pitchers`, and Python doesn’t know how to compare `Pitchers`
    because they are one of _our_ types not a built-in type so we have
    to help it out by providing an `__eq__` method in `class Pitcher`:

    ``` python
    def __eq__(self, other):
        if type(self) == type(other):
            return self.capacity == other.capacity \
                   and self.contents == other.contents
        else:
            return False
    ```

6.  **`and new_state not in state_list`** A subtle bug I missed first
    time through (good thing I had tests!). It’s not enough just to
    make sure `new_state` isn’t in `tried_states`, we also have to
    check that it hasn’t already been created and added to `state_list`
    by an earlier operation this time through the `while` loop so we add
    the test `and new_state not in state_list`.

Here are two versions of a program incorporating `solve_it`. They differ
only in the verbosity of the code and output.
[`pitcher_new_1_verbose.py`](pitcher_new_1_verbose.py) has more comments
and prints out a play-by-play record of what operations are being
performed. I think it will be _very_ helpful to run it on the tests one
at a time to see how the program operates.

**Stop here and run
[`pitcher_new_1_verbose.py`](pitcher_new_1_verbose.py) a few times. Make
sure you can follow how it is finding the solution.**

On the other hand, it _is_ verbose and once you understand it, you
won’t need all those comments, and the extra `print` statements obscure
the logic of the code a bit, so there is also
[`pitcher_new_1_succint.py`](pitcher_new_1_succint.py) (I know, the
name’s not succint, but the function is) which may make a better
jumping off point for further development.
