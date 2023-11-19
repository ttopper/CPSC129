# Assignment 11

## Problems

1.  In the notes we developed a working Pitcher Problem” solver
    [pitcher_new_2_succint.py](../11.1_Pitcher_Problems/pitcher_new_2_succint.py).
    There is a hitch though. Its output does not in fact tell us _how_
    to solve the problem, only that it _can_ be solved. Modify the code
    developed in the notes so that it outputs instructions on how to
    solve the problem (if it can be), e.g.

         
        Fill the 7 litre pitcher.
        Pour from the 7 litre pitcher into the 3 litre pitcher.
        Empty the 3 litre pitcher.
        Pour from the 7 litre pitcher into the 3 litre pitcher.
        There will be 1 litre in the 7 litre pitcher.

    Hint: The easiest way that has occurred to me of doing this is to
    modify the state variable so that it includes a list of instructions
    on how the state was reached, i.e.
    `start = [ [Pitcher(7,0),Pitcher(3,0], [] ]` And that empty list
    following the list of Pitchers will contain a list of string
    instructions on how to reach the state. After each fill, pour or
    empty action add a new string to that list saying what you just did
    so that when you discover a state is a solution you’ll it will
    contain the list of instructions on how it was reached.

2.  Write a function called `summarize` that is passed the name of a
    file whose lines contain data formatted like this,

        continent:country:population:area

    and returns a string containing a report formatting the data
    **exactly** like this,

        CONTINENT       COUNTRY    POPULATION       AREA       POP. DEN.
                                  (,000,000s)   (,000s MI^2)  (POP./MI^2)

        Asia            China         1032          3705         278.5
                        India          746          1267         588.8
                        Japan          120           144         833.3
                        USSR           275          8649          31.8
                                      ----         -----
                        Total         2173         13765

        Europe          England         56            94         595.7
                        France          55           211         260.7
                        Germany         61            96         635.4
                                      ----         -----
                        Total          172           401

        North America   Canada          25          3852           6.5
                        Mexico          78           762         102.4
                        USA            237          3615          65.6
                                      ----         -----
                        Total          340          8229

        South America   Brasil         134          3286          40.8
                                      ----         -----
                        Total          134          3286

    Now it’s hard to compare your output with the model output above
    (that requires detailed data processing after all!) so the file
    [a11p2_tester.py](a11p2_tester.py) contains a program to test your
    function for you.

    Tip:

    -   Remember not to trust your data source!

    -   To achieve neat columns you will want to use format strings
        specifying the field widths.

## Logistics

-   Use the following naming scheme for your program files:,
    `a`*assignment#*`p`*problem#*`v`*version#*`.py` .
