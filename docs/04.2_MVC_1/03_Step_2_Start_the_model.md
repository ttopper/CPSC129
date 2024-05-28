# Step 2: Start the model

Although our controller was not supposed to know that we were using a 
shelve to store our data, the model will have to know. Below is a sketch 
of the code that will be required to run the three methods used in our 
controller, as well as some place holders for methods we expect to need 
later.


```python
# MVC_Model_0.py
import shelve

class Model:
    def __init__(self, location):
        self.location = location
        self.datastore = shelve.open(location)

    def create(self, uid, item):
        self.datastore[uid] = item

    def retrieve(self, uid):
        pass
    
    def update(self, uid, item):
        pass
        
    def delete(self, uid):
        pass

    def listall(self):
        for key in self.datastore:
            print(key, ':', self.datastore[key])

    def close(self):
        self.datastore.close()

if __name__ == '__main__':
    pass

```

We will need to import the model into our controller with the code 
`from MVC_Model_0 import *`.