# Recursive Data Structures

A recursive data structure is a structure that contains itself inside 
itself. An easy example is a list which may contain sublists (that may 
contain sublists etc. ).

``` python
lst = [ 1, 2, 3, [6, 7], 9, [2, [8, 9], 4]]
```

Resursive data structures are hard to traverse with explicit loops. 
Imagine we wanted to navigate through the above list to find the largest 
number. Normally we look at the first number and say it is the largest, 
before looking at each item in term to see if it is larger than our 
current largest. If the new number is largest we say it is the largest, 
otherwise we do nothing and keep going. A recursive data structure 
interupts this search because each element could be a number or it could 
be a list. There is no easy way to go into a list without recursion, but 
with recursion it is quite straightforward.


``` plaintext
def largest(lst):
    While there is more list
        If the item is a number
            If it is bigger than the largest number
                Set it to the new largest
        Otherwise
            Call largest on the sublist
    Return the largest number
```

This algorithm isn't perfect. It does not cleanly handle an empty list, 
but I will leave you to work on it for the next assignment. We will 
instead try to get the sum of all the numbers in the list and its 
sublists.

``` python
def r_sum(lst):
    ''' returns the sum of all the numbers in lst and
    its sublists.
    N.B. This is quite difficult to do without recursion.'''
    sum = 0
    for item in lst:
        if type(item) == type([]):
            sum = sum + r_sum(item)
        else:
            sum = sum + item
    return sum

print('r_sum():')
lst = [ 1, 2, 3, [6, 7], 9, [2, [8, 9], 4]]
print('The sum of [ 1, 2, 3, [6, 7], 9, [2, [8, 9], 4],[]] is', r_sum(lst))
print('The sum of [2, [[100, 7], 90], [1, 13], 8, 6] is', r_sum([2, [[100, 7], 90], [1, 13], 8, 6]))
print('The sum of [2, [[13, 7], 90], [1, 100], 8, 6] is', r_sum([2, [[13, 7], 90], [1, 100], 8, 6]))
print('The sum of [[[13, 7], 90], 2, [1, 100], 8, 6] is', r_sum([[[13, 7], 90], 2, [1, 100], 8, 6]))
print()
```

This solution uses a combination of an explicit loop and recursive 
iteration. If the next element in the list is a number we add it to our 
sum, and we only call the function recursively if we bump into a sublist.