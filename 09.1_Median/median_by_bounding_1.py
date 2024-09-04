# median_by_bounding.py
#
# Based on the insight that the median is the value
# that has the same number of values larger than it and smaller than it.
#
# Version history:
#
# 0 First inefficient attempt. Fails on some lists.
# 1 Refine test to account for possibility of duplicate values in list.
#
def median(lst):
    # It could be any item in the list, so we check each one.
    for item in lst:
        # Check if this item is the median.
        # Count smaller and larger values.
        count_smaller = 0
        count_larger = 0
        for value in lst:
            if value < item:
                count_smaller = count_smaller + 1
            elif value > item:
                count_larger = count_larger + 1
        # Refined logic to account for duplicates.
        # Test: If it is the median then half or less of the values
        # will be smaller than it, and half or less will be larger than it,
        # i.e. the largest the "halves" could be is:
        # < < < < = > > > >
        # but it could also be
        # < < < = = = = > >
        # in which case the <s and >s each account for less than half
        # the values.
        if count_smaller <= len(lst)//2 and count_larger <= len(lst)//2:
            return item

if __name__ == '__main__':
    print(median([37, 61, 42, 21, 19, 86, 95, 78, 54]))
    print(median([1]))
    print(median([1, 42, 99]))
    print(median([1, 5, 42, 42, 42, 99]))
    print(median([42, 42, 42, 99]))
