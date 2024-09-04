# The inner nature of HTTP

We are most used to console-like interactions where a user has an
extended conversation with a program. HTTP is different from this in
some important ways. The differences were designed into HTTP to make it
scalable. They are key to the fact that it became the **world-wide** web
instead of the me-and-my-buddy-here’s very local web (if you are old
enough you might know those as BBS systems).

-   The first is that HTTP is **connectionless**, unlike a console
    interaction which is one long continuous connection of user to
    program. After the client (browser) makes a request it disconnects
    from the server and waits for the server’s response. If the
    connection has been broken how can the server send the information
    back? Because the client gave it it’s return address. In this way
    the difference between connection and connectionless is a bit like
    the difference between a phone call and using old-fashioned postal
    mail. In a phone call you establish a connection and wait on the
    line (holding the line open) while the person on the other end finds
    the answer to your question. Using postal mail you mail a letter
    with your return address on it, and then do other things while you
    wait for the response to come back by return mail. A console
    interaction is like a phone conversation; HTTP is like postal mail.
    Why do this? Because for a server to keep thousands of connections
    open while it processes requests would waste bandwidth.

-   HTTP is also **stateless**. The server has no memory. Using the mail
    metaphor it doesn’t file any old correspondence. It processes the
    request, and on completion throws its details away. Why do this?
    Because it would take both storage and time (our two computaitinal
    resources, remember?) for the server to retrieve old correspondence
    each time it has to handle a request. Instead the client is supposed
    to include all necessary information in each request. This way the
    server can handle it, and then forget all about it.

-   The final characteristic is that HTTP is **media independent**. Most
    people think of it as providing HTML pages and some rich media to
    place on those pages, but in fact HTML can serve any type of
    content. The server and client discuss what format would be best and
    the server provides the content in that form. The discussion is
    simple. The client sends a list of types it can handle in order of
    preference. The server consults a list of formats in which it can
    provide the resource and picks the one most favoured by the client.
    The MIME specification describes how this content negotiation takes
    place. [Many media
    types](https://www.w3-tools.com/mime_types_list.html) are
    registered.

These qualities enable HTTP to support several interrelated technologies
that lead to the web’s remarkable scalability (and it truly is a modern
engineering triumph):

-   Caching. The web is heavily cached. Ideally most requests never have
    to reach the server to be served, but instead can be handled by a
    cache somewhere along the way, perhaps in the client machine itself,
    or in a caching proxy along the way, or a cache on the server (so it
    doesn’t have to recompute an expensive resource).

-   Last-modified checking. The system doesn’t know if it can trust a
    value from a cache unless it knows it hasn’t been modified since
    going into the cache. Last-modified checking enables this.

-   ETag checking. ETags are hashes (UIDs!) sent by the server that
    enable a client to determine if its copy of a resource is still up
    to date.
