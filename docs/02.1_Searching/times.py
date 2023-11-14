length = int(raw_input('List length? '))

##print 'Length Times'
##
##for length in range(100, 2000, 100):
##    print '%6d' % (length),
times = 1
while length > 1:
    length = length / 2
    times = times + 1
##print '%5d' % (times)
print 'At most', times, 'guesses.'
