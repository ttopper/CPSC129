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

def median(lst):
    return _median(lst, len(lst)//2)

def _median(lst, posn):
    # Re the leading underscore:
    # According to PEP 8 [http://www.python.org/dev/peps/pep-0008/]
    # we should use one leading underscore in the names of non-public methods,
    # i.e. ones that are for internal use only.

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
    return str(smaller) + ' + ' + str(larger)

if __name__ == '__main__':
    lst = [37, 61, 42, 21, 19, 86, 95, 78, 54]
    print(lst)
    print(median(lst))
