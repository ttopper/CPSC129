# exch_sort.py
# sorts list into ascending order

def exch_sort(lst):
    ''' Sorts a list into ascending order.

    Swaps neighbouring values in the list that are out of order,
    until the entire list is in order.
    '''
    #for times in range(len(lst)-1):
    change_made = True
    while change_made:
        change_made = False
        for here in range(len(lst)-1):
            print(here)
            if lst[here]>lst[here+1]:
                lst[here], lst[here+1] = lst[here+1], lst[here]
                change_made = True

if __name__=='__main__':
    l = [ 8, 3, 1, 9, 5, 6, 2, 4 ]
    print('Before: ', l)
    exch_sort( l )
    print('After:  ', l)
    l = [ 8, 3 ]
    print('Before: ', l)
    exch_sort( l )
    print('After:  ', l)
    l = [ 8 ]
    print('Before: ', l)
    exch_sort( l )
    print('After:  ', l)
    l = [ ]
    print('Before: ', l)
    exch_sort( l )
    print('After:  ', l)
    l = [ 8, 3, 8, 9, 8, 6, 3, 3 ]
    print('Before: ', l)
    exch_sort( l )
    print('After:  ', l)


