# CRUD vs HTTP

We’ve seen what the GET method does, but what about those other
methods: POST, PUT and DELETE? Their existence points out that web
servers can and do more than serve web pages. They can allow us to
upload, edit and delete resources as well.

Consider again the guidelines for using those methods:

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

You’ll notice that although the names differ these four operations map
neatly onto the CRUD model of operations.

| CRUD     | HTTP   |
|----------|--------|
| Create   | POST   |
| Retrieve | GET    |
| Update   | PUT    |
| Delete   | DELETE |


This is no accident; the engineers who designed HTTP knew what they were
doing. Modern best practice in web development is to build servers that
implement REST architecture. This stands for [Representational State
Transfer](http://en.wikipedia.org/wiki/Representational_State_Transfer)
and is a topic unto itself, but you won’t go far wrong if you think of
it as treating HTTP as CRUD using other names, and that’s what we will
do.
