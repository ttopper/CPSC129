# Translating MVC+CRUD to HTTP

Our MVC_controller.py supported the following actions:

        Actions
        -------
        c - create an object to add to the collection
        r - retrieve an object from the collection and display it
        u - update an object in the collection
        d - delete an object from the collection
        l - list all the objects in the collection
        q - exit

We want to support the same functionality using HTTP, with a browser as
the client, and our same shelve as the back-end datastore.

Now how _exactly_ can we map these CRUD actions onto the HTTP methods?
There are two issues we have to resolve.

1.  Remember that the form of an HTTP request is `METHOD URL VERSION` so
    we need to identify the URLs for each method, i.e. we have to say
    **GET** from ***somewhere***, **POST** to ***somewhere*** etc.

    Some of these are easier to figure out than others:

    GET and DELETE will obviously be `GET uid` to retrieve the html
    representation of object uid, and `DELETE uid` to delete the object
    with UID uid.

    UPDATE is not so clear. Clearly we will want to issue `UPDATE uid`
    to update the object with UID uid, but we will have to send it the
    information to use in creating the updated object which presumes an
    earlier interaction. Remember that in our console-based controller
    we _first_ got the modified values by interacting with the user and
    _then_ called the update method in model.py. In an HTTP system the
    initial interaction will be achieved by presenting the user with an
    HTML form to fill in and then submitting this form to trigger the
    UPDATE.

2.  This highlights the second issue: Some of those actions invoked an
    interaction between the user and the controller, but HTTP is
    stateless, that is each request is handled alone without knowledge
    of previous requests. (Now lots of approaches to web apps try to get
    around this by managing sessions, but that adds complexity,
    fragility and makes many desirable performance features of the web
    unavailable, e.g. caching. )

    So we will need to call one form to fill in the modified values and
    then PUT that form to trigger the actual update.

    Similarly using POST to create a new object will involve two steps,
    first requesting a form to use to specify the characteristics of the
    new object and second a POST request to actually trigger its
    creation. Now where do we post to to create a new object? To a
    special object creation URL.

    Finally there is listall to consider. We will do that by GETting the
    server root.
