# pitcher_v0.py

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

a = Pitcher(7,5)
b = Pitcher(3,3)
print a
print b
pour(a,b)
print a
print b
pour(b,a)
print a
print b

'''
Get pitchers and goal
statelist = []
while not done: # quit when all dead ends
    for every pitcher:
        try every action
            if goal amount is in a pitcher
                stop
            else:
                add state to statelist if it's not already there
'''
        
