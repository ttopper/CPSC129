# a8_1_Tests.py
# Showing how to set up a file to contain both correctness and
# performance tests.
# BUGS:
# Performance tests should use exponentially increasing values,
# e.g. 0, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, ...
# or 0, 1, 2, 4, 8, 16, 32, 64, ...

def median(lst): # wrapper function
    return _median(lst, len(lst)/2)

def _median(lst, posn):
    if len(lst) == 0:
        return None
    if len(lst)==1:
        return lst[0]
    pivot = lst[0]
    bigger = [num for num in lst if num > pivot]
    equal = [num for num in lst if num == pivot]
    smaller = [num for num in lst if num < pivot]
    if len(smaller) == posn:
        return pivot
    elif len(smaller) > posn:
        return _median(smaller, posn)
    else:
        if len(bigger) > 0 and (posn - len(smaller) - len(equal)) >= 0:
            return _median(bigger, posn-len(smaller)-len(equal))
        else:
            return equal[0]

def median2( l ):
    if len(l) == 0:
        return None
    lo = min(l)
    hi = max(l)
    considered = 0
    skipped = 0
    for item in l:
        if item > lo and item < hi:
            considered += 1
            smaller = 0
            larger = 0
            for i in l:
                if i < item:
                    smaller += 1
                elif i > item:
                    larger += 1
            if smaller == larger:
                return item
            elif smaller > larger:
                hi = item
            else:
                lo = item
        else:
            skipped += 1
    return lo


if __name__=='__main__':
    # Correctness tests:
    # Each test contains a test list and the correct median value.
    testlist = [ # Typical list, odd number of values.
                 [[37, 61, 42, 21, 19, 86, 95, 78, 54], 54],
                 # Many duplicate values.
                 [[42,42,42,42,42,42,42,42,42,42,42,42,42,43],42],
                 # Typical list, even number of values.
                 [[37, 61, 42, 21, 19, 86, 95, 78, 54, 96],57],
                 # Ordered list.
                 [[1, 2, 3, 4, 5],3],
                 # All duplicate values.
                 [[1, 1, 1],1],
                 # Empty list.
                 [[],None],
                 # One-item list.
                 [[1],1], # List with two items
                 # Two-item list.
                 [[1,2],1]
                ]
                    
    for test in testlist:
        if median(test[0]) != test[1]:
            print 'median error on:', test[0]
        if median2(test[0]) != test[1]:
            print 'median2 error on:', test[0]

    # Performance tests:
    # See BUGS at top of file!
    import random, time

    results = {}
    for trials in range(100):
        start =0.0
        start2=0.0
        N = random.randint(0, 500)
        lst = []
        for i in range(N):
            num = random.randint(1,1000000000)
            while num  in lst:
                num = random.randint(1,1000000000)
            lst.append(num)
        start = time.clock()
        m1 = median(lst) 
        t1 = float(time.clock()-start)
        start2 = time.clock()
        m2 = median2(lst)
        t2 = float(time.clock()-start2)
        c = 0 #rare case: same length of list happens twice or more, average the results
        if results.has_key(len(lst)):
            t1 = (results[len(lst)][0] + t1)/2.0
            t2 = (results[len(lst)][1] + t2)/2.0
            c = results[len(lst)][2] + 1
        results[len(lst)] = [t1, t2, c]

    result_keys = results.keys()
    result_keys.sort()

    # Note use of same field widths for title row as for data rows to produce tabular
    # output.
    print '%4s' % ('N'), '%15s' % ('Median'), '%15s' % ('Median2')
    for k in result_keys:
        print '%4d' % (k), '%15.15f' % (results[k][0]), '%15.15f' % (results[k][1])

