# search2.py
# Linear search in an ordered list.
# Kate May 2024

def search(lst, target):
    '''Searches for a target in an ordered list.
    Returns a Boolean value.'''
    for entry in lst:
        if entry < target:
            continue
        elif entry == target:
            return True
        else:
            return False
    return False

def search_i(lst, target):
    '''Searches for a target in an ordered list.
    Returns the index of the object.'''
    for i in range(len(lst)):
        if lst[i] < target:
            continue
        elif lst[i] == target:
            return i
        else:
            return -1
    return -1

lst = [16, 18, 53, 56, 62, 78, 82, 87, 92]

print(search(lst,42))
print(search(lst,78))

print(search_i(lst,42))
print(search_i(lst,78))

