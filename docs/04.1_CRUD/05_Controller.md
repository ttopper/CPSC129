# A controller for our database

"Wait a minute! What database?" Is that your first thought? Because it
would be a fair one if you hadn't noticed that once we have a
persistent dictionary-like storage, e.g. a shelve, we have a database.
And if we have a database we need some way to control it. Control what
exactly? The actions that get performed on that database. Those actions
are most easily recalled by remembering the acronym CRUD,

-   **C**reate: We need a way to create a new entry in the database.
-   **R**etrieve: We need to be able to retrieve an entry in the
    database.
-   **U**pdate: We need a way to update an existing entry in the
    database.
-   **D**elete: We need a way to delete an entry in the database.

Those are really the only things we can do with a database, though the
retrieve operation is a little slippery because it's unclear what it
means. Does it refer just to accessing an entry whose key you know, or
does it also include finding entries that match certain criteria?
Because the latter operation, searching, is a very complicated task
(basically it's the problem Google is being rewarded for "solving").

What we'll do here is to build a little controller[^*] that will let us
work on our database of quotations. The pseudocode for most controllers
is similar[^**],

```plaintext
Forever
    Display the possible actions
    Get the user's choice of action
    Execute the code corresponding to the chosen action
```
The Python code for CRUD operations on a shelve of quotes could look
like,

```python
# crud_controller.py
import shelve
fname = input('What file of quotes would you like to work with? ')
db = shelve.open(fname)

# Forever
over = False
while not over:

    # Display the possible actions
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

    # Get the user's choice of action
    choice = input()
    
    # Execute the code corresponding to the chosen action
    if choice == 'c':
        pass       
    elif choice == 'r':
        pass   
    elif choice == 'u':
        pass   
    elif choice == 'd':
        pass  
    elif choice == 'l':
        pass            
    elif choice == 'q':
        over = True       
    else:
        print('Not a valid choice!')
        
db.close()
```

The code is a fairly straightforward translation of the pseudocode:

-   The Forever loop is implemented with a quit option.
-   The possible actions are displayed using a triple quoted string to
    display a menu of choices.
-   We get the user's choice via a call to `input`.
-   We choose the appropriate action using an `if-elif-else` cascade.

The `pass` statements are new, but they do nothing. Truly. If they do
nothing why have them? Because you can't have nothing between
an `if` and an `elif` or between a pair of `elif`s,

```plaintext
>>> if x > 5:
elif x == 5:
  File "<pyshell#59>", line 2
    elif x == 5:
       ^
IndentationError: expected an indented block
>>> 
```

The job of a `pass` statement is to have a statement somewhere you
don't want one by 1) being a statement, but 2) doing nothing. Most
languages provide a "do nothing" statement. They were originally
included because sometimes the structure that is otherwise the natural
choice would have a blank where a statement is required. The solution:
create a do nothing statement to avoid having a blank slot. They are
used most commonly now during program construction as I have done above.
They serve as temporary stand-ins when you are writing a program from
the top-down or outside-in, i.e. from the general to the specific,
because you can write the overall framework and put these dummy
statements in as placeholders until you are ready to write more detailed
code.

Here's another version with a couple of the actions filled in,

```python
# crud_controller.py
import shelve
fname = input('What file of quotes would you like to work with? ')
db = shelve.open(fname)
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
        db[lastname] = [author, text]
        
    elif choice == 'r':
        pass
    
    elif choice == 'u':
        pass
    
    elif choice == 'd':
        pass
    
    elif choice == 'l':
        print('Here are the contents of the shelve', fname, ':')
        for key in db:
            print(key, ':', db[key])
            
    elif choice == 'q':
        over = True
        
    else:
        print('Not a valid choice!')
        
db.close()
```

and a sample run,

```plaintext
>>> 
What file of quotes would you like to work with? quotes
    Actions
    -------
    c - create a quote to add to the collection
    r - retrieve a quote from the collection and display it
    u - update a quote in the collection
    d - delete a quote from the collection
    l - list all the items in the collection
    q - exit
    Your choice?
l
Here are the contents of the shelve quotes :
Beck : ['Kent Beck', 'Optimism is an occupational hazard of programming: 
testing is the treatment.']
Kernighan : ['Brian Kernighan', 'Controlling complexity is the essence 
of computer programming.']
    Actions
    -------
    c - create a quote to add to the collection
    r - retrieve a quote from the collection and display it
    u - update a quote in the collection
    d - delete a quote from the collection
    l - list all the items in the collection
    q - exit
    Your choice?
c
Who is the author of the quote? Fred Flintstone
What did they say or write? Yaba daba doo!
    Actions
    -------
    c - create a quote to add to the collection
    r - retrieve a quote from the collection and display it
    u - update a quote in the collection
    d - delete a quote from the collection
    l - list all the items in the collection
    q - exit
    Your choice?
l
Here are the contents of the shelve quotes :
Flintstone : ['Fred Flintstone', 'Yaba daba doo!']
Beck : ['Kent Beck', 'Optimism is an occupational hazard of programming: 
testing is the treatment.']
Kernighan : ['Brian Kernighan', 'Controlling complexity is the essence 
of computer programming.']
    Actions
    -------
    c - create a quote to add to the collection
    r - retrieve a quote from the collection and display it
    u - update a quote in the collection
    d - delete a quote from the collection
    l - list all the items in the collection
    q - exit
    Your choice?
q
>>> 
```

What about the other actions? Check out the assignment :-)

------------------------------------------------------------------------

[^*]: Controllers are ubiquitous in computing. If you have a device or
server you want to manipulate through software then you need a
controller.

[^**]: Which may have you thinking that it should be possible to build a
universal controller which with some OOP and an MVC architecture it
pretty much is. OOP will be the subject of the remaining four modules of
this course. MVC you can either Google or wait to study in CPSC 129.
