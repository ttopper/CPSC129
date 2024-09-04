# seln_sort.py
# sorts list into ascending order

def seln_sort(lst):
    ''' Sorts a list into ascending order.

    Considers every position in the list, scanning the remainder of
    the list to find the value (smallest) that belongs here, and then
    swapping it into position.
    '''
    for here in range(len(lst)):
        smallest = here
        for test in range(here+1, len(lst)):
            if lst[test] < lst[smallest]:
                smallest = test
        lst[here], lst[smallest] = lst[smallest], lst[here]

if __name__=='__main__':
    l = [ 8, 3, 1, 9, 5, 6, 2, 4 ]
    print('Before: ', l)
    seln_sort( l )
    print('After:  ', l)
    l = [ 8, 3 ]
    print('Before: ', l)
    seln_sort( l )
    print('After:  ', l)
    l = [ 8 ]
    print('Before: ', l)
    seln_sort( l )
    print('After:  ', l)
    l = [ ]
    print('Before: ', l)
    seln_sort( l )
    print('After:  ', l)
    l = [ 8, 3, 8, 9, 8, 6, 3, 3 ]
    print('Before: ', l)
    seln_sort( l )
    print('After:  ', l)


