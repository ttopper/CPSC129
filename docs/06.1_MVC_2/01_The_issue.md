# The Issue

Our first pass at refactoring our text-controller/quote database
application into an MVC architecture resulted in excellent separation of
the model component from the view-controller, but the view-controller
still has to know too much about the objects it is handling. Remember
that one of the primary goals of MVC architecture is to allow
development on the M, V and C components to proceed independently by
insulating each component from the others. The problem with our existing
code is that we cannot make changes to our object class `Quote.py`
without also making changes to our controller, `controller.py`. I’ve
highlighted the problematic lines below.

``` python
# MVC_controller_0.py
from MVC_Model_0 import *
from Quote_0 import *

model_name = raw_input('What model would you like to work with? ')
model = Model(model_name)

over = False
while not over:
    print '''
    Actions
    -------
    c - create a quote to add to the collection
    r - retrieve a quote from the collection and display it
    u - update a quote in the collection
    d - delete a quote from the collection
    l - list all the items in the collection
    q - exit

    Your choice?'''
    choice = raw_input()
    
    if choice == 'c': # Create
        author = raw_input('Who is the author of the quote? ')
        text = raw_input('What did they say or write? ')
        obj = Quote(author, text)
        model.create(obj)
        
    elif choice == 'r': # Retrieve
        uid = raw_input( 'What is the uid of the object you wish to retrieve? ')
        if model.retrieve(uid):
            print model.retrieve(uid)
        else:
            print 'Sorry your collection does not contain an object with that uid.'
    
    elif choice == 'u': # Update
        pass
    
    elif choice == 'd': # Delete
        uid = raw_input( 'What is the uid of the object you wish to delete? ')
        if model.delete(uid):
            print 'Object %s successfully deleted.' % (uid)
        else:
            print 'Object %s could not be deleted.' % (uid)
    
    elif choice == 'l': # List
        print 'Here are the contents of the model', model_name, ':'
        model.listall()
            
    elif choice == 'q': # Quit
        over = True
        
    else:
        print 'Not a valid choice!'
        
model.close()
```

**The issue:*** How can we free our controller from having to know about
the innards of the objects it processes?*
