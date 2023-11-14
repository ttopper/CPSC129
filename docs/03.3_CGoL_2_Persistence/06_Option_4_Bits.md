# Option 4: Use only 1 bit per cell

There are numerous other options, but one that often occurs to students
is that since cells are either dead or alive their state could be stored
using single bit rather than an entire byte. This would reduce the
storage requirements by a factor of 8 in the first two options. But how
to convert our universe to a sequence of bits?

Here are the pieces you’ll need to assemble a solution:

First, the class constructor for `int`s allows the base of the input to
be specified, e.g.

    >>> int("111", base=2)
    7
    >>> int("10111001", base=2)
    185
    >>> u = "10111001"*100
    >>> u
    '10111001101110011011100110111001101110011011100110111001101110011011100110111001101110011011100110111001101110011011100110111001101110011011100110111001101110011011100110111001101110011011100110111001101110011011100110111001101110011011100110111001101110011011100110111001101110011011100110111001101110011011100110111001101110011011100110111001101110011011100110111001101110011011100110111001101110011011100110111001101110011011100110111001101110011011100110111001101110011011100110111001101110011011100110111001101110011011100110111001101110011011100110111001101110011011100110111001101110011011100110111001101110011011100110111001101110011011100110111001101110011011100110111001101110011011100110111001101110011011100110111001101110011011100110111001101110011011100110111001101110011011100110111001'
    >>> int(u,base=2)
    4837579098363815845901068946209539970477569763248796116365912530103321133318674247966529243769558995244870719450137841107801679631419931528891062234043935523637663342000363503198703854485041547352386384255447142614167797595816256230844381625L

So we could take our universe of numerical 1s and 0s, change them to
string 1s and 0s, and concatenate them all to get a very long string
representation of a binary number. We could then convert this binary
number to `int` thus compressing it:

    >>> len(u)
    800
    >>> len(str(int(u, base=2)))
    241

And then write that number to a file.

To load the universe from the file we read in the int value and convert
it to binary, and then to a list of binary values and then to a list of
lists of binary values. Hint:

    >>> bin(185)
    '0b10111001'
    >>> list(bin(185))
    ['0', 'b', '1', '0', '1', '1', '1', '0', '0', '1']
    >>> list(bin(185))[2:]
    ['1', '0', '1', '1', '1', '0', '0', '1']
    >>> 

It is indeed possible to do this helped along by [Python’s binary
operators](http://docs.python.org/reference/expressions.html#binary-bitwise-operations)
which allow us to manipulate the bits inside bytes, but these are not a
focus of the course so we will just nod at this possibility as we move
on by. (There are also fussy end conditions to deal with when the
universe is not a multiple of 8 in size because then our information
does not exactly fill bytes). Just know that you could use individual
bits to represent cells, but that doing so is fussy.
