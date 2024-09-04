# quote.py
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

def factory():
    '''Handles console interaction required to create a new Quote object.'''
    author = input('Who is the author of the quote? ')
    text = input('What did they say or write? ')
    return Quote(author, text)
    
class Quote:
    def __init__(self, author='', text=''):
        self.author = author
        self.text = text
        self.uid = str(hash('Quote' + self.author + self.text))

    def __str__(self):
        return '[%s] %s said "%s"' % (self.uid, self.author, self.text)

    def update(self):
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

    print(bordered('Testing factory()'))
    s = factory()
    print('Here’s the new Quote object:')
    print('\t', s)
    print('Did factory create a Quote object?',)
    print(type(s) == type(q)) # Checks that factory is returning a Quote object.
    print()

    print(bordered('Testing update()'))
    print('The Quote q before:')
    print('\t', q)
    print()
    print('Calling console_update():')
    print()
    q.update()
    print()
    print('The Quote q after:')
    print('\t', q)
    print()

