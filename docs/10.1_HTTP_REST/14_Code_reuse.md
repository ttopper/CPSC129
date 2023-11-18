# Code reuse

OK now what do we have to work with to make this happen? Our earlier MVC
controller obviously. What parts of it can we,

-   reuse without modification?
-   modify for reuse?
-   replace with new code?

Recall that our earlier application consisted of:

-   MVC_model.py
-   MVC_controller.py
-   quote.py

We had better be able to reuse the **model** (MVC_model.py) as-is, or it
will be evidence that we missed the boat on the separation of
responsibilities between M, V and C.

Equally straightforward, the **controller** has to be reimplemented
although much of its internal logic will survive intact since the logic
of the operations is unchanged. For example updating required us to get
the updated values, create a new object, save it, and delete the old
object. The steps remain the same, but since our application now
interacts with the user through a browser communicating across an HTTP
connection, it’s no surprise that little of our console-based code can
be reused.

Not as obvious is what to do about `quote.py`. Much of it remains
relevant since we are still dealing with the same types of objects. On
the other hand we we will now need HTML representations of the objects,
and our current `quote.py` doesn’t provide that. So our scorecard looks
like this:

| MVC_model.py      | &rarr; | Reuse without modification (we hope). |
|-------------------|--------|---------------------------------------|
| MVC_controller.py | &rarr; | Replace with new HTTP server.         |
| quote.py          | &rarr; | Modify by adding methods.             |

