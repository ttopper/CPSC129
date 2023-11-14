# r0.py: Examples of recursive functions

# Infinite loop via recursion.
# Define the recursive function "printer":
##def printer():
##    print 'Hi'
##    printer()
##
##printer() # This invokes the recursive function called "printer"


# Print a list using a recursive function instead of an explicit loop.
def printer(lst):
    if lst:
        print lst[0]
        printer(lst[1:])

printer([1,2,3])
print

# Calculating factorials.
# Remember:
# 4! = 4 x 3 x 2 x 1 = 24
# 5! = 5 x 4 x 3 x 2 x 1 = 120
# n! = n x (n-1) x (n-2) x ... x 1

# factorial fuunction using an explicit loop.
def factorial(n):
    product  = 1
    for value in range(1,n+1):
        product = product * value
    return product

print '4! =', factorial(4)
print '5! =', factorial(5)
print '10! =', factorial(10)
print '20! =', factorial(20)
print '0! =', factorial(0)
print '1! =', factorial(1)
print

# factorial function using recursion.
# N.B. replaces earlier definition.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print '4! =', factorial(4)
print '5! =', factorial(5)
print '10! =', factorial(10)
print '20! =', factorial(20)
print '0! =', factorial(0)
print '1! =', factorial(1)
print

# Binary search using recursion.
def bin_search(lst, target):
    if not lst:
        return False
    elif lst[len(lst)/2] == target:
        return True
    elif lst[len(lst)/2] > target:
        return bin_search(lst[0:len(lst)/2], target)
    else:
        return bin_search(lst[len(lst)/2+1:], target)

# Tests:
print bin_search([1,3,5,7,9,11,13,15], 3)
print bin_search([1,3,5,7,9,11,13,15], 5)
print bin_search([1,3,5,7,9,11,13,15], 1)
print bin_search([1,3,5,7,9,11,13,15], 15)
print bin_search([1,3,5,7,9,11,13,15], 4)
print bin_search([1,3,5,7,9,11,13,15], 2)
print bin_search([1,3,5,7,9,11,13,15], 6)
print bin_search([1,3,5,7,9,11,13,15], 0)
print bin_search([1,3,5,7,9,11,13,15], 20)

# Working with recursive data structures
def r_sum(nested_num_list):
    sum = 0
    for element in nested_num_list:
        if type(element) == type([]):
            sum = sum + r_sum(element)
        else:
            sum = sum + element
    return sum

print r_sum([2, 9, [1, 13], 8, 6])
print r_sum([2, [[100, 7], 90], [1, 13], 8, 6])
print r_sum([2, [[13, 7], 90], [1, 100], 8, 6])
print r_sum([[[13, 7], 90], 2, [1, 100], 8, 6])
