# Step 3: The Quote class

Now we are going to update our controller and our model so that they can 
handle different types of data, not just quotes. To do that we will have 
to go through our code and identify areas that are specific to the 
structure of quotes. The main change we are going to make is that we are 
going to ask objects in our model to generate their own unique 
identifier (uid). So far we've been using the author name as the uid, 
but there are some limitations to using the author name. The biggest one 
so far has been that the same author can have multiple quotes. Moving 
forward each object in the model is going to generate its own uid. Let's 
look at how that changes the code in the model.


```python
# MVC_Model_0.py
import shelve

class Model:
    def __init__(self, location):
        self.location = location
        self.datastore = shelve.open(location)

    def create(self, item):
        self.datastore[uid] = item

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
    pass

```

Now that we have removed the uid from the model, we also need to edit 
the controller. This will change how we create new objects, and later 
how we retrieve, update, and delete them. In the controller we stop 
assuming that our model only handles quotes, and will instead create a 
`Quote` object. The new quote object will generate the uid and the 
create method will use the uid provided by the object quote.


```python
from MVC_Model_0 import *
from Quote_0 import *
model_name = input('What model would you like to work with? ')

model = Model(model_name)

over = False
while not over:
    print('''
    Actions
    -------
    c - create a quote to add to the collection
    r - retrieve a quote from the collection and display it
    u - update a quote in the collection
    d - delete a quote from the collection
    l - list all the items in the collection
    q - exit

    Your choice?''')
    choice = input()
    
    if choice == 'c':
        author = input('Who is the author of the quote? ')
        text = input('What did they say or write? ')
        #lastname = author[author.rfind(' ')+1:]
        obj = Quote(author, text)
        model.create(obj)
        
    elif choice == 'r':
        pass
    
    elif choice == 'u':
        pass
    
    elif choice == 'd':
        pass
    
    elif choice == 'l':
        print('Here are the contents of the shelve', fname, ':')
        model.listall()
            
    elif choice == 'q':
        over = True
        
    else:
        print('Not a valid choice!')
        
model.close()
```

The last thing we are going to do is create the `Quote` class. Quote 
objects will need to be intialized and displayed. When a quote is 
initialized it generates its own uid using `hash`. 

```python
# Quote_0.py

class Quote:
    def __init__(self, author='', text=''):
        self.author = author
        self.text = text
        self.uid = str(hash('Quote' + self.author + self.text))

    def __str__(self):
        return f'[{self.uid:s}] {self.author:s}] ~ {self.text:s}'

if __name__ == '__main__':
    q = Quote( 'Kent Beck', 'Optimism is an occupational hazard of programming: testing is the treatment.')
    r = Quote( 'Brian Kernighan', 'Controlling complexity is the essence of computer programming.')
    print(q)
    print(r)
```