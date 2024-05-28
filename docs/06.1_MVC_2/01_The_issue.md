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
added a comment to each of the problematic lines below.

``` python
# MVC_controller_0.py
from MVC_Model_0 import *
from Quote_0 import *

model_name = input('What model would you like to work with? ')
model = Model(model_name)

over = False
while not over:
    print('''
    Actions
    -------
    c - create a quote to add to the collection             # REFERENCES QUOTE
    r - retrieve a quote from the collection and display it # REFERENCES QUOTE
    u - update a quote in the collection                    # REFERENCES QUOTE
    d - delete a quote from the collection                  # REFERENCES QUOTE
    l - list all the items in the collection
    q - exit

    Your choice?''')
    choice = input()
    
    if choice == 'c': # Create
        author = input('Who is the author of the quote? ')  # REFERENCES QUOTE
        text = input('What did they say or write? ')        # REFERENCES QUOTE
        obj = Quote(author, text)                           # QUOTE OBJECT
        model.create(obj)
        
    elif choice == 'r': # Retrieve
        uid = input( 'What is the uid of the object you wish to retrieve? ')
        if model.retrieve(uid):
            print(model.retrieve(uid))
        else:
            print('Sorry your collection does not contain an object with that uid.')
    
    elif choice == 'u': # Update
        pass
    
    elif choice == 'd': # Delete
        uid = input( 'What is the uid of the object you wish to delete? ')
        if model.delete(uid):
            print(f'Object {uid:s} successfully deleted.')
        else:
            print(f'Object {uid:s} could not be deleted.')
    
    elif choice == 'l': # List
        print('Here are the contents of the model', model_name, ':')
        model.listall()
            
    elif choice == 'q': # Quit
        over = True
        
    else:
        print('Not a valid choice!')
        
model.close()
```

**The issue:** *How can we free our controller from having to know about
the innards of the objects it processes?*
