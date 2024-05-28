# Pickling

Recall this bit of code from writing coordinates to a file,

```python
for coord in coords:
    f.write(str(coord[0])+' '+str(coord[1])+'\n')
```

It's straightforward enough, but it feels like busywork converting
numbers to strings and bundling the strings together into lines. In fact
it feels like such straightforward busywork that our intuitions suggest
it could be automated, and in fact Python provides a module that
automatically converts its built-in types to strings that can be stored
in text files. The module is whimsically called `pickle` (because
it _preserves_ the objects the way pickling preserves foods). Its use is
straightforward:

```python
# life.py
universe = [ [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 1, 1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]
           ]
import pickle
f = open( 'pickled_universe.txt', 'wb') # we use wb to indicate we are writing bytes
pickle.dump(universe, f)
f.close()
f = open('pickled_universe.txt', 'rb') # we use rb to indicate we are reading bytes
u = pickle.load(f)
f.close()
print(u)
```

Output:

```plaintext
>>> 
[[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
>>> 
```

Almost any Python object can be pickled (among the exceptions are odd
ducks like sockets for network connections and file handles). Given how
compact it is why would we not just always use it? The answer is that
we _will_ often use it, but not without thinking first. One reason we
will sometimes avoid it is that the pickled representation is neither
particularly compact nor particularly
readable. `pickled_universe.txt` above looks like this,

```plaintext
(lp0
(lp1
I0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aa(lp2
I0
aI0
aI0
aI0
aI0
aI0
aI0
aI0
aa(lp3
I0
aI0
aI0
aI1
...
```

and is 383 bytes in size. That makes it 2 to 3 times as large as our
hand-rolled solutions in Options 1 and 2.

A more subtle reason is that it can be inefficient for some data types.
One common situation is to want to store a dictionary of objects to
disk. The dictionary can be pickled, but then to access any individual
element of the dictionary the _entire_ dictionary must be read into
memory and unpickled before the element can be accessed. If the
dictionary is large this can represent a significant amount of
processing time and memory. Because this use case is so common Python
provides the `shelve` module in its standard library. A `shelve` is like
a dictionary that is stored on disk.