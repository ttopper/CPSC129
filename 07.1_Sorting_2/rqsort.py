# rqsort.py

def quicksort(lst):
    rqsort(lst, 0, len(lst)-1)
    
def rqsort(lst, lo, hi):
    print('Before: ', lst[lo:hi+1])
    pivot = lst[lo]
    bigger = lo+1
    smaller = hi
    while bigger < smaller:
        while lst[bigger] < pivot:
            bigger += 1
        while lst[smaller] > pivot:
            smaller -= 1
        if bigger < smaller:
            lst[smaller], lst[bigger] = lst[bigger], lst[smaller]
    lst[lo], lst[smaller] = lst[smaller], lst[lo]
    print('After: ', lst[lo:hi+1])
    rqsort(lst, lo, smaller-1)
    rqsort(lst, smaller+1, hi)

l = [49, 12, 67, 87, 21, 94, 24, 73, 69, 34]
quicksort(l)
