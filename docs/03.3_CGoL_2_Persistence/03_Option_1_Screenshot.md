# Option 1: Store a screenshot of the universe

One approach would be to “take a snapshot” of the universe and store
that screenshot to disk. In other words we’d like the disk file to be a
picture of the universe. If the universe looks like this onscreen,

    - - - - -
    - - @ - -
    - - - @ -
    - @ @ @ -
    - - - - -

We’d like to store this in the file,

    - - - - - \n- - @ - - \n- - - @ - \n- @ @ @ - \n- - - - - \nEOF

We can do that by copying our original display code and modifying it to
open a file and then use `write` instead of `print`.

One nice thing about this representation is that it could be opened in a
text editor and modified to create new starting configurations for the
universe. It’s always nice if your file format plays well with the
other tools you are using.

The resulting code to write the universe to disk in this format looks
much like the code to display it onscreen, but has to open the file and
then use `write` instead of `print` for output.

``` python
fname = input('Name of file to store universe in: ')
outfile = open(fname, 'w')
for row in range(U_ROWS):
    for col in range(U_COLS):
        if u[row][col] == 1:
            outfile.write(LIVE_CELL+' ')
        elif u[row][col] == 0:
            outfile.write(DEAD_CELL+' ')
    outfile.write('\n')
outfile.close()
```

## Evaluation

How is this format?

It is easy to write the code to write it to disk.

You will have to evaluate how easy it is to write code to read it from
disk once you have completed the assignment.

How about the size of the representation on disk? For each cell in the
universe, it stores two Bytes to disk, one for the cell and one for the
space separating it from the next cell. In addition, it stores a newline
character to mark the end of each row. So for an r × c universe it uses
(r × c × 2) + r Bytes. To make this more concrete lets consider a couple
of specific universe sizes:

| Universe size | Storage Space   |
|---------------|-----------------|
| 25 x 80       | 4,025 Bytes     |
| 1000 x 1000   | 2,001,000 Bytes |


We could cut the storage almost in half just by dropping the spaces we
store to disk. Does this make it easier to harder to read the file in
from disk? If it makes it harder, is it worth it?
