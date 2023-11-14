# Back to our program: is_goal()

In case you have forgotten during the interlude: `is_goal()` is supposed
to look at a state and determine if it meets a goal. It could do that by
having the goal amount in one of the pitchers, or by having the contents
of any group of pitchers in `state` add to the goal amount. That means
we can see if the goal is met by looking at the total amount of water in
each subset of the pitchers in `state`. Doing this will include
individual pitcher solutions we were already testing for since single
pitchers are just the subsets with exactly one element (i.e. 100, 010
and 001), but also include all combinations of multiple pitchers.

``` python
def subset_x(lst, x):
    ''' return subset number x of the items in lst
        see the numbering in the earlier table to interpret x
    '''
    subset = []
    for i in range(len(lst)):
        # Check to see if bit corresponding to item i is set in x.
        if x & (2**i):
            subset.append(lst[i])
    return subset

def is_goal(state, goal):
    ''' Does any subset of pitchers in state contain the goal amount? '''
    # Check each subset of state. There are 2**len(state) possible subsets.
    for subset_num in range(1, 2**len(state)): # Q: why start at 1?
        subset = subset_x(state, subset_num)
        total = 0
        for pitcher in subset:
            total += pitcher.contents
        if total == goal:
            return True
    return False
```
