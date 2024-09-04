# Potential Problems

As mentioned in the introduction to this module the challenges in data
processing are usually posed by the data rather than the processing
algorithms.

For example you will have to deal with the possibility that you cannot
read one of the files. This could happen if you do not have permissions
to read the file, if the file does not exist, etc. How could one of the
files not exist? It could be because it actually doesn’t exist (perhaps
the volunteer forgot to copy it onto the flashdrive being used), or
perhaps it appears to your program not to exist because they typed its
name in incorrectly. At any rate you need to, at best, help them out,
and, at least, fail gracefully with an explanation.

Similarly you’ll have to ensure that the files are properly formatted,
for example that each record in the contestant file does contain the
number fields you expect it to, not more, and not less. Let’s say you
opt to split a line to get the field values, e.g. running

    (number, last_name, first_name) = line.split(',')

will produce an error if the value of `line` is `"Topper,Tim"`,

    >>> (number, first_name, last_name) = 'Topper,Tim'.split(',')

    Traceback (most recent call last):
      File "<pyshell#0>", line 1, in <module>
        (number, last_name, first_name) = line.split(',')
    ValueError: not enough values to unpack (expected 3, got 2)
    >>> 

But a naive” user should not be confronted with a Python error
message.

There are two programming approaches to dealing with potential error
situations. One is anticipatory, the other is reactive.

-   In the **anticipatory approach** you check that there is an object with
    the name you were given, that it is a file (not a directory, or
    link, etc.), that you have permisson to open it and so on.

-   In the **reactive approach** you try to open it and then deal with an
    error if one results by catching exceptions”.

Which approach should be preferred is a subject of active debate in the
programming community[^*], but one approach often dominates the other in
particular languages. The anticipatory approach is prevalent in the C
community, while the reactive approach is more common in the Python
community. See the next page, [Python
Exceptions](05_Python_exceptions.md), for the syntactical details
about working with Python’s exceptions.

------------------------------------------------------------------------

[^*] A readable entry to the debate is Joel Spolsky’ spiece titled simply
[Exceptions](http://www.joelonsoftware.com/items/2003/10/13.html).
Searching for [reactions to the
piece](http://www.google.ca/search?q=%22joel+spolsky%22+exceptions) will
lead you to the other side of the debate.
