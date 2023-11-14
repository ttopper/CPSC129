# The goal

If we are running the game of life and an interesting configuration
appears on screen we’d like to be able to store it to disk. Later we’d
like to be able to restore it from disk and use it to initialize the
universe. A run of our program might look like this,

    ================================
    Welcome to Conway's Game of Life
    --------------------------------

    Initialize (r) randomly or (f) from file? r
    Number of rows in universe? 8
    Number of columns in universe? 8
    Initial percentage of live cells? 42
    @ @ - @ @ @ @ @
    - @ @ @ - - - -
    - - - - @ - @ @
    @ @ - @ @ @ @ @
    @ @ - - @ @ - @
    @ @ - - @ @ @ -
    - @ - @ @ - @ -
    - @ - - - @ @ -

    Options:
        a : Age universe one generation
        m : Age universe multiple generations
        s : Save universe to disk
        l : Load universe from disk
        q : Quit program

    Command (a|m|s|l|q): a
    - - - - - - - -
    - @ - - - - - -
    - - - - - - - -
    - @ @ @ - - - -
    - - - - - - - -
    - - - - - - - -
    - @ - @ - - - -
    - - - - - - - -

    Options:
        a : Age universe one generation
        m : Age universe multiple generations
        s : Save universe to disk
        l : Load universe from disk
        q : Quit program

    Command (a|m|s|l|q): l
    Name of file to load from? test.lif
    - - - - - - - -
    - - - - - - - -
    - - @ @ @ - - -
    - - @ @ @ - - -
    - - @ - @ @ - -
    - - - - @ - - -
    - - - - - @ - -
    - - - - - - - -

    Options:
        a : Age universe one generation
        m : Age universe multiple generations
        s : Save universe to disk
        l : Load universe from disk
        q : Quit program

    Command (a|m|s|l|q): m
    How many generations? 2
    - - - - - - - -
    - - - @ - - - -
    - - @ - @ - - -
    - @ - - - - - -
    - - @ - - @ - -
    - - - @ @ - - -
    - - - - - - - -
    - - - - - - - -

    - - - - - - - -
    - - - @ - - - -
    - - @ @ - - - -
    - @ @ @ - - - -
    - - @ @ @ - - -
    - - - @ @ - - -
    - - - - - - - -
    - - - - - - - -

    Options:
        a : Age universe one generation
        m : Age universe multiple generations
        s : Save universe to disk
        l : Load universe from disk
        q : Quit program

    Command (a|m|s|l|q): s
    Name of file to save to? test2.lif
    Options:
        a : Age universe one generation
        m : Age universe multiple generations
        s : Save universe to disk
        l : Load universe from disk
        q : Quit program

    Command (a|m|s|l|q): q
    >>> 
