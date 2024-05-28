# A bigger Gotcha: Shelves update on assignment not mutation

> **WTH!?**"_Shelves update on assignment not mutation._"

Shelves are mostly very easy to use, but there is one common gotcha to 
be aware of when you use them and that is that <q>shelves update on 
assignment not mutation</q>. There have I said it enough times? Now I'll 
explain it.

## The problem: Surprise!

Consider the following transcript carefully,

```plaintext
>>> s = shelve.open('test_shelve')
>>> s['bob'] = 42
>>> s['liz']=[31]
>>> s.close()
>>> s = shelve.open('test_shelve')
>>> for key in s:
print(key, ':', s[key])

bob : 42
liz : [31]
>>> s['bob'] = 43
>>> s['liz'][0] = 30
>>> s.close()
>>> s = shelve.open('test_shelve')
>>> for key in s:
print(key, ':', s[key])

bob : 43
liz : [31]
```

The thing to notice here is that `s['bob']` was changed (from 
`42` to `43`), but that `s['liz']` was **not** (it's still just `[31]`). 
**WTH?** The reason is that `s['bob']` was _assigned to_, but `s['liz']` 
was only _mutated_, that is the contents of the list `s['liz']` were 
changed, but `s['liz']` itself still refers to the same list object. 
That object's contents may have changed but Python has no (easy and 
efficient) way of noticing that. So `s['bob']` was assigned to and 
therefore updated but `s['liz']` was only mutated and so was not 
updated, just like the phrase says: "Shelves update on assignment not 
mutation".

How can we force `s['liz']` to be updated?

## Solution 1

Open the shelve with the option `writeback=True`,

```plaintext
>>> s = shelve.open('test_shelve', writeback=True)
>>> s['liz'][0] = 1
>>> s.close()
>>> s = shelve.open('test_shelve')
>>> for key in s:
print(key, ':', s[key])

bob : 43
liz : [1]
```

_But_ listen to the official documentation:

> If the optional writeback parameter is set to True, all entries 
accessed are cached in memory, and written back at close time; this can 
make it handier to mutate mutable entries in the persistent dictionary, 
but, if many entries are accessed, **it can consume vast amounts of 
memory** for the cache, and it can make the close operation **very 
slow** since all accessed entries are written back (there is no way to 
determine which accessed entries are mutable, nor which ones were 
actually mutated). [*](http://docs.python.org/lib/module-shelve.html)

## Solution 2

Mutate the object via a temporary name assigned to it and then reassign 
the temporary name to the shelve (i.e. keyed) name. In other words use a 
temporary name to force an assignment to the keyed name happen:

```plaintext
>>> s = shelve.open('test_shelve')
>>> tmp = s['liz']
>>> tmp[0] = 2
>>> s['liz'] = tmp
>>> s.close()
>>> s = shelve.open('test_shelve')
>>> for key in s:
print(key, ':', s[key])

bob : 43
liz : [2]
```

<br>

## Summary

**Fact**: _Shelves update on assignment, not mutation_.

**Implication**: This means that changes to shelve members that contain
mutable types, e.g. lists and dictionaries, are not automatically
updated to disk.

**Solution 1**: Open the shelve with the option `writeback` set
to `True`.

**Drawback**: If the shelve is open for long a large number of cached
shelve objects will accumulate and need to be written to the shelve file
when it is closed.

**Solution 2**: Mutate the shelve object via a temporary name assigned
to it and then reassign the temporary name to the shelve (i.e. keyed)
name.

**Drawback**: It takes some care to do this consistently.

**Conclusion: Use Solution 2.**