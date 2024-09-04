# quote.py
#
# Version 3
#
# Changes:
#
# - Adding HTML methods.
# - Rename factory to be console_factory
# - Rename update to be console_update
#
# Version 2 (archived as quote_2.py)
#
# Changes:
#
# - Implemented Quote.update() method.
#
# Version 1 (archived as quote_1.py)
#
# Changes:
#
# - Changed naming convention to initial lower case to ease  importing.
#
# - Added creation method to be called from controller when new Quote
#   object is required.
#
# - Changed name of object creation routine from "create" to "factory"
#   to avoid confusion with Model.create and to follow common practice
#   of Factory patterns
#   (see e.g. http://en.wikipedia.org/wiki/Factory_method_pattern).
#
# Version 0 (archived as Quote_0.py)
#
# - Initial roughing out.

def console_factory():
    '''Handles console interaction required to create a new Quote object.'''
    author = input('Who is the author of the quote? ')
    text = input('What did they say or write? ')
    return Quote(author, text)

def HTML_factory(form_dict):
    '''Builds a Quote from the data returned in the form
    CREATION_FORM.'''
    author = form_dict[b'author'].decode('utf-8')
    text = form_dict[b'text'].decode('utf-8')
    return Quote(author, text)

# Use this template for both creation via POST and update via PUT.
CREATION_FORM = '''
<h1>Create form</h1>

<div> 
    <form method="POST" action="http://localhost/create/quote">
        <input type="hidden" name="_method" value="POST" />
        <label
for="text">Text:</label><textarea id="text" name="text" rows="3"

        cols="50">Enter the quote here...</textarea><br /> 
        <label for="author">Author:</label><input type="text" id="author"

        name="author" size="50" /><br /> 
        <label for="method">&nbsp;</label> 
        <input type="submit" value="Create" />
    </form> 
</div> 
'''

UPDATE_TEMPLATE = '''
<h1>Update form</h1>

<div>
    <form method="POST" action="http://localhost/%s">
        <input type="hidden" name="_method" value="PUT" />
        <label
for="text">Text:</label><textarea id="text" name="text" rows="3"

        cols="50">%s</textarea><br /> 
        <label for="author">Author:</label><input type="text" id="author"

        name="author" size="50" value="%s"/><br /> 
        <label for="method">&nbsp;</label> 
        <input type="submit" value="Update" />
    </form> 
</div> 
'''

HTML_TEMPLATE = '''
<div> 
    <blockquote> 
      <p><span class="quote-text">%s</span> ~
      <span class="quote-author">%s</span></p> 
    </blockquote> 

    <!-- View this quote alone. -->
    <form method="GET" action="http://localhost/%s" class="view"> 
      <input type="submit" value="View" />
    </form>

    <!-- Request the update form for this quote. -->
    <form method="GET" action="http://localhost/%s/HTML_update_form" class="update">
      <input type="submit" value="Update" />
    </form>

    <!-- Delete this quote. -->
    <form method="POST" action="http://localhost/%s" class="delete">
      <input type="hidden" name="_method" value="DELETE" />
      <input type="submit" value="Delete" /> 
    </form> 
</div>
'''

class Quote:
    def __init__(self, author='', text=''):
        self.author = author
        self.text = text
        self.uid = str(hash('Quote' + self.author + self.text))

    def __str__(self):
        return '[%s] %s said "%s"' % (self.uid, self.author, self.text)

    def HTML(self):
        return HTML_TEMPLATE % (self.text, self.author, self.uid, self.uid, self.uid)

    def HTML_update_form(self):
        return UPDATE_TEMPLATE % (self.uid, self.text, self.author)

    def console_update(self):
        '''Handles the console interaction required to modify a Quote object.'''
        
        print('The current author is:', self.author)
        change = input('Modify author (y/n)? ')
        if change in ['y', 'Y']:
            self.author = input('Enter modified author: ')
        print('The current text is:', self.text)
        change = input('Modify text (y/n)? ')
        if change in ['y', 'Y']:
            self.text = input('Enter modified text: ')
        self.uid = str(hash('Quote' + self.author + self.text))        

if __name__ == '__main__':
    def bordered(s):
        return len(s)*'='+'\n'+s+'\n'+len(s)*'-'
    
    print(bordered('Testing __init__() and __str__()'))
    q = Quote( 'Kent Beck', 'Optimism is an occupational hazard of programming: testing is the treatment.')
    r = Quote( 'Brian Kernighan', 'Controlling complexity is the essence of computer programming.')
    print('The Quote q is:')
    print('\t', q)
    print('The Quote r is:')
    print('\t', r)
    print()

    print(bordered('Testing HTML()'))
    print('Here’s the HTMl representation of q:')
    print(q.HTML())

##    print(bordered('Testing console_factory()'))
##    s = console_factory()
##    print('Here’s the new Quote object:')
##    print('\t', s)
##    print('Did factory create a Quote object?',)
##    print(type(s) == type(q)) # Checks that factory is returning a Quote object.
##    print()
##
##    print(bordered('Testing console_update()'))
##    print('The Quote q before:')
##    print('\t', q)
##    print()
##    print('Calling console_update():')
##    print()
##    q.console_update()
##    print()
##    print('The Quote q after:')
##    print('\t', q)
##    print()
