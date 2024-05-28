# Recursion Through a List

This time we are going to write a function that prints the contents of a 
list. The trick with recursion is to take the next step that would take 
you closer to the solution. Then you just call the function again and 
let the next instance of the function take the next step. The first step 
of printing a list is to print the first item, then we can use recursion 
to print the rest. We do this by printing the first item and then 
calling the function again with the rest of the list (using slicing). 


``` python
def printer(lst):
    print(lst[0])
    printer(lst[1:])
        
print('printer():')
print('The items in [1,2,3,4] are:')
printer([1,2,3,4])
print()
```
If you run the code above you will get an 'IndexError: list index out of 
range'. This occurs at the end of the list when we call printer with an 
empty list. On the next line it tries to `print(lst[0])`, and cannot 
because there is nothing at index 0. So the last thing we need to 
consider is our graceful from the recursive loop. We need to consider 
when we want to stop printing, which is when there is nothing left in 
the rest of the list to print. We can do that by double checking that 
we have a none empty list.

``` python
def printer(lst):
    if lst:
        print(lst[0])
        printer(lst[1:])
    else:
        pass
        
print('printer():')
print('The items in [1,2,3,4] are:')
printer([1,2,3,4])
print()
```

The list will evaluate as `False` if it is an empty list. If the list is 
empty we don't want to do anything, so we `pass`. Since `pass` doesn't 
actually do anything we can take that out the else statement.

``` python
def printer(lst):
    if lst:
        print(lst[0])
        printer(lst[1:])
        
print('printer():')
print('The items in [1,2,3,4] are:')
printer([1,2,3,4])
print()
```