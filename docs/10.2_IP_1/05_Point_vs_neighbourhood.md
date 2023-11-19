# Point vs Neighbourhood Processes

Darkening the penguin image was an example of a _point operation_. Point
operations depend only a single pixel value and affect only that same
pixel’s value. That means that point operations can process each pixel individually
without worrying about their neighbours. (It also makes them ideal
candidates for parallelization if have a computer with thousands of
processors).

In contrast many image processing operations work on _neighbourhoods_ of
pixels. Edge detection is an example of this.

 

