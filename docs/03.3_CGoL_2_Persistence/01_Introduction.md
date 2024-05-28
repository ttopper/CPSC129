# Designing file formats

So if you’ve got some data you want to store between runs of a program
(or a set of programs), you need to write it to disk somewhere. To get
it back you need to read it from disk and that means knowing what format
it is in, i.e. knowing how it was written to disk. Often you are adding
a program to a suite of existing software and the file formats have
already been determined. Sometimes though you are in at the beginning of 
a project and get to decide how to write the data to disk. In this case
your task is to design a file format, i.e. to decide how the relevant
information should be written to disk. Generally we’d like a way that
is easy to code, both for reading and writing, and that is compact and
thus efficient in its use of disk space. Perhaps surprisingly quite
different approaches can usually be taken to storing data on disk. One
accessible problem that affords different alternatives is the problem of
storing the state of the universe in Conway’s Game of Life so in this
unit we’ll consider alternative ways of storing and restoring a Life
universe to and from disk.
