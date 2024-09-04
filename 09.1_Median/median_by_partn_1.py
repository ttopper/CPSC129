# median_by_partn.py
#
# Based on the insight that the median value will be in the middle of a list
# of sorted values, plus the hint that we may be able to find it without
# completely sorting the list, we find the median by successive partitions
# of the list.
#
# Our strategy will be to partition as in quicksort initially,
# but then to further partition only the portion that will contain the median.
#
# Version history:
# 0 - Just partitioning the list into smaller and larger.
# 1 - Add stopping condition; discover infinite loop.

def median(lst):
    return _median(lst, len(lst)//2)

def _median(lst, posn):
    # Re the leading underscore:
    # According to PEP 8 [http://www.python.org/dev/peps/pep-0008/]
    # we should use one leading underscore in the names of non-public methods,
    # i.e. ones that are for internal use only.
    print(lst, posn) # Debugging

    # Stopping condition:
    if len(lst) == 1:
        return lst[0]

    # Start by partitioning the list into a list of values smaller than
    # the pivot and a list of values larger than the pivot.
    pivot = lst[0]
    smaller = []
    larger = []
    for value in lst:
        if value < pivot:
            smaller.append(value)
        else:
            larger.append(value)
            
    # Now where to look for the "middle" value?
    #
    # If we are hunting for the value that will end up in posn 3
    # and there are 5 elements in smaller, then we better look in smaller.
    if len(smaller) > posn:
        return _median(smaller, posn)
    # But if we are looking for position 8 and there are only 5
    # elements in smaller, we better look in larger.
    # But we are no longer looking for position 8 in larger.
    # Since there are 5 elements in smaller we are now looking for
    # posn = 8 - 5 = 3 in larger.
    # (I had to draw a picture to sort that out -- you might need to too
    # to understand it).
    else:
        return _median(larger, posn-len(smaller))

if __name__ == '__main__':
    lst = [37, 61, 42, 21, 19, 86, 95, 78, 54]
    print(median(lst))
