# pitcher_new_1_verbose.py
import copy

class Pitcher:
    def __init__(self, capacity, contents=0):
        self.capacity = capacity
        self.contents = contents

    def empty(self):
        self.contents = 0

    def fill(self):
        self.contents = self.capacity

    def __str__(self): # debugging aid
        return '%d/%d' % (self.contents, self.capacity)

    def __eq__(self, other):
        if type(self) == type(other):
            return self.capacity == other.capacity \
                   and self.contents == other.contents
        else:
            return False
        
    def is_full(self): # Convenience function to make code more readable.
        return self.capacity == self.contents
    
    def is_empty(self): # Convenience function to make code more readable.
        return self.contents == 0

def pour(src, destn):
    destn_space = destn.capacity - destn.contents
    src_avail = src.contents
    transfer = min(destn_space, src_avail)
    # print 'Transferring', transfer, 'liters.'
    destn.contents += transfer
    src.contents -= transfer

def is_goal(state, goal):
    ''' Determines whether state meets goal.
        BUG: Misses multi-pitcher solutions!
    '''
    # Check each pitcher to see if it contains goal litres of water.
    for pitcher in state:
        if pitcher.contents == goal:
            return True
    return False

# A little debugging help:
def show_state_list(sl):
    print '\nstate_list:'
    for i in range(len(sl)):
        print i, ':', 
        show_state(sl[i])
        print
    print
def show_state(s):
    for p in s:
        print p,

def solve_it(pitchers, goal):
    '''Solve the problem of measuring goal litres of water
       using the pitchers in the list pitchers.
    '''
    state_list = [pitchers] # Initialize the state list
    tried_states = [] # Initialize tried_states
    
    while True: # See note 1 #
        show_state_list(state_list)                                     # DEBUG

        # Is it time to give up?
        # It is if there are no more states to try.
        if len(state_list) == 0:
            break

        # If not, get the next state to try.
        # Take it from the front of the list to do breadth-first traversal.
        state = state_list.pop(0)

        # DEBUG                                                         # DEBUG
        print 'Working with state:',                                    # DEBUG
        show_state(state)                                               # DEBUG
        print                                                           # DEBUG

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
                print 'Emptying', pitcher,                              # DEBUG
                pitcher.empty()
                print '-->',                                            # DEBUG
                show_state(new_state)                                   # DEBUG
                # If this isn't a state we've tried and it isn't already in
                # state_list:
                if new_state not in tried_states \
                   and new_state not in state_list: # See note 5 #
                    state_list.append(new_state)
                    print ', added to state_list.'                      # DEBUG
                else:                                                   # DEBUG
                    print ', not unique.'                               # DEBUG

        # Filling:
        for i in range(len(state)):
            new_state = copy.deepcopy(state)
            pitcher = new_state[i]
            if not pitcher.is_full():
                print 'Filling', pitcher,                               # DEBUG
                pitcher.fill()
                print '-->',                                            # DEBUG
                show_state(new_state)                                   # DEBUG
                if new_state not in tried_states \
                   and new_state not in state_list:
                    state_list.append(new_state)
                    print ', added to state_list.'                      # DEBUG
                else:                                                   # DEBUG
                    print ', not unique.'                               # DEBUG

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
                    print 'Pouring from', source, 'into', destination,  # DEBUG
                    pour(source, destination)
                    print '-->',                                        # DEBUG
                    show_state(new_state)                               # DEBUG
                    if new_state not in tried_states \
                       and new_state not in state_list:
                        state_list.append(new_state)
                        print ', added to state_list.'                  # DEBUG
                    else:                                               # DEBUG
                        print ', not unique.'                           # DEBUG

    # We end up here if it is solved, but also if it is unsolvable
    if is_goal(state, goal):
        print 'Figured it out!'
    else:
        print 'That’s an impossible problem!'
    
if __name__ == '__main__':
##    # Test Pitcher class:
##    print 'Create pitchers 7:5 and 3:3'
##    a = Pitcher(7,5)
##    b = Pitcher(3,3)
##    print a
##    print b
##    print 'Try pouring into a full pitcher:'
##    pour(a,b)
##    print a
##    print b
##    print 'Try pouring from 3:3 into 7:5, should pour 2 litres:'
##    pour(b,a)
##    print a
##    print b
##    print 'Empty both pitchers:'
##    a.empty()
##    b.empty()
##    print a
##    print b
##    print

    # Test Pitcher Problem solving function solve_it:
    print 'Starting problems...'

    # Test Problem 1: Measure 4 litres using 3 and 7 litre pitchers
    goal = 4 # Set the goal
    start = [Pitcher(3,0), Pitcher(7,0)] # Start with two empty pitchers
    solve_it(start, goal)
    
##    # Test Problem 2: Measure 1 litre using 2, 5 and 10 litre pitchers
##    goal = 1 # Set the goal
##    start = [Pitcher(2,0), Pitcher(5,0), Pitcher(10,0)] # Start with two empty pitchers
##    solve_it(start, goal)
##
##    # Test Problem 3: Measure 2 litres using 3 and 7 litre pitchers
##    goal = 2 # Set the goal
##    start = [Pitcher(3,0), Pitcher(7,0)] # Start with two empty pitchers
##    solve_it(start, goal)
##
##    # Test Problem 4: Measure 1 litres using 5 and 10 litre pitchers
##    goal = 1 # Set the goal
##    start = [Pitcher(5,0), Pitcher(10,0)] # Start with two empty pitchers
##    solve_it(start, goal)
                
    print '...done.'
