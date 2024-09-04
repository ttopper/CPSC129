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
        obj = Quote(author, text)
        model.create(obj)
        
    elif choice == 'r':
        pass
    
    elif choice == 'u':
        pass
    
    elif choice == 'd':
        pass
    
    elif choice == 'l':
        print('Here are the contents of the model', model_name, ':')
        model.listall()
            
    elif choice == 'q':
        over = True
        
    else:
        print('Not a valid choice!')
        
model.close()
