# shell_sort.py
# Sorts list into ascending order.

def shell_sort(lst):
    ''' Sorts a list into ascending order.

    It does this by using Shell's algorithm:
    http://en.wikipedia.org/wiki/Shell_sort.
    '''
    step = len(lst)/2
    while step>=1:
        for start in range(step):
            for i in range(start+step, len(lst), step):
                tmp = lst[i]
                j = i-step
                while j >= step-1 and tmp < lst[j]:
                    lst[j+step] = lst[j]
                    j = j-step
                lst[j+step] = tmp
        step = step/2

if __name__=='__main__':
    lst = [ 11, 89, 32, 42, 56, 78, 81, 39, 92, 16, 43, 57, 73]
    print 'Before: ', lst
    shell_sort( lst )
    print 'After: ', lst
    
    lst = [ 8, 3 ]
    print 'Before: ', lst
    shell_sort( lst )
    print 'After: ', lst
    lst = [ 8 ]
    print 'Before: ', lst
    shell_sort( lst )
    print 'After: ', lst
    lst = [ ]
    print 'Before: ', lst
    shell_sort( lst )
    print 'After: ', lst
    lst = [ 8, 3, 8, 9, 8, 6, 3, 3 ]
    print 'Before: ', lst
    shell_sort( lst )
    print 'After: ', lst


