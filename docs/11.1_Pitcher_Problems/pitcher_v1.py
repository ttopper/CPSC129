# pitcher_v1.py

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

def pour(src, destn):
    destn_cap = destn.capacity - destn.contents
    src_avail = src.contents
    transfer = min(destn_cap, src_avail)
    print 'Transferring', transfer, 'liters.'
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


#Get pitchers and goal
pitchers = [(7,0),(3,0)]
goal = 4
statelist = [pitchers]
done = False
while not done: # quit when all dead ends
    print statelist
    for pitcher in pitchers:
        #try every action
        # Filling:
        pitcher.fill()
        if pitcher.contents == goal:
            print 'Done it!'
            done = True
        if not done:
            if pitchers not in statelist:
                statelist.append(pitchers)
        # Emptying:
        if not done:
            pitcher.empty()
            if not done:
                if pitchers not in statelist:
                    statelist.append(pitchers)
    pour(pitchers[0], pitchers[1])
    for p in pitchers:
        if p.contents == goal:
            print 'Done it!'
            done = True
    pour(pitchers[1], pitchers[0])
    for p in pitchers:
        if p.contents == goal:
            print 'Done it!'
            done = True

print statelist       
