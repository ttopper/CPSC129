# search1.py
# Linear search in an unordered list
# Kate May 2024

def search(lst, target):
    '''Searches for a target in an unordered list.
    Returns a Boolean value.'''
    for entry in lst:
        if entry == target:
            return True
    return False


def search_i(lst, target):
    '''Searches for a target in an unordered list.
    Returns the index of the object.'''
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

lst = [56, 82, 18, 62, 87, 78, 92, 16, 53]

print(search(lst,42))
print(search(lst,78))

print(search_i(lst,42))
print(search_i(lst,78))

