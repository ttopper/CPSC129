# Separating Controller and Quote

Back to the immediate issue: *How can we free our controller from having
to know about the innards of the objects it processes?* Look again at
our controller with the Quote-specific parts highlighted in
are noted in the comments.

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

The striking thing is that only one our three CRD methods makes specific
reference to Quote properties (note that Update isn’t implemented in
the code above, so we’ll set it aside for the moment.). Retrieve and
Delete are already able to work with generic objects since they only
require a uid and no specific object properties to get their jobs done.

(The only other place the quote class is referenced is in the user
prompts and those we can quickly change to ’object’.)

So we want to remove the following code from `MVC_Controller_0.py` to 
somewhere else.

``` python
    if choice == 'c': # Create
        author = input('Who is the author of the quote? ')
        text = input('What did they say or write? ')
        obj = Quote(author, text)
        model.create(obj)
```

To where? The only sensible answer is to `Quote_0.py`” since it
should be the `Quote` class’s job to create `Quote` objects. But there
is a bit of a chicken and egg problem here. We must get the user input
about the quote object attributes author and text before we create a
Quote object, but since there isn’t a Quote object there is no self,
and that means it can’t be a Quote class method, but the Quote class is
by careful design the only thing in Quote_0.py. So it seems that we are
stuck because we can’t prompt for object attributes until there is an
object, but we also can’t create an object until we have attributes
(see chicken and egg).

We are not the first programmers to encounter this problem, and several
approaches have been worked out to deal with it. The one we will use is
called the Factory Pattern. The rationale is this: Where do objects come
from? They are made in factories. So if you want to create obejcts you
need a factory to do it.
