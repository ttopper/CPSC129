# ins_sort.py
# Sorts list into ascending order.

def ins_sort(lst):
    ''' Sorts a list into ascending order.

    It does this by considering each value after the first one,
    and inserting it into the front (sorted) part of the list
    where it belongs. '''
    for i in range(1, len(lst)):
        tmp = lst[i]
        j = i-1
        while j >= 0 and tmp < lst[j]:
            lst[j+1] = lst[j]
            j = j-1
        lst[j+1] = tmp

if __name__=='__main__':
    l = [ 8, 3, 1, 9, 5, 6, 2, 4 ]
    print('Before: ', l)
    ins_sort( l )
    print('After:  ', l)
    l = [ 8, 3 ]
    print('Before: ', l)
    ins_sort( l )
    print('After:  ', l)
    l = [ 8 ]
    print('Before: ', l)
    ins_sort( l )
    print('After:  ', l)
    l = [ ]
    print('Before: ', l)
    ins_sort( l )
    print('After:  ', l)
    l = [ 8, 3, 8, 9, 8, 6, 3, 3 ]
    print('Before: ', l)
    ins_sort( l )
    print('After:  ', l)


