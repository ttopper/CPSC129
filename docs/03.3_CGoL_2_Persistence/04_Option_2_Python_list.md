# Option 2: Store the universe array using str(u)

You will notice when you write the code for reading in the universe in
this first format on the assignment that although it is not overly long,
it does involve some fussing and converting from string characters to
their matching numerical values in the universe array, i.e. 0 or 1. One
alternative is to take advantage of Python’s built-in machinery for
doing this.

Look at the transcript below carefully and note that Python is able to 
figure out the type of the value entered and translate the input string 
into an object of the necessary type.

    >>> x = input('Gimme a value: ')
    Gimme a value: 4
    >>> type(x)
    <type 'int'>
    >>> x = input('Gimme a value: ')
    Gimme a value: '4'
    >>> type(x)
    <type 'str'>
    >>> x = input('Gimme a value: ')
    Gimme a value: [1, 2, 3]
    >>> type(x)
    <type 'list'>
    >>> 

How could we leverage this ability to help us? We can store the string
representation for the universe to disk by calling the list class’
`str` method. Then when we read in the string we can trigger the
evaluation method ourselves by calling the built-in `eval` function.

Here’s a little test program demonstrating this approach,

``` python
u = [ 
     [0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0],
     [0, 0, 0, 1, 0],
     [0, 1, 1, 1, 0],
     [0, 0, 0, 0, 0],
    ]

fname = input('Name of file to store universe in: ')
outfile = open(fname, 'w')
outfile.write(str(u))
outfile.close()

infile = open(fname, 'r')
input_line = infile.read()
u = eval(input_line)

print(u)
print(type(u))
```

which produces this as output when it is run,

    Name of file to store universe in: list.txt
    [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]]
    <type 'list'>

## Evaluation

How is this format?

As you can see the code is very brief. It is easy to write if one is
used to using `str` and `eval`, though hard to think of if one is not.

How about the size of the representation on disk? For each cell in the
universe it stores roughly three Bytes to disk, one for the cell and one
each for the comma and space separating it from the next cell. (I say
roughly because the last cell in each row does not have a trailing space
and comma). In addition it stores four characters to separate rows:
[], . Finally it uses two characters to delimit the entire list: [].
So for an r × c universe it uses r × (c-1) × 3 + r + 4 × (r-1) + 2 + 2
Bytes = (3c-2) × r Bytes. To make this more concrete lets again consider
a couple of specific universe sizes:

| Universe size | Storage Space   |
|---------------|-----------------|
| 25 x 80       | 5,950 Bytes     |
| 1000 x 1000   | 2,998,000 Bytes |
