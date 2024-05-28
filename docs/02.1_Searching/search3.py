# search3.py
# Binary search in an ordered list.
# Kate May 2024

import random

def search(lst, target):
    '''Searches for a target in an ordered list.
    Returns a Boolean value.'''
    lo = 0
    hi = len(lst)-1
    mid = (lo+hi)//2
    while lo != mid:
        if lst[mid] == target:
            return True
        elif target < lst[mid]:
            hi = mid
        else:
            lo = mid
        mid = (lo+hi)//2
    return False

if __name__ == '__main__':
    n = int(input('How long do you want your test list to be?'))
    lst = []
    lst.append(random.randint(1,10))
    for i in range(0,n-1):
        lst.append(lst[i] + random.randint(2,6))
    print(lst)
        
    # Testing for targets that are present
    for target in lst:
        if search(lst,target) != True:
            print('Failed on present target:', target)

    # Testing for targets that are absent
    for target in lst:
        if search(lst,target+1) != False:
            print('Failed on absent target:', target+1)

    # Absent off the left hand end of the list
    if search(lst,lst[0]-1) != False:
        print('Failed on absent target:', lst[0]-1)

