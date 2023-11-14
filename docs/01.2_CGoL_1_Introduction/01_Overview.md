# Algorithm Development Case Study: Life 1: Conway’s Game of Life (aka CGoL)

First up this semester is a simulation of Conway’s Game of Life (CGoL).
It will remind us how to work with lists of lists, a very common data
structure, and give us a base for algorithm refinements in the coming
weeks.

-   [Introduction [16:35]](02_Introduction.mp4) Overview of the
    “game”. The rules. Stepping through the game using an applet.
    Reasons to study CGoL.

-   [Algorithm Overview [7:32]](03_Algorithm_overview.mp4) Look over
    the Wikipedia page’s section on algorithms for simulating CGoL.
    Preview of enhancements to the basic algorithm: Identify unchanging
    areas; toroidal universes; representing the universe by a list of
    locations of live cells; and the suggestion that even more
    sophisticated data structures are possible.

-   [Pseudocode [4:09]](04_Pseudocode.mp4) Saying what we need to do
    in English and gradually refining this description from this,

        Create the universe
        Initialize the universe
        Forever:
            Display the universe 
            Age the universe

    to this,

        Create the universe
        Initialize the universe

        Forever:
            Display the universe
            
            Age the universe:
            Consider every cell in the universe
            Counts its live neighbours
            Based on its current state and its number of live neighbours
                Decide if it lives, dies, or is born
                Record the result in next universe
                
            Replace universe with next universe

-   [Create and Initialize the Universe
    [11:59]](05_Create_and_initialize_U.mp4) Turn the pseudocode into
    Python comments and then begin translating them into Python line by
    line. I hope this is a useful presentation of methodical
    programming.

-   [Display the Universe [6:56]](06_Display.mp4) As above, but in
    addition mistakes are made! And then corrected. Which is to say,
    typical programming.

-   [Age the Universe [21:35]](07_Age.mp4) Accessing the eight
    neighbours with a pair of loops. There is an extended debugging of
    one error, hopfully useful as a model of how I go about it. You will
    also see, if you haven’t already noticed, that I read and reread my
    code numerous times as I write it trying first to make it clear, and
    then to keep it clear in my head. (Errata: There are a couple of
    verbal slips where I say “live” instead of “dead” about cells
    around the 16:20 mark. Hopefully they do not lead to confusion.)

-   [life_v0.py.png](life_v0.py.png) The code developed so far (as an
    image, so you’ll need to type it in). This is the starting point
    for Assignment 1.

