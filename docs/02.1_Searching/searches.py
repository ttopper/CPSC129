def lu_search(lst, target):
    for entry in lst:
        if entry == target:
            return True
    return False

def lu_search_i(lst, target):
    for i in range(0, len(lst)):
        if lst[i] == target:
            return i
    return -1

def lo_search(lst, target):
    for entry in lst:
        if entry < target:
            continue
        elif entry == target:
            return True
        else:
            return False
    return False

def lo_search_i(lst, target):
    for i in range(0, len(lst)):
        if lst[i] < target:
            continue
        elif lst[i] == target:
            return i
        else:
            return -1
    return -1

def bin_search(lst, target):
    lo = 0
    hi = len(lst) - 1
    mid = (lo + hi) / 2
    while lo != mid:
        if lst[mid] == target:
            return True
        elif lst[mid] > target:
            hi = mid
        else:
            lo = mid
        mid = (lo + hi) / 2
    return False

# Notes on binary search:
#
#       0   1   2   3   4   5   6   7   8
#lst = [16, 18, 53, 56, 62, 78, 82, 87, 92]
#      lo              mid             hi
#                      lo      mid     hi
#                      lo  mid hi
#      lo              mid             hi
#      lo      mid     hi
#      lo  mid  hi
#        lo/mid hi

def interp_search(lst, target):
    pass

# Notes on Interpolative Search:
#         10                                          30       
# [ ..., 1000, , , , , , , , , , , , , , , , , , , , 2000, ...]
#         lo                                        hi
# nxt = lo + (hi-lo)/((lst[hi]-lst[lo])/(target-lst[lo]))


if __name__ == '__main__':
    import random
    
    #lst = [16, 18, 53, 56, 62, 78, 82, 87, 92]

    # Generate randomized ordered list of desired length:
    n = int(raw_input('How long a list to use for testing? '))
    lst = []
    prev = random.randint(1, 10) # random first value in list
    lst.append(prev)
    for values in range(1, n):
        # Generate successive values by adding random increment to previous value
        prev = prev + random.randint(2, 5) 
        lst.append(prev)
    print lst

    tests = [ [bin_search, 'bin_search'], [lu_search, 'lu_search']]
    for test in tests:
        search = test[0]
        label = test[1]
        
        # Testing for targets that are present.
        for item in lst:
            target = item
            if search(lst, target) != True:
                print label, 'failed on present target:', target

        # Testing for targets that are absent within list, and off RHE of list.
        for item in lst:
            target = item + 1
            if search(lst, target) != False:
                print label, 'failed on absent target:', target

        # Testing for target absent off LHE of list.
        target = lst[0] - 1
        if search(lst, target) != False:
            print label, 'failed on absent target:', target
        
