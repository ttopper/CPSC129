# Our HTTP Request-Response Cycles

So the flow of requests and responses looks like this. When the client
indicates they want to,

-   List all objects
    -   Request: GET http://localhost/
    -   Response: HTML list of HTML representations of all objects in
        datastore.
-   Retrieve an object, i.e. the HTML representation of an object
    -   Request: GET http://localhost/*uid*
    -   Response: HTML representation of the object, i.e. a web page.
-   Create a new object
    -   Request: GET http://localhost/*object_creation_form*
    -   Response: HTML form to fill in with object details.
    -   Request: POST http://localhost/object_creation_url
    -   Response: HTML representation of newly created object.
-   Delete an object
    -   Request: DELETE http://localhost/*uid*
    -   Response: Homepage of site (Seems reasonable, but not the only
        possibility --- we could give them a successful deletion message
        --- but this seems reasonable because we need to send them
        somewhere, and since the “current object” just got deleted we
        can’t send them to view it.)
-   Update an object
    -   Request: GET http://localhost/*uid/update_form*
    -   Response: HTML form filled with object details ready to be
        modified.
    -   Request: PUT http://localhost/*uid*
    -   Response: HTML representation of updated object.
