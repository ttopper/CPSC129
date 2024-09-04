# Quote_0.py

class Quote:
    def __init__(self, author='', text=''):
        self.author = author
        self.text = text
        self.uid = str(hash('Quote' + self.author + self.text))

    def __str__(self):
        return f'[{self.uid:s}] {self.author:s}] ~ {self.text:s}'
    
if __name__ == '__main__':
    q = Quote( 'Kent Beck', 'Optimism is an occupational hazard of programming: testing is the treatment.')
    r = Quote( 'Brian Kernighan', 'Controlling complexity is the essence of computer programming.')
    print(q)
    print(r)
