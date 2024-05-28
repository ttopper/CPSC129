# Recursion by Example

Recursion is the repeated application of some procedure. This is a form 
of iteration (like our `while` and `for` loops), it is something that 
our programs repeat multiple times. Recursion occurs when a function 
calls itself, which causes the function to run repeatedly. Below is a 
very simple application of recursion. *WARNING* - this code fragment 
causes an infinite loop, so if you run it be ready to hit ctrl-C to 
cancel the program.

``` python
# Be ready with Ctrl-C as soon as you press F5!
def printer():
    print('Hi')
    printer()

printer()
```

This function will start running, print `'Hi'`, and then calls itself. 
Then that will start running, print `'Hi'`, then calls itself, which 
will start running... You get the idea. The call to itself inside of the 
function is what makes this a recursive function. The result of this 
function is that will it keeps printing 'Hi' forever (or until you 
cancel it). That is because there is no reason for this program to ever 
end. We've found an infinite loop!

If you run and cancel this program you'll notice something interesting 
about the Traceback (angry red text). This tells us what was running 
when the program was cancelled. You will notice that the message is very 
long, and lists the same file, line, and function repeatedly. You may 
also get the message 'RecursionError: maximum recursion depth exceeded'. 
The reason for this is that each time we call the function we are 
pausing the current function and beginnng a new version of the function. 
The state information of the current call (i.e. the values of the local 
variables) is pushed onto a stack (like appending to the end of a list).
In essence this results in many copies of the function stored on the 
stack that all needed to be cancelled. There was one copy of `printer` 
running for every 'Hi' that was printed.

Some programming languages only use resursion for iteration, and don't 
have anything like a while loop or a for loop defined. Recursion can be 
a very powerful and very simple way of expressing some algorithms. To 
use recursion effectively we need to define functions that exit 
elegantly and don't cause infinite loops.
