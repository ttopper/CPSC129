# MVC_model.py
#
# Version 2 (archived as MVC_model_2.py)
#
# Changes:
#
# - Implemented Model.update() method.
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
        '''Store item in the datastore using its internal uid as the key.'''
        self.datastore[item.uid] = item

    def retrieve(self, uid):
        '''Return the object with key uid.'''
        if uid in self.datastore:
            return self.datastore[uid]
        else:
            return False
    
    def update(self, uid, item):
        '''Update the entry with key uid with item.

        Since we store items by uid, this means deleting the old entry,
        and creating a new one for the modified entry
        (since it will have a different uid).'''
        if self.delete(uid):
            self.create(item)
            # Return key of newly added item.
            return item.uid 
        else:
            return None        
        
    def delete(self, uid):
        '''Delete the object with key uid.'''
        if uid in self.datastore:
            del self.datastore[uid]
            return True
        else:
            return False

    def listall(self):
        '''Return a list of all the objects in the datastore.'''
        return_set = []
        for key in self.datastore:
            return_set.append( self.datastore[key] )
        return return_set

    def close(self):
        self.datastore.close()

if __name__ == '__main__':
    def bordered(s):
        return len(s)*'='+'\n'+s+'\n'+len(s)*'-'
    
    print(bordered('Preparation...'))
    print()
    
    import quote
    print('Creating two Quotes.')
    q = quote.Quote( 'Kent Beck', 'Optimism is an occupational hazard of programming: testing is the treatment.')
    r = quote.Quote( 'Brian Kernighan', 'Controlling complexity is the essence of computer programming.')
    print()
    
    print(bordered('Testing the model constructor __init__()...'))
    model = 'test_model'
    print('Opening the model %s.' % (model))
    m = Model('test_model')
    print()

    print(bordered('Testing create()...'))
    print('Adding the two Quotes to the model.')
    m.create(q)
    m.create(r)
    print()

    print(bordered('Testing listall()...'))
    print('Displaying all objects in the model.')
    for obj in m.listall():
        print(obj)
    print()

    print(bordered('Testing delete()...'))
    print('Deleting one of the objects from the model.')
    m.delete(r.uid)
    print()
    print('Displaying all objects in the model for verification.')
    for obj in m.listall():
        print(obj)
    print()

    print(bordered('Testing update()...'))
    print('Creating modified quote.')
    modified_q = quote.Quote( 'Kent Beck', 'Optimism is an occupational hazard of programming: testing is the treatment!')
    print(m.update(q.uid, modified_q))
    print()

    print(bordered('Testing close()...'))
    print('Closing the model.')
    m.close()
    print()
    
    print(bordered('Done tests.'))
