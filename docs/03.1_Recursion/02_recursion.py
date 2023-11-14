######################
# Recursion by Example 
######################
#
# Here is the sample code developed during the screencast.
#
# I've added some more comments at few points so it comes clsoer to
# standing on its own.
#
# The file is runnable.
#

print 78*'=','\n', 'Recursion by Example', '\n', 78*'-'
print

#####################################
# Artificial example of infinite loop
#####################################
# Be ready with Ctrl-C as soon as you press F5!
##def printer():
##    print 'Hi'
##    printer()
##
##printer()

#######################################
# Print the items in a list recursively
#######################################
def printer(lst):
    if lst:
        print lst[0]
        printer(lst[1:])
        
print 'printer():'
print 'The items in [1,2,3,4] are:'
printer([1,2,3,4])
print

########################
# Calculating factorials
########################

# Review: What a factorial is.
# 4! =     4 x 3 x 2 x 1 = 24
# 5! = 5 x 4 x 3 x 2 x 1 = 120
# n! = n x (n-1) x (n-2) x ... 1

# Explicit implementation of factorial
# based on observation that n! = 1 x 2 x 3 x ... x n
def factorial(n):
    product = 1
    for value in range(1, n+1):
        product = product * value
    return product

print 'factorial() implemented using explicit iteration:'
print '4! = ', factorial(4)
print '5! = ', factorial(5)
print

# Recursive implementation of factorial
# based on observation that n! = n x (n-1)!
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print 'factorial() implemented using recursion:'
print '4! = ', factorial(4)
print '5! = ', factorial(5)
print
# N.B. Space inefficient because it is O(n) in calls to itself,
# so it uses a lot of space on the call stack.

###############################
# Binary search using recursion
###############################
def bin_search(lst, target):
    if not lst:
        return False
    elif lst[len(lst)/2] == target:
        return True
    elif lst[len(lst)/2] > target:
        return bin_search(lst[0:len(lst)/2], target)
    else:
        return bin_search(lst[len(lst)/2+1:], target)

print 'bin_search():'
print '3 in [1,3,5,7,9,11,13,15]?', bin_search([1,3,5,7,9,11,13,15], 3)
print '5 in [1,3,5,7,9,11,13,15]?', bin_search([1,3,5,7,9,11,13,15], 5)
print '1 in [1,3,5,7,9,11,13,15]?', bin_search([1,3,5,7,9,11,13,15], 1)
print '15 in [1,3,5,7,9,11,13,15]?', bin_search([1,3,5,7,9,11,13,15], 15)
print '2 in [1,3,5,7,9,11,13,15]?', bin_search([1,3,5,7,9,11,13,15], 2)
print '6 in [1,3,5,7,9,11,13,15]?', bin_search([1,3,5,7,9,11,13,15], 6)
print '4 in [1,3,5,7,9,11,13,15]?', bin_search([1,3,5,7,9,11,13,15], 4)
print '0 in [1,3,5,7,9,11,13,15]?', bin_search([1,3,5,7,9,11,13,15], 0)
print '20 in [1,3,5,7,9,11,13,15]?', bin_search([1,3,5,7,9,11,13,15], 20)
print
# N.B. Fairly space efficient, because it is O(log n) in calls to itself,
# so e.g. to search a list of 1,000,000 elements will only take 20 calls.

###########################
# Recursive data structures
###########################
# lst is a list that could contain other lists which could contain
# other lists which could contain...
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

print'r_sum():'
lst = [ 1, 2, 3, [6, 7], 9, [2, [8, 9], 4] ]
print 'The sum of [ 1, 2, 3, [6, 7], 9, [2, [8, 9], 4] ] is', r_sum(lst)
print 'The sum of [2, [[100, 7], 90], [1, 13], 8, 6] is', r_sum([2, [[100, 7], 90], [1, 13], 8, 6])
print 'The sum of [2, [[13, 7], 90], [1, 100], 8, 6] is', r_sum([2, [[13, 7], 90], [1, 100], 8, 6])
print 'The sum of [[[13, 7], 90], 2, [1, 100], 8, 6] is', r_sum([[[13, 7], 90], 2, [1, 100], 8, 6])
print

#########
# Summary
#########
print 78*'-','\n', 'S U M M A R Y', '\n', 78*'-'
print '''
Recursion SYNTAX = a function calls itself.
Recursion FUNCTIONALITY = another way of iterating.

TWO PARTS of a recursive function definition:
    BASE CASE or stopping condition (without this you have an infinite loop)
    how to move one STEP CLOSER to solution
'''

# META: Recording dimensions = 685px x 528px
