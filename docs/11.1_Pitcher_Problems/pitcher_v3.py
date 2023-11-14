# pitcher_v3.py
import copy

class Pitcher:
    def __init__(self, capacity, contents=0):
        self.capacity = capacity
        self.contents = contents
    def empty(self):
        self.contents = 0
    def fill(self):
        self.contents = self.capacity
    def __str__(self):
        return '%d of %d' % (self.contents, self.capacity)
    def __eq__(self,other):
        if type(self) == type(other):
            return self.capacity == other.capacity and self.contents == other.contents
        else:
            return False

def pour(src, destn):
    destn_cap = destn.capacity - destn.contents
    src_avail = src.contents
    transfer = min(destn_cap, src_avail)
    #print 'Transferring', transfer, 'liters.'
    destn.contents += transfer
    src.contents -= transfer

def showstatelist(sl):
    for s in sl:
        showstate(s)
        
def showstate(s):
    for p in s:
        print p,
    print

def subset_x(lst, x):
    ''' return subset number x of the items in lst '''
    subset = []
    for i in range(len(lst)):
        if x & (2**i):
            subset.append(lst[i])
    return subset

def is_goal(state, goal):
    # Does any subset of pitchers in state contain the goal amount?
    for x in range(1, 2**len(state)):
        subset = subset_x(state, x)
        total = 0
        for pitcher in subset:
            total += pitcher.contents
        if total == goal:
            return True
    return False
            
def solve_it(pitchers, goal):
    statelist = [pitchers]

    for state in statelist:
##        print 'Statelist ='
##        showstatelist(statelist)
##        print 'Working with:',
##        showstate(state)
        
        # Try every action.
        # Filling:
        for i in range(len(state)):
            newstate = copy.deepcopy(state)
            newstate[i].fill()
            if is_goal(newstate, goal):
                showstate(newstate)
                return True
            ... += 'Fill from ...'
            elif newstate not in statelist:
                statelist.append(newstate)
                
        # Emptying:
        for i in range(len(state)):
            newstate = copy.deepcopy(state)
            newstate[i].empty()
            if newstate not in statelist:
                statelist.append(newstate)
                
        # Pouring:
        for i in range(len(state)):
            for j in range(len(state)):
                if j!=i:
                    newstate = copy.deepcopy(state)
                    pour(newstate[i], newstate[j])
                    for p in newstate:
                        if  is_goal(newstate, goal):
                            showstate(newstate)
                            return True
                    if newstate not in statelist:
                        statelist.append(newstate)
            
    return False

#Get pitchers and goal
pitchers = [Pitcher(10,0),Pitcher(5,0),Pitcher(2,0)]
goal = 15

#for goal in range(0, pitchers[0].capacity+pitchers[1].capacity+1):
print goal, solve_it(pitchers, goal)          
