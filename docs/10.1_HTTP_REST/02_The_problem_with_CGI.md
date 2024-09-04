# The problem with CGI

Why not just keep using CGI?

-   **Ease of programming**. CGI is best suited to providing an
    interface to a program, and not so much to a site which might
    consist of a mix of static and dynamically generated resources. It
    can be done, but it’s awkward, and you’ll wish you hadn’t.

-   **Efficiency**. There’s a lot of overhead in running a CGI program.
    The web server has to load the Python interpreter (which varies in
    size, but can be several megabytes, call it 4MB), execute the
    program, gather the results, and transfer them back to the client
    for every request that comes in.

What could be better?

There are a lot of schemes that keep the Python (or other scripting
language) interpreter running instead of starting and stopping it, e.g.
FastCGI and SCGI, and others that embed it into the web server itself,
e.g. mod_python, mod_wsgi. But these are, finally, just halfway
measures. If the issue is to avoid having two large-footprint pieces of
software running why not just write a customized web server in Python so
that we have complete control _and_ good performance? Since Python will
be running the whole time, the cost of running a script reduces from
loading a 4+MB language interpreter to loading a (say) 2KB script.
Furthermore, the code will be streamlined compared to a complete server
because it will only contain code for things that it will actually do,
and not code for anything that anyone, anywhere might conceivably want
it to do (as a general purpose web server must provide).
