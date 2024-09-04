done = False
while not done:
    try:
        x = int(raw_input('Please enter an integer value: '))
        done = True
    except ValueError:
        print 'Give me an integer damnit!'
print 'Thanks!'
