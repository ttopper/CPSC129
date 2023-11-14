# Mapping Actions to HTTP Method + URL pairs

Looking carefully back at the request-response cycles we can see that
deciding what to return to the client depends on **both** the HTTP
method **and** the URL specified.

  --------------------- ------------- ----------------------- ---------------------------------------------------------------------------------------------------------------
  Action                HTTP Method   URL                     Python Methods and Actions
  List all objects      GET           /                       model.listall() + display entries as HTML
  Retrieve an object    GET           /uid                    obj = model.retrieve(uid) + display as HTML, i.e. obj.HTML()
  Create a new object   GET           /object_creation_form   new: but just return a static HTML page containing the form
                        POST          /create/objtype         obj = Quote() + model.create(obj) + display new object as HTML, i.e. obj.HTML()
  Delete an object      DELETE        /uid                    model.delete(uid) + model.listall() + display entries as HTML
  Update an object      GET           /uid/HTML_update_form   new: return uid’s update_form(), i.e. obj = model.retrieve(uid) + return obj.HTML_update_form()
                        PUT           /uid                    new_uid = model.update(uid, obj) followed by obj = model.retrieve(new_uid) + display as HTML, i.e. obj.HTML()
  --------------------- ------------- ----------------------- ---------------------------------------------------------------------------------------------------------------

There are only three new methods in the rightmost column of this table:

-   `obj.HTML()` The `Quote` class will have to add an `HTML` method
    that returns an HTML representation of an object (similar to the way
    `__str__` returns a plain text representation).

-   something that returns an object creation form, i.e.
    `Quote.``object_creation_form()`

-   `obj.HTML_update_form()` which has to return an HTML form for an
    object that is suitable to use in updating it. This should be
    identical to the object creation form except with values filled in.
