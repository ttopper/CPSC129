# median_by_bounding.py
#
# Based on the insight that the median is the value
# that has the same number of values larger than it and smaller than it.
#
# Version history:
# 0 First inefficient attempt. Fails on some lists.
# 1 Refine test to account for possibility of duplicate values in list.
# 2 Let's use what we are learning about the list to reduce the number
#   of comparisons we do.
#   
def median(lst):
    lo = min(lst)
    hi = max(lst)
    # It could be any item in the list, so we check each one.
    for item in lst:
        print('Checking', item)
        # Check if this item is the median,
        # but don't bother if it is outside the possible range.
        if item >= lo and item <= hi:
            count_smaller = 0
            count_larger = 0
            for value in lst:
                if value < item:
                    count_smaller = count_smaller + 1
                elif value > item:
                    count_larger = count_larger + 1
            if count_smaller <= len(lst)//2 and count_larger <= len(lst)//2:
                return item
            # update our bounds
            elif count_smaller > count_larger:
                hi = item
            else:
                lo = item

if __name__ == '__main__':
    print(median([37, 61, 42, 21, 19, 86, 95, 78, 54]))
    print(median([1]))
    print(median([1, 42, 99]))
    print(median([1, 42, 42, 42, 99]))
    print(median([1, 5, 42, 42, 99]))
    print(median([42, 42, 42, 42, 99]))
