# Reading numeric data

In the examples so far we have read string data, but what if we wanted
to read numerical data, e.g. to read our coordinates back in and
reconstitute the list `coords`?

Pseudocode,

```plaintext
Open the file
Initialize coords to an empty list
Read it a line at a time
    Split the line into parts at blanks
    Convert each part into an integer value
    Append the integer values to the list coords
```

In Python,

```python
# read_coords.py
coords = []
fname = input('Name of file to read from? ')
f = open(fname, 'r')
for line in f:
    (x_string, y_string) = line.split()
    coords.append([int(x_string),int(y_string)])
f.close()
print('coords =', coords)
```

A sample run:

```plaintext
>>> 
Name of file to read from? test.dat
coords = [[12, 31], [75, 19], [28, 51]]
>>> 
```