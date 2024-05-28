# MVC_Model_0.py
import shelve
from Quote_0 import *

class Model:
    def __init__(self, location):
        self.location = location
        self.datastore = shelve.open(location)

    def create(self, item):
        self.datastore[item.uid] = item

    def retrieve(self, item):
        pass
    
    def update(self, item):
        pass
        
    def delete(self, item):
        pass

    def listall(self):
        for key in self.datastore:
            print(key, ':', self.datastore[key])

    def close(self):
        self.datastore.close()

if __name__ == '__main__':   
    q = Quote( 'Kent Beck', 'Optimism is an occupational hazard of programming: testing is the treatment.')
    m = Model('test_model')
    m.create(q)
    r = Quote( 'Brian Kernighan', 'Controlling complexity is the essence of computer programming.')
    m.create(r)
    m.listall()
    m.close()
