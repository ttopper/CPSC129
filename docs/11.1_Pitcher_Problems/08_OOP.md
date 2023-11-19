# Towards Python: A little OOP

Well that pseudocode expresses our algorithm, but it is one vague, buggy
mess at the moment. How to move from there to a clear, correct Python
program? Let’s start with a bit of OOP, and look for the _nouns_ and
_verbs_ we’ve used in our pseudocode to identify the _objects_ and
_methods_ we need to implement to let us express the algorithm.

The only objects in sight are `Pitcher`s.

What attributes do they have? A `capacity` and some `contents`.

What methods do they have? `fill` and `empty`.

Any other verbs we’ve used? `pour`.

That leads directly to this code:

``` python
class Pitcher:
    def __init__(self, capacity, contents=0):
        self.capacity = capacity
        self.contents = contents

    def empty(self):
        self.contents = 0

    def fill(self):
        self.contents = self.capacity

    def __str__(self): # debugging aid
        return '%d of %d' % (self.contents, self.capacity)

def pour(src, destn):
    # How much can we pour into the destination pitcher?
    destn_space = destn.capacity - destn.contents
    # How much can we pour from the source pitcher?
    src_avail = src.contents
    # The amount we transfer is the least of those two amounts.
    transfer = min(destn_space, src_avail)
    #print 'Transferring', transfer, 'liters.'
    # Now we simulate pouring by adjusting the amounts in each pitcher.
    destn.contents += transfer
    src.contents -= transfer
    
if __name__ == '__main__':
    print 'Create pitchers 7:5 and 3:3'
    a = Pitcher(7,5)
    b = Pitcher(3,3)
    print a
    print b
    print 'Try pouring into a full pitcher:'
    pour(a,b)
    print a
    print b
    print 'Try pouring from 3:3 into 7:5, should pour 2 litres:'
    pour(b,a)
    print a
    print b
    print 'Empty both pitchers:'
    a.empty()
    b.empty()
    print a
    print b
```

Running it produces some encouraging output:

    >>> 
    Create pitchers 7:5 and 3:3
    5 of 7
    3 of 3
    Try pouring into a full pitcher:
    Transferring 0 litres.
    5 of 7
    3 of 3
    Try pouring from 3:3 into 7:5, should pour 2 litres:
    Transferring 2 litres.
    7 of 7
    1 of 3
    Empty both pitchers:
    0 of 7
    0 of 3
    >>>
