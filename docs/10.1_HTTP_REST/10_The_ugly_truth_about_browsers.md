# The ugly truth about browsers

Sadly (no, more than that, frustratingly, maddeningly, infuriatingly) we
cannot use a browser to test `object_server.py` because current browsers
only support the GET and POST methods. Change is coming, e.g. HTML5
forms will support all four methods, but at the moment everyone is
forced to work around this painful browser limitation.

There are several common work arounds:

1.  We could **write our own client** instead of using a browser. But
    this means more code to write, and then we’d have to distribute our
    client to our users, and people don’t want another client, they
    have browsers and want to keep using them. Note however that this is
    a common solution in vertical applications, e.g. library access to
    commercial databases, and in commercial applications generally where
    we can provide a custom client to our customers, e.g. iTunes.

2.  **Modify our client to use Ajax** to issue the calls. The browsers
    don’t directly support PUT and DELETE, but they do all now support
    [the XMLHttpRequest
    object](http://www.w3schools.com/ajax/ajax_xmlhttprequest.asp). This
    enables programmers to use Javascript to issue PUT and DELETE
    requests and is my preferred solution in my own apps. I originally
    began these notes using this approach, but there was too much to
    explain about Javascript, and JSON or XML, and on and on.

3.  **Modify our server so we can tunnel through POST** for UPDATE and
    DELETE. This is probably the most common strategy and suits us since
    we don’t have to add another language (Javascript), but
    unfortunately we do have to ugly up our HTML a bit.
