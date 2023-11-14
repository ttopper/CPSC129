# crud_controller.py
import shelve

fname = raw_input('What file of quotes would you like to work with? ')
db = shelve.open(fname)

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
    
    if choice == 'c':
        author = raw_input('Who is the author of the quote? ')
        text = raw_input('What did they say or write? ')
        lastname = author[author.rfind(' ')+1:]
        db[lastname] = [author, text]
        
    elif choice == 'r':
        pass
    
    elif choice == 'u':
        pass
    
    elif choice == 'd':
        pass
    
    elif choice == 'l':
        print 'Here are the contents of the shelve', fname, ':'
        for key in db:
            print key, ':', db[key]
            
    elif choice == 'q':
        over = True
        
    else:
        print 'Not a valid choice!'
        
db.close()
