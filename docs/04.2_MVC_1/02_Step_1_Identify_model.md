# Step 1: Identify the model

Let's re-examine our CRUD controller and refactor it into an 
object-orieted MVC architecture. We are going to start by creating the 
code for the view and controller. The first step will be to look through 
our original code and identify the parts that belong to the model, so 
that we can remove them from the original file. Any references to how 
the quotes will be stored should properly be in the model, so I will 
comment out those cases in the code below and replace them with 
something more generic and object-oriented. We will start working with 
a model class, that we will write later once we know what it needs to do.

```python
# import shelve

# fname = input('What file of quotes would you like to work with? ')
model_name = input('What model would you like to work with? ')

# db = shelve.open(fname)
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
        lastname = author[author.rfind(' ')+1:]
        # db[lastname] = [author, text]
        # the general case is storing an object by a unique identifier
        model.create(uid, obj)
        
    elif choice == 'r':
        pass
    
    elif choice == 'u':
        pass
    
    elif choice == 'd':
        pass
    
    elif choice == 'l':
        print('Here are the contents of the shelve', fname, ':')
        # for key in db:
            # print(key, ':', db[key])
        model.listall()
            
    elif choice == 'q':
        over = True
        
    else:
        print('Not a valid choice!')
        
# db.close()
model.close()
```

We commented out all of the references to shelve and added a new class 
`Model`. So far model has three methods: the `create` method that take 
adds objects to the model with a unique identifier (uid), the `listall` 
method which displays the model, and the `close` method which closes the 
connection with the model.