# Introduction

The goal of algorithm analysis is to understand the performance of a
particular algorithm. If you think back to the very beginning of CPSC
128 you may recall that the best algorithm is the one that makes most
efficient use of the computational resources at hand, and that those
computational resources are processor time and storage space. Algorithm
analysis tries to characterize the performance of a particular algorithm
in terms of its usage of those two resources. Furthermore it aims to
describe not just the typical performance, but also to establish the
best-case and worst-case performances.

That performance can be estimated through

-   theoretical analyses, i.e. calculations based on the source code,

or,

-   empirical evidence of actual timings of program execution.

Each method has strengths and weaknesses. Theoretical analysis is more
prone to human error in performing the analysis, whereas the empirical
approach produces reproducible numbers for the run time and memory
utilization. On the other hand the theoretical analysis often leads to a
more general description of the behaviour than we can arrive at through
timings because the timings can depend on the particular data used in
the run. We will make use of both approaches during this course.
