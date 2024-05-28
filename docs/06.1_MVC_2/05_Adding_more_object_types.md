# Adding More Object Types

Now that we have more separation between our controller and our object
class let’s take the next step towards an ObjectServer and see how our
code will have to change to accomodate other objects besides Quotes.

We’ll have to ask our user what type of object they want to create and
then branch to code to handle the creation of that type of object, so
something like this would do the trick:

``` python
    choice = input()
    
    if choice == 'c':
        print('Object types:')
        print('1. Quotation')
        print('2. Riddle')
        print('3. Famous Programmer')
        obj_type = input('What type of object would you like to create? ')

        if obj_type == '1':
            author = input('Who is the author of the quote? ')
            text = input('What did they say or write? ')
            obj = Quote(author, text)
        elif obj_type == '2':
            text = input('What is the text of the riddle? ')
            answer = input('What is the answer to the riddle? ')
            obj = Riddle(text, answer)
        elif obj_type == '3':
            first_name = input('What is their first name? ')
            last_name = input('What is their last name? ')
            nationality = input('What is their nationality? ')
            source_of_fame = input('What are they famous for? ')
            obj = FamousProgrammer(first_name, last_name, nationality, source_of_fame)

        model.create(obj)
        
    elif choice == 'r':
        pass
```

While this would work it doesn’t take advantage of the `quote`
module’s `factory` method. Assuming the other modules for Riddles and
FamousProgrammers would also be outfitted with factories the code can be
shortened to:

``` python
    choice = input()
    
    if choice == 'c':
        print('Object types:')
        print('1. Quotation')
        print('2. Riddle')
        print('3. Famous Programmer')
        obj_type = input('What type of object would you like to create? ')

        if obj_type == '1':
            obj = quote.factory()
        elif obj_type == '2':
            obj = riddle.factory()
        elif obj_type == '3':
            obj = famousProgrammer.factory()

        model.create(obj)
        
    elif choice == 'r':
        pass
```

(Note that we are establishing a _convention_ here that our objects will
be defined one to a module, and that each module will provide a factory
method. This approach is known as _programming by convention_, in
contrast to _configuration_ where we would explicitly say, in for
example a separate configuration file, what our classes are and what the
names of each of their factories are, and where they may be found.
Relying on conventions over explicit configuration is generally simpler
and reduces the amount of code, but is not as flexible.)

This is a further improvement, but there is an obvious repetitive
pattern in the code, and it should be becoming second nature to us to
replace repetitive code where we see it. In this case we can replace it
like this:

``` python
    if choice == 'c':
        # Display menu of object choices:
        print('Which type of object do you want to create:')
        print('quote')
        print('riddle')
        print('famous_programmer')
        print('Hint: For the moment you _have_ to choose quote.')
        # Get the user's choice:
        obj_type = input('? ')

        # Call the appropriate object factory:
        obj = eval(obj_type+".factory()") # e.g. quote.factory()

        model.create(obj)
```

First note that the menu of choices is changed from numerical choices,
1, 2, 3, to a list of module names. We use the module name input to
build a string. For example if the user enters `quote` we build the
string, `quote.factory()`. Then we execute that string as though it were
a Python expression using the built-in function `eval`, so the line,

``` python
        obj = eval(obj_type+".factory()") # e.g. quote.factory()
```

becomes in effect,

``` python
        obj = quote.factory() # e.g. quote.factory()
```

This is our first small example of _metaprogramming_, the art of writing
programs that write programs. In this case we wrote some code, that
generates some other code, that we then execute. Metaprogramming is a
very powerful technique that often allows for very short and expressive
code that can respond to its execution context.

Where might we go with this? Well imagine that we put all our class
modules in one directory. We could scan that directory for the module
names and build the menu of object choices programmatically. Once we had
that in place we could add new object types to our ObjectServer by just
dropping the class module into the right directory folder and not have
to change our Controller (or Model) at all.
