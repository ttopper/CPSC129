# Shelves

A `shelve` ([Official documentation](http://docs.python.org/library/shelve.html)) 
is like a dictionary that is stored on disk. (The name continues the 
canning theme begun with `pickle`). The dictionary values can be any 
object that can be pickled. Retrieval is fast because the dictionary 
keys are hashed for fast retrieval.

Here is an example that stores quotations into a `shelve` on disk. The 
comments should make it self-explanatory.

```python
# shelve_test.py
import shelve
# First here are a couple of quotes to work with.
b = ['Kent Beck', 'Optimism is an occupational hazard of programming: testing is the treatment.']
k = ['Brian Kernighan', 'Controlling complexity is the essence of computer programming.']
# Now let's create an in-RAM dictionary with the quotes in it.
quotes = {}
# Add the quotes to the dictionary keyed by last name.
quotes['Kernighan'] = k
quotes['Beck'] = b
# Now let's display what we have:
print('Here\'s the dictionary:')
print(quotes)
print()
print('Here it is again by looping through it:')
for person in quotes.keys():
    print(quotes[person])
print()
# Now let's create a shelve and put the quotes in it.
# Like a file we open it, but unlike with a file
# opening a shelve is non-destructive so you can reopen it as often
# as you want.
quotefile = shelve.open('quotes')
# Notice how the access syntax mirrors the dictionary syntax above.
quotefile['Kernighan'] = k
quotefile['Beck'] = b
quotefile.close()
# The quotes should be stored on-disk now.
# Let's reopen the shelve and display the quotes.
quotefile = shelve.open('quotes')
print('Here\'s the content of the shelve:')
# Notice how similar this is to working with the in-memory dictionary above.
for key in quotefile:
    print(key, ':', quotefile[key])
quotefile.close()
```

The example shows how to store and retrieve data with the shelve, but 
what about deleting a stored item? Just use `del dictionary[key]` or in 
the specific example above we could use `del quotefile['Beck']` to 
remove the Kent Beck quote.

## A small gotcha

Brian Kernighan is a very smart guy and has said many memorable things. 
What if we add a second quote by him to the shelve? Well if we use the 
same key, i.e. his last name `Kernighan`, it will replace the existing 
quote. What to do? One view is that last name was not a good choice for 
the key because it is not unique to the items being stored, i.e. two 
items can have the same key. Another is that it is a fine key, but the 
values in the dictionary should be a list of the quotes by Brian 
Kernighan not a single list element giving one quote, i.e. the entry 
should be a list of lists. In either case we probably want to be able to 
tell if we already have any quotes by him already and we can do that 
using the shelve's `in` method,

```python
if 'Kernighan' in quotefile:
   # deal with it...
```


