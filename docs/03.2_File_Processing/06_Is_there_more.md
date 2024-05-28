# Is there more?

Of course there is: you can tell where you are in a text file by using
its `tell` method, i.e. `f.tell()`, you can seek to a particular
location in a file using `f.seek(`*`offset`*`)`, tell if a file is open
by checking its `closed` attribute. There is always more...but this is
enough for now[^*].

------------------------------------------------------------------------

[^*]: If it is not enough for you, you can [read more
online](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) or
explore via the Python Shell, e.g.

```plaintext
>>> dir(f)
['__class__', '__delattr__', '__doc__', '__enter__', '__exit__', '__format__', 
'__getattribute__', '__hash__', '__init__', '__iter__', '__new__', '__reduce__', 
'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', 
'__subclasshook__', 'close', 'closed', 'encoding', 'errors', 'fileno', 
'flush', 'isatty', 'mode', 'name', 'newlines', 'next', 'read', 'readinto', 
'readline', 'readlines', 'seek', 'softspace', 'tell', 'truncate', 'write', 
'writelines', 'xreadlines']
>>> 
```