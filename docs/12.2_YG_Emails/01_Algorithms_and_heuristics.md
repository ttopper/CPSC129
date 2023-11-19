# Algorithms and Heuristics

This course and its predecessor CPSC 128 have focussed exclusively on
solving problems using algorithms. An algorithm is a _mechanical_
procedure that is guaranteed to find the _correct_ solution in a
_finite_ amount of time. The word _mechanical_ indicates that it
doesn’t rely on magic, or luck, or involve human judgment or intuition;
_correct_ means that it always works; and _finite_ that we won’t have
to wait forever to get that answer. Those are all desirable properties
of a solution methodology, but sometimes they may be overriden by other
considerations. For example we may need a solution **now** (after all
finite just guarantees us that an algorithm won’t take forever, but it
could take years, or for that matter millenia, and still qualify as an
algorithm), and be willing to accept an inexact one as long as it is
close to the correct one. It might also be that no perfect solution is
even possible, i.e. that the solution is not computable, for example
because there is insufficient information. In these cases we may turn to
heuristics instead of algorithms. Heuristics are solution techniques
that give us reasonable answers quickly.

A well-known investing heuristic is that you can find the number of
years it will take an investment to double in value by dividing the
interest rate into 72. For example money invested at 6% will double in
(approximately) 72/6=12 years. (This is an example of an approximation
heuristic.)

Email virus scanners use heuristics to flag spam by relying on the
presence of certain words to classify messages. The presence of the word
viagra” does not guarantee that the message is spam, but unless you
are a medical researcher it is likely. (This is an example where no
perfect mechanical solution is possible.)

This week’s problem will give you the chance to come up with some
heuristics to help with an intractable problem.
