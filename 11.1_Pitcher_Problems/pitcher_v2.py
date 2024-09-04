# pitcher_v2.py
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

##a = Pitcher(7,5)
##b = Pitcher(3,3)
##print a
##print b
##pour(a,b)
##print a
##print b
##pour(b,a)
##print a
##print b

def showstatelist(sl):
    for s in sl:
        showstate(s)
        
def showstate(s):
    for p in s:
        print p,
    print

#Get pitchers and goal
pitchers = [Pitcher(7,0),Pitcher(3,0)]
goal = 2
statelist = [pitchers]

for s in statelist:
    print 'Statelist ='
    showstatelist(statelist)
    print 'Working with:',
    showstate(s)
    
    state = copy.deepcopy(s)
    pourcopy = copy.deepcopy(s)
    for pitcher in state:
        # Try every action.
        # Filling:
        pitcher.fill()
        if pitcher.contents == goal:
            print 'Done it!'
            break
        newstate = copy.deepcopy(state)
        if newstate not in statelist:
            statelist.append(newstate)
        # Emptying:
        pitcher.empty()
        newstate = copy.deepcopy(state)
        if newstate not in statelist:
            statelist.append(newstate)
            
    state = pourcopy
    pour(state[0], state[1])
    for p in state:
        if p.contents == goal:
            print 'Done it!'
            break
    newstate = copy.deepcopy(state)
    if newstate not in statelist:
        statelist.append(newstate)

    pour(state[1], state[0])
    for p in state:
        if p.contents == goal:
            print 'Done it!'
            break
    newstate = copy.deepcopy(state)
    if newstate not in statelist:
        statelist.append(newstate)

      
