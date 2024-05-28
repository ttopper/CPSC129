# Shell Sort

Shell sort is a modification of linear insertion sort based on the
observation that if we move values more than 1 step toward their final
position at a time they will get there faster. This might allow us to
make fewer (potentially *far fewer*) movements.

Before we embark on the code for it, watch the description of it at the
4:30 mark of [Sorting Out
Sorting](https://youtu.be/YvTW7341kpA?t=279)
again. Notice that Shellsort does multiple linear insertion sorts of the
list with different gaps between the values being sorted. _All_ we need
to do then is to modify our linear insertion sort to apply itself to the
list multiple times with appropriate parameters each time.

Let’s begin by modifying our code for a simple linear insertion sort to
sort values that are separated by a gap or `step` size, i.e. values that
are not immediate neighbours. Where in our existing code is the
assumption that values are next to each other baked in”?

``` python
    for i in range(1, len(lst)):
        tmp = lst[i]
        j = i-1
        while j >= 0 and tmp < lst[j]:
            lst[j+1] = lst[j]
            j = j-1
        lst[j+1] = tmp
```

Well we’ll want `i` to increase by `step` instead of `1` each time, and
when we move around in the list we will want to move `step` positions at
a time instead of `1` so the `-1` and `+1` expressions will become
`-step` and `+step`.

Less obviously, our sublists will not necessarily begin in position one,
but in other positions. Let me try to show this diagrammatically.
Suppose our `step` size is 4. Then the list `lst` below will have
several sublists:

    Index:   0   1   2   3   4   5   6   7   8   9  10  11  12

    lst = [ 11, 89, 32, 42, 56, 78, 81, 39, 92, 16, 43, 57, 73]

    Sublists:
    1)      11              56              92              73
    2)          89              78              16
    3)              32              81              43
    4)                  42              39              57

    Index:   0   1   2   3   4   5   6   7   8   9  10  11  12

So the starting position for each sublist will have to vary as well. The
changed code is,

``` python
            for i in range(start+step, len(lst), step):
                tmp = lst[i]
                j = i-step
                while j >= step-1 and tmp < lst[j]:
                    lst[j+step] = lst[j]
                    j = j-step
                lst[j+step] = tmp
```

Now this bit of code sorts one sublist of items `step` apart using a
linear insertion sort. For example it might sort sublist 1) above. To
sort all the sublists at a given step size we have to loop over the
possible starting positions of the lists,

``` python
        for start in range(step):
            for i in range(start+step, len(lst), step):
                tmp = lst[i]
                j = i-step
                while j >= step-1 and tmp < lst[j]:
                    lst[j+step] = lst[j]
                    j = j-step
                lst[j+step] = tmp
```

And to ensure the list is completely sorted we have to make the step
size decline from something large — to get large efficient initial
movements — to something small to ensure the list eventually gets
sorted completely,

``` python
    step = len(lst)//2
    while step>=1:
        for start in range(step):
            for i in range(start+step, len(lst), step):
                tmp = lst[i]
                j = i-step
                while j >= step-1 and tmp < lst[j]:
                    lst[j+step] = lst[j]
                    j = j-step
                lst[j+step] = tmp
        step = step//2
```

Here I have begun with a step size equal to half the list size and then
reduced it to 1 by dividing by 2 after each pass of sorts.

Packaging it all up gives us,

``` python
# shell_sort.py
# Sorts list into ascending order.

def shell_sort(lst):
    ''' Sorts a list into ascending order.

    It does this by using Shell's algorithm:
    http://en.wikipedia.org/wiki/Shell_sort.
    '''
    step = len(lst)//2
    while step>=1:
        for start in range(step):
            for i in range(start+step, len(lst), step):
                tmp = lst[i]
                j = i-step
                while j >= step-1 and tmp < lst[j]:
                    lst[j+step] = lst[j]
                    j = j-step
                lst[j+step] = tmp
        step = step//2

if __name__=='__main__':
    lst = [ 11, 89, 32, 42, 56, 78, 81, 39, 92, 16, 43, 57, 73]
    print('Before: ', lst)
    shell_sort( lst )
    print('After: ', lst)
    
    lst = [ 8, 3 ]
    print('Before: ', lst)
    shell_sort( lst )
    print('After: ', lst)

    lst = [ 8 ]
    print('Before: ', lst)
    shell_sort( lst )
    print('After: ', lst)

    lst = [ ]
    print('Before: ', lst)
    shell_sort( lst )
    print('After: ', lst)

    lst = [ 8, 3, 8, 9, 8, 6, 3, 3 ]
    print('Before: ', lst)
    shell_sort( lst )
    print('After: ', lst)
```
