# Recursive Binary Search

Binary search is the first example that is often implemented with 
recursion. Remember binary search works by continually dividing the list 
in half and looking at only the first or second half of the list, 
depending on whether or not the target is higher or lower than the mid 
point of the current list or sublist. Each time the list is divided in 
half and the function repeats the steps. This sounds very recursive. The 
algorithm will divide the list in half and call itself recursively, 
either with the first half of the list or the second half of the list. 
The last thing we need to consider is when to stop. There are actually 
two stop conditions:

    1. When we've found the target.

    2. When we are considering an empty list.

Let's look at what the algorithm looks like in python.

``` python
def bin_search(lst, target):
    if not lst:
        return False
    elif lst[len(lst)//2] == target:
        return True
    elif lst[len(lst)//2] > target:
        return bin_search(lst[0:len(lst)//2], target)
    else:
        return bin_search(lst[len(lst)//2+1:], target)

print('bin_search():')
print('3 in [1,3,5,7,9,11,13,15]?', bin_search([1,3,5,7,9,11,13,15], 3))
print('5 in [1,3,5,7,9,11,13,15]?', bin_search([1,3,5,7,9,11,13,15], 5))
print('1 in [1,3,5,7,9,11,13,15]?', bin_search([1,3,5,7,9,11,13,15], 1))
print('15 in [1,3,5,7,9,11,13,15]?', bin_search([1,3,5,7,9,11,13,15], 15))
print('2 in [1,3,5,7,9,11,13,15]?', bin_search([1,3,5,7,9,11,13,15], 2))
print('6 in [1,3,5,7,9,11,13,15]?', bin_search([1,3,5,7,9,11,13,15], 6))
print('4 in [1,3,5,7,9,11,13,15]?', bin_search([1,3,5,7,9,11,13,15], 4))
print('0 in [1,3,5,7,9,11,13,15]?', bin_search([1,3,5,7,9,11,13,15], 0))
print('20 in [1,3,5,7,9,11,13,15]?', bin_search([1,3,5,7,9,11,13,15], 20))
print()
```

The recursive solution to this problem is in some ways simpler than what 
we did with explicit loops. The only tricky bits are whether the edge of 
the sublist should include the midpoint or not. You'll notice that we 
added 1 when we were looking at the second half of the list.

This solution is a good example of recursion, and it is efficient 
because it is O(log(n)) in calls to itself. This doesn't grow quickly 
even when the lists get really long.