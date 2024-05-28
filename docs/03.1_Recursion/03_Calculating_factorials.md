# Caculating Factorials

Factorials are a mathematical notation using an exclamation mark (e.g. 
4!). We solve 4! by mulitplying 4 x 3 x 2 x 1 = 24. Below are the 
solutions of some of the lower factorials, as well as the general 
solution using n. 

``` plaintext
Review: What a factorial is.
1! =                 1 = 1
2! =             2 x 1 = 2
3! =         3 x 2 x 1 = 6
4! =     4 x 3 x 2 x 1 = 24
5! = 5 x 4 x 3 x 2 x 1 = 120

n! = n x (n-1) x (n-2) x ... x 1
```

Let's first write a function using an explicite loop (no recursion) to 
solve factorial. The easiest way to understand how to do this is to look 
at the general solution and read it backwards... 1 x 2 x ... x n. We can 
easily do this in a for loop by looping through all the values 1 to and 
keeping track of the product as we go.


``` python
def factorial(n):
    product = 1
    for value in range(1, n+1):
        product = product * value
    return product

print('factorial() implemented using explicit iteration:')
print('4! = ', factorial(4))
print('5! = ', factorial(5))
print()
```

Let's try writing this again with a recursive approach. How could we 
define this function recursively? It is important to notice that 5! is 
equal to 5 x 4! (a recursive definition). That means that in general 
`n! = n * (n-1)!.` This provides the recursive element of our function, 
but we also need to consider when to stop. Looking at our table the 
recursion naturally stops when `n == 1`, so we will use an if-else 
statement to make sure our function exits smoothly.

``` python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print('factorial() implemented using recursion:')
print('4! = ', factorial(4))
print('5! = ', factorial(5))
print()
```

This solution is a good example of recursion, but it is actually 
inefficient because it is O(n) in calls to itself, so it uses a lot of 
space on the call stack.