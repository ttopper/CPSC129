# quote.py
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

    #
    # Your Assignment 6 code here.
    #

if __name__ == '__main__':
    
    q = Quote( 'Kent Beck', 'Optimism is an occupational hazard of programming: testing is the treatment.')
    r = Quote( 'Brian Kernighan', 'Controlling complexity is the essence of computer programming.')
    print(q)
    print(r)
    print('Testing new factory function:')
    s = factory()
    print(type(s) == type(q)) # Checks that factory is returning a Quote object.
    print(s)
