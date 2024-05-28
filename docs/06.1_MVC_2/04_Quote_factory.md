# A Quote Factory

Here’s what a `Quote` factory looks like:

``` python
# quote.py
#
# Version 1 (archived as quote_1.py)
#
# Changes:
#
# - Changed naming convention to initial lower case to ease  importing.
#
# - Added factory method to be called from controller when new Quote
#   object is required.
#   (for background see e.g. http://en.wikipedia.org/wiki/Factory_method_pattern).
#
# Version 0 (archived as Quote_0.py)
#
# - Initial version from module 4.2 MVC 1 earlier in course.

def factory():
    author = input('Who is the author of the quote? ')
    text = input('What did they say or write? ')
    return Quote(author, text)
    
class Quote:
    def __init__(self, author='', text=''):
        self.author = author
        self.text = text
        self.uid = str(hash('Quote' + self.author + self.text))

    def __str__(self):
        return f'[{self.uid:s}] {self.author:s}] ~ {self.text:s}'
```

You can see the factory function above the `Quote` class. Function like
this are called _module methods_, because the notation makes them look
like methods of the module when we use them (remember that Python files
are called _modules_). For example:

``` python
import quote

q = quote.factory()# factory looks like a method of the module quote
                   # (Which happens because it is!)
```

The other small change to notice is that the module name has been
changed from `Quote_0.py` to `quote.py`. There are a couple of reasons
driving this. We change from capital Q `Quote` to lowercase q `quote`
because Python convention is to use lower case names for modules that
define classes. I’ve removed the version information from the module
name so it is called `quote.py` instead of `quote_1.py`, because when a
software project grows and is made up of multiple modules it becomes
tiresome _and error-prone_ to have to edit the imports in other modules
each time you update one module and change its name. Instead, the most
up-to-date version will always have the name `quote.py`, but we will
archive all versions with version numbers in their names as shown in the
comments above. Python makes the archiving easy to do using the **File →
Save Copy As...** menu command.

Using the `Quote` factory the Create portion of our controller now looks
like this:

``` python
    choice = input()
    
    if choice == 'c': # Create
        obj = quote.factory()   # CHANGED
        model.create(obj)
        
    elif choice == 'r': # Retrieve
        ...
```

Now our controller needs to know much less about `Quote` objects than it
did before. In fact it just needs to know one thing: that the `quote`
module will have a method called `factory` that will return a Python
object.
