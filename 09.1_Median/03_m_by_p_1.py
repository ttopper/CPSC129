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
def median(lst):
    return _median(lst, len(lst)//2)

def _median(lst, posn):
    print(lst, posn) # Debugging
    pivot = lst[0]
    smaller = []
    larger = []
    for value in lst:
        if value < pivot:
            smaller.append(value)
        else:
            larger.append(value)
    # < < < < < < P > >
    #         M
    if len(smaller) > posn:
        return _median(smaller, posn)
    # < < P > > > > > >
    #         M
    else:
        return _median(larger, posn-len(smaller))

if __name__ == '__main__':
    lst = [37, 61, 42, 21, 19, 86, 95, 78, 54]
    print(lst)
    print(median(lst))
