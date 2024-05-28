# shell_sort.py
# Sorts list into ascending order.

def shell_sort(lst):
    ''' Sorts a list into ascending order.

    It does this by using Shell's algorithm:
    http://en.wikipedia.org/wiki/Shell_sort.
    '''
    step = len(lst)//2
    while step>=1:
        for start in range(step):
            for i in range(start+step, len(lst), step):
                tmp = lst[i]
                j = i-step
                while j >= step-1 and tmp < lst[j]:
                    lst[j+step] = lst[j]
                    j = j-step
                lst[j+step] = tmp
        step = step//2

if __name__=='__main__':
    l = [ 8, 3, 1, 9, 5, 6, 2, 4 ]
    print('Before: ', l)
    shell_sort( l )
    print('After:  ', l)
    l = [ 8, 3 ]
    print('Before: ', l)
    shell_sort( l )
    print('After:  ', l)
    l = [ 8 ]
    print('Before: ', l)
    shell_sort( l )
    print('After:  ', l)
    l = [ ]
    print('Before: ', l)
    shell_sort( l )
    print('After:  ', l)
    l = [ 8, 3, 8, 9, 8, 6, 3, 3 ]
    print('Before: ', l)
    shell_sort( l )
    print('After:  ', l)
