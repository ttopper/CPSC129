def creator():
    x = raw_input('What is the attribute value? ')
    return X(x)

class X:
    def __init__(self, attr):
        self.a = attr

    def __str__(self):
        return 'My attribute is %s' % (self.a)
