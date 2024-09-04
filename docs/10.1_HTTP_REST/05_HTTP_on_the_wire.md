# HTTP on the wire”

The HTTP protocol is a very simple one, a key to its widespread
implementation and thus its eventual success. A request consists of a
sequence of lines of text. The first one specifies the HTTP method
(verb), the resource (by its URL, or, rarely, its URI) being requested
and the HTTP protocol version, e.g.

    GET /index.html HTTP/1.0

There are four key HTTP
methods<sup>[^*](https://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html)[^**](https://www.rfc-editor.org/rfc/rfc9110.html#name-methods)</sup>,
([all of them](http://en.wikipedia.org/wiki/Http#Request_methods))

GET
:   “The GET method means retrieve whatever information ... is
    identified by the Request-URI. If the Request-URI refers to a
    data-producing process, it is the produced data which shall be
    returned as the entity in the response...”

PUT
:   “The PUT method requests that the enclosed entity be stored under
    the supplied Request-URI.”

POST
:   “The POST method is used to ... [provide] a block of data, such
    as the result of submitting a form, to a data-handling process;
    extend a database though an append operation.”

DELETE
:   “The DELETE method requests that the origin server delete the
    resource identified by the Request-URI.”

The remaining lines, if any, are optional header lines that modify the
processing of the request. The end of the header lines is signalled by a
blank line. The format of each header line is a key or name followed by
a colon, followed by a string value. Here is a sample set of headers
([all headers](http://en.wikipedia.org/wiki/List_of_HTTP_headers)) for a
request for a page to give you an idea of the type of information that
is sent. I have bolded the header names to make them stand out, but in
the actual request it’s all plain text.

    Host: www.w3.org
    User-Agent: Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11
    Accept: text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5
    Accept-Language: en-gb,en;q=0.5
    Accept-Encoding: gzip,deflate
    Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
    Keep-Alive: 300
    Connection: keep-alive
    Referer: http://www.google.ca/[long URL trimmed]

The server puts together a similar package when it returns its response:
a status line ([status
codes](http://en.wikipedia.org/wiki/List_of_HTTP_status_codes)), then a
set of header lines, followed by a blank line, followed by the content
of the response. Here are the headers returned by the request above:

    Date: Wed, 06 Feb 2008 21:17:26 GMT
    Server: Apache/2
    Last-Modified: Wed, 01 Sep 2004 13:24:52 GMT
    Etag: "40d7-3e3073913b100"
    Accept-Ranges: bytes
    Content-Length: 16599
    Cache-Control: max-age=21600
    Expires: Thu, 07 Feb 2008 03:17:26 GMT
    P3P: policyref="http://www.w3.org/2001/05/P3P/p3p.xml"
    Content-Type: text/html; charset=iso-8859-1
    X-Cache: MISS from squid.yukoncollege.local
    X-Cache-Lookup: MISS from squid.yukoncollege.local:3128
    Via: 1.0 squid.yukoncollege.local:3128 (squid/2.6.STABLE14)
    Connection: keep-alive

For a very clear explanation of what happens between a client and server
see: [What really happens when you navigate to a
URL](http://igoro.com/archive/what-really-happens-when-you-navigate-to-a-url/)
