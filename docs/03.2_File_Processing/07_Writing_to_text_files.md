# Writing to text files

The mechanics of writing to text files are very straightforward. Suppose
we need to store a list of coordinates to a text file, e.g.

```python
coords = [[12, 31], [75, 19], [28, 51]]
```

Writing them to a file could be done by code like this,

```python
# write_coords.py
coords = [[12, 31], [75, 19], [28, 51]]
fname = input('Name of file to create? ')
f = open(fname, 'w')
for coord in coords:
    f.write(str(coord[0]) + ' ' + str(coord[1]) + '\n')
f.close()
```

The pattern is similar to reading from a file:

-   We open the file, but with a mode of `w` for **w**rite. Note the
    wording of the prompt `'Name of file to create? '` Opening a file
    for writing deletes an existing file of the same name if one exists!
    In production code it is critical to either know you can clobber
    existing files, or to check whether a file name has already been
    used, and then prompt the user for another name if existing files
    shouldn't be clobbered.
-   We direct output to the file using the file
    object's `write` method. This method wants a string argument so we
    need to format our coordinates accordingly (`f.write(coord[0]`))
    would throw an error). Note that we also have to add the newline
    character ourselves.
-   When we are done we close the file.

The resulting file looks like this if you open it in a text editor, e.g.
IDLE,

```plaintext
12 31
75 19
28 51
```