# Assignment 3

## Problems

1.  Another pencil and paper”[^*] exercise on algorithmic complexity.

    a.  A straight selection sort algorithm,O(n^2^), takes 10ms
        (milliseconds) to sort an array of 100 elements. How long do you
        estimate it will take to sort an array with 2000 elements?

    b.  An O(2^n^) algorithm takes 5 seconds to process a dataset with
        20 entries. How long will it take it to process a dataset with
        300 entries?

    c.  A Shellsort implementation, O(n log n), takes 11 seconds to sort
        a list of 1,000 elements. How long do you estimate it will take
        to sort a list with 40,000 elements?

    d.  An O(n!) algorithm takes 2 seconds to process a list with 10
        entries. How long will it take to process a list with 100
        entries?

    e.  A binary search of a list of 2,000 items takes takes 2
        microseconds. How long do you estimate it will take to search a
        list with 120,000 elements?

    [^*] Pencil and paper” does not mean that it _has_ to be done
    with pencil and paper, it just points out that it _can_ be and
    doesn’t require a program as an answer. The Python shell might
    provide a convenient way of doing the calculations and you could
    submit the Python expressions that calculate the answers, e.g. an
    answer for a2p2e might be
    `print pow(2,12000)/pow(2,100)*4, 'microseconds'`.

2.  Here are a couple of problems just to give you a bit of practice
    with recursion and help you internalize the idea.
    a.  Write a recursive function called `list_max` named that returns
        the largest value in a list it is passed. Note that like some of
        the lists in the notes the list could be recursive, e.g.
        `[2, [[100, 7], 90], [1, 13], 8, 6]`.

    b.  Write a recursive function called `is_palindrome` that
        determines if a string it is passed is a palindrome. (A
        palindrome is a string that is the same forward and backward,
        i.e. where the first and last letters are the same and the
        second and second-last letters are the same etc., e.g. eye”,
        dad” and madam” are palindromes. Word enthusiasts also
        count phrases that are palindromic once you remove the spaces,
        capitalization and punctuation, e.g. Do geese see God?” and
        Murder for a jar of red rum.”)

    c.  Write a recursive function called `power` that raises a number
        to an exponent. The naive way is to use an explicit loop to
        multiply the number by itself the required number of times, e.g.
        computing 2^16^ would require 15 multiplications. But we can be
        more efficient by noting that 2^16^ = 2^8^ × 2^8^, and that 2^8^
        = 2^4^ × 2^4^ and that 2^4^ = 2^2^ × 2^2^ and finally that 2^2^
        = 2 × 2. Putting this together we could calculate 2^16^ as
        (2^2^)^2^)^2^)^2^ and do only 4 multiplications. It doesn’t
        work out quite so well if the original number isn’t an even
        power of two, but it’s not terrible even then. The trick is to
        view 2^9^ as 2^4^× 2^4^ ×2. The general relationship is that
        a^n^ = a^n/2^ × a^n/2^ if n is even and a^n^ = a^n/2^ × a^n/2^ ×
        a if n is odd. Write a recursive function called `power` that
        raises a whole number to a whole power (e.g. power(2, 9) using
        this method.

3.  ### Persistent Life

    Modify a working game of life program (yours or mine:
    [life_v3.py](../03.3_CGoL_2_Persistence/life_v3.py)[^*]) so that it
    can store and retrieve states of the universe. It should be able to
    store in any of the three formats discussed in the notes. It should
    also be able to read files in all three formats and should
    autodetect which format the file is in, i.e. it shouldn’t need to
    ask the user.

    [^*] if you find there is too much code in the version linked to,
    version 3, you might find it helpful to look at the stepping stone
    on the way there:
    [life_v2.py](../03.3_CGoL_2_Persistence/life_v2.py).

## Logistics

-   Use the following naming scheme for your program files:,
    `a`*assignment#*`p`*problem#*`v`*version#*`.py` . So your first
    attempt at problem 1 on this assignment will be named `a3p1v1.py`
    and your second attempt (should there be one) will be named
    `a3p1v2.py` .
