# rqsort1.py
#
# As per the weekly meeting:

def quicksort(lst):
    print('Before:', lst)
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    lo = 1
    hi = len(lst) - 1
    while lo < hi:
        while lo <= len(lst)-1 and lst[lo] < pivot:
            lo = lo + 1
        while  hi >= 1 and lst[hi] > pivot:
            hi = hi - 1
        if lo < hi:
            (lst[lo], lst[hi]) = (lst[hi], lst[lo])
    if lst[0] > lst[hi]:
        (lst[0], lst[hi]) = (lst[hi], lst[0])
    print('After:', lst)
    return quicksort(lst[0:hi-1]) + quicksort(lst[lo:])
    
l = [49, 12, 67, 87, 21, 94, 24, 73, 69, 34]
print(quicksort(l))
l = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(quicksort(l))
l = [1, 2, 3, 4, 5, 6, 7, 8]
print(quicksort(l))

            
