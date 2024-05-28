# Persistence

So far each run of one of our programs has been independent from the
rest. Each began with a blank slate of memory working only with values
input during that run of the program, and all its results were lost when
the program ended.

This is typical of calculation type programs in which some one-time
value is calculated, but there are many other types of programs that
either work on existing data, or need to store their results. For
example most office applications work on long-lived documents. You may
use a word processor to open the existing copy of your resume, update it
and then save the new version. Game programs may wish to save the state
of a game so it can be resumed later, or to record and store a high
score.

What these situations require is the ability to move data out of RAM,
which is volatile, often reused after a program terminates and always
lost when a computer is turned off, to a longer lasting, stable storage
medium, i.e. to move the data from memory to disk. The technical term
for this is data persistence.

There are several choices for the persistence medium

-   Local text files
-   Local binary files
-   Local or remote database servers
-   Remote storage, e.g. across the internet

In this module we will consider the first two options.
