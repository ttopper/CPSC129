# MVC_model.py
#
# Version 1 (archived as MVC_model_1.py)
#
# Changes:
#
# - Changed "from Quote_0 import *" to "import quote"
#   and then updated references to quote methods in test block,
#   e.g. Quote becomes quote.Quote.
#
# - Moved "import quote" down into the test block because that is the
#   only place it is needed.
#
# - Rewrote listall so it returns a list of all the objects,
#   but leaves rendering them up to the controller.
#
# Version 0 (archived as MVC_model_0.py)
#
# - Initial roughing out.

import shelve

class Model:
    def __init__(self, location):
        self.location = location
        self.datastore = shelve.open(location)

    def create(self, item):
        self.datastore[item.uid] = item

    def retrieve(self, uid):
        if uid in self.datastore:
            return self.datastore[uid]
        else:
            return False
    
    def update(self, uid):
        #
        # Your Assignment 6 code here.
        #
        pass
        
    def delete(self, uid):
        if uid in self.datastore:
            del self.datastore[uid]
            return True
        else:
            return False

    def listall(self):
        return_set = []
        for key in self.datastore:
            return_set.append( self.datastore[key] )
        return return_set

    def close(self):
        self.datastore.close()

if __name__ == '__main__':   
    import quote
    model = 'test_model'
    print(f'Opening the model {model:s}.')
    m = Model('test_model')
    print()
    print('Creating two Quotes.')
    q = quote.Quote( 'Kent Beck', 'Optimism is an occupational hazard of programming: testing is the treatment.')
    r = quote.Quote( 'Brian Kernighan', 'Controlling complexity is the essence of computer programming.')
    print()
    print('Adding them to the model.')
    m.create(q)
    m.create(r)
    print()
    print('Displaying all objects in the model.')
    for obj in m.listall():
        print(obj)
    print()
    print('Deleting one of the objects from the model.')
    m.delete(q.uid)
    print()
    print('Displaying all objects in the model for verification.')
    for obj in m.listall():
        print(obj)
    print()
    print('Closing the model.')
    m.close()
    print()
    print('Done.')
