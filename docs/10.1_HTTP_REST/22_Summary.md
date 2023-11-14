# Summary

The big picture:

-   We were able to produce an MVC CRUD controller that operated across
    HTTP by writing our own web server to handle the interactions with
    the client.

-   This meant translating the CRUD operations into their equivalent
    HTTP (REST) methods: POST, GET, PUT and DELETE.

-   HTTP design consists largely of mapping actions onto Method+URL
    pairs.

-   Because our server follows the principles of REST it will be a good
    web citizen, and lends itself to high performance by enabling
    caching at all points between and inside client and server.

-   Because we designed our earlier system using an MVC architecture:

    -   We were able to reuse `model.py` without any changes(!).

    -   Our changes to `quote.py` were localized and only added
        functionality without removing any existing functionality, or
        requiring us to rewrite any existing code.

    -   We did have to rewrite our controller, `object_server.py`, but
        we were able to retain its logic, just reimplementing it to deal
        with intermittent stateless HTTP interactions instead of
        continuous console interactions.

-   We ignored security issues, which would obviously not be reasonable
    for a production system!

Noteworthy details:

-   We built our web server by **subclassing** the server the Python
    Standard Library provides, a classic example of OOP enabling reuse.

-   It turns out the web is just built on computers throwing **strings**
    (plain old strings!) back and forth across a network.

-   Faced with **browser limitations** we had to choose between
    modifying the client (the browser via Ajax), or modifying our server
    (via tunneling) to handle PUT and DELETE requests. The web is still
    new enough that web progamming involves a lot of working around
    limitations.

-   **Tunneling** means to enclose one kind of message inside another
    (an envelope inside an envelope if you will). We tunneled the HTTP
    methods PUT and DELETE inside POSTs because current browsers don’t
    support them directly.

-   We made heavy use of **templates** to simplify the generation of the
    HTML responses. In an industrial-strength system we would probably
    store our templates as complete HTML files so they could be created
    by a graphic or interaction designer. We could then extract the
    portion of the entire page we require.

-   **HTTP application design** can benefit from:

    -   Explicitly identifying the **request-response cycles** it will
        enable.

    -   A graphic interaction **storyboard** showing the transitions
        between pages” in the application.

The final source code:

-   [object_server.py](object_server.py) The custom web server.

-   [model.py](model.py) The model, unchanged from before(!).

-   [quote.py](quote_3.py) Sample object class that knows how to
    display, and update itself through HTML.

-   [hockey_player.py](hockey_player.py) Sample object class that knows
    how to display, and update itself through HTML.

-   [HTML5_template.html](HTML5_template.html) Minimal, generic HTML5
    template. It looks like it’s just a %s, but do a view source, or
    save as, to see what’s really there.
