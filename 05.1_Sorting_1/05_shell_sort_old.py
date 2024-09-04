# a4_2.py
# Misha Hampl
# 02.25.08


def shell_sort_alt(lst):
    '''Sorts a list in ascending order.

    It does this by considering each value after the first one,
    and inserting it into the front (sorted) part of the list
    where it belongs.
    Uses step pattern ..., 121, 40, 13, 4, 1
    '''
    step = 1
    while step < len(lst):
        step = (step*3)+1
    while step >=1:
        for start in range(step):
            for i in range(start+step, len(lst), step):
                tmp = lst[i]
                j = i-step
                while j >= step-1 and tmp < lst[j]:
                    lst[j+step] = lst[j]
                    j = j-step
                lst[j+step] = tmp
        step = (step-1)//3


def shell_sort(lst):
    '''Sorts a list in ascending order.

    It does this by considering each value after the first one,
    and inserting it into the front (sorted) part of the list
    where it belongs.
    Uses step pattern ..., 16, 8, 4, 2, 1
    '''
    step = len(lst)//2
    while step >=1:
        for start in range(step):
            for i in range(start+step, len(lst), step):
                tmp = lst[i]
                j = i-step
                while j >= step-1 and tmp < lst[j]:
                    lst[j+step] = lst[j]
                    j = j-step
                lst[j+step] = tmp
        step = step//2


if __name__ == '__main__':
    l = [ 8, 3, 1, 9, 5, 6, 2, 4, 3, 11, 9, 5, 2, 7, 12, 3, 8, 9, 13, 1 ]
    print('Before: ', l)
    shell_sort( l )
    print('After: ', l)

##    from time import time
##    from random import randint
##
##
##    l = []
##    for i in range(0, 10000):
##        l.append(randint(0,1000))
##    start = time()
##    shell_sort(l)
##    print "Original step method took:"
##    print time() - start
##    print "Seconds"
##    
##    print
##    print
##    
##    l = []
##    for i in range(0, 10000):
##        l.append(randint(0,1000))
##    start = time()
##    shell_sort_alt(l)
##    print "Alternat step method took:"
##    print time() - start
##    print "seconds"
##
##                
