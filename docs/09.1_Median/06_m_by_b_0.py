# median_by_bounding.py
#
# Based on the insight that the median is the value
# that has the same number of values larger than it and smaller than it.

def median(lst):
    for item in lst:
        count_smaller = 0
        count_larger = 0
        for value in lst:
            if value < item:
                count_smaller += 1
            elif value > item:
                count_larger += 1
        if count_smaller == count_larger:
            return item

if __name__ == '__main__':
    print(median([37, 61, 42, 21, 19, 86, 95, 78, 54]))
    print(median([1]))
    print(median([1, 42, 99]))
    print(median([1, 42, 42, 42, 99]))
    print(median([1, 5, 42, 42, 99]))
    print(median([42, 42, 42, 42, 99]))
