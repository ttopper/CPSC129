# Examinable Topics

I’ll leave this here because it serves as a useful list of topics, but
focus your studying on the [Exam Study Guide](02_Exam_study_guide.md).

Items that are crossed out were covered in the course, but will not be examined.

#### Algorithmics: How? When?

-   **Searching**: exhaustive, linear, binary (with and without
    recursion), interpolation. _Be able to write the first three. Know
    the performance of all._
-   **Sorting**: straight insertion, selection and exchange (bubble);
    Shell sort, quicksort (with and without recursion), heapsort. _Be
    able to write the first three, read and modify the second three.
    Know the performance of all six._
-   **Recursion**. _Be able to step through, and convert to and from
    recursive solutions._
-   **Median**. *Remember and be able to adapt the two approaches.*
-   **~~Indexing~~**~~. Persistent indexes~~.
-   **Breadth-first tree search**, e.g. pitcher problem. *Remember the
    approach.*
-   **Binary trick** to get all subsets. _Be able to discuss, read and
    modify (but not write from scratch)._

#### Data structures

-   Processing **arrays**, e.g. Game of life, Mazes.
-   **Complex representations**: e.g. maze with _shared_ walls.
-   **Binary trees** in a list, e.g. heap; ischild(), parent(),
    ancestor().

#### Design patterns, tools, and issues

-   **~~Persistence~~**~~: designing text file formats (see CGoL
    alternatives: screenshot, list of live ones). Binary file formats,
    e.g. bitmap for CGoL, pickling and shelves. Analyzing space
    requirements of file formats, e.g. as we did for the text formats in
    CGoL.~~
-   **Theoretical algorithm analysis**. Big O notation. Be able to do
    the assignment problems.
-   **~~Empirical algorithm analysis~~**~~: Plot your timing data vs the
    hypothesized order, a straight line means your hypothesis is
    correct.~~
-   **~~Event driven programming~~**~~, e.g. our text and visual
    controllers for the object server~~.
-   T~~ext **controllers** vs visual (for us, HTML) controllers~~.
-   Object **serialization**. (Just know what the term means).
-   ~~**TDD**: Test driven development.~~
-   **MVC**: Model-view-controller. Know the diagram.
-   **CRUDS**: Create-retrieve-update-delete-search.
-   Approach: **Design _from_ the desired interface _to_ the code**.
-   **OO modelling**, e.g. as we did for pitchers.
-   **Testing** for correctness (unit testing). Performance testing.
    Testing frameworks.
-   **UIDs**: Hashing (SHA, md5, Python’s hash())
-   **Efficiency strategies**: Avoid unnecessary work; Remember
    previously computed values (cache).
-   ~~Symbolic **debuggers**.~~
-   ~~**UML.** You should remember what we saw in CPSC 128.~~

#### Major problem domains that might be referred to

-   CGoL: Conway’s game of life
-   Bitmapped graphics, e.g. bouncing ball.
-   Mazes
-   Text files
-   Object server (originally quote server)
-   ~~CGI programming. HTML forms for input. Parsing the query~~.
-   String processing, e.g. early anagram-like problem using people’s
    names.
-   ~~Pitcher problems~~

#### Language specific issues

-   the subtleties of reference semantics; copy.deepcopy()
-   list comprehensions
-   list splitting and slicing, e.g. as done in median-by-partition.
-   hash()
-   pickling and shelves (which update on assignment not mutation).
-   try...except...
