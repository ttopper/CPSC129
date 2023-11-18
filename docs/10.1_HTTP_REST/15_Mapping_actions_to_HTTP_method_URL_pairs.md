# Mapping Actions to HTTP Method + URL pairs

Looking carefully back at the request-response cycles we can see that
deciding what to return to the client depends on **both** the HTTP
method **and** the URL specified.

  <table class="dark">
  <col>
  <col>
  <col>
  <col>
  <tbody>
    <tr>
      <th>Action</th>
      <th>HTTP Method</th>
      <th>URL</th>
      <th>Python Methods and Actions</th>
    </tr>
    <tr>
      <td>List all objects</td>
      <td>GET</td>
      <td>/</td>
      <td>model.listall() + display entries as HTML</td>
    </tr>
    <tr>
      <td>Retrieve an object</td>
      <td>GET</td>
      <td>/uid</td>
      <td>obj = model.retrieve(uid) + display as HTML, i.e. obj.HTML()</td>
    </tr>
    <tr>
      <td>Create a new object</td>
      <td>GET</td>
      <td>/object_creation_form</td>
      <td>new: but just return a static HTML page containing the form</td>
    </tr>
    <tr>
      <td></td>
      <td>POST</td>
      <td>/create/objtype</td>
      <td>obj = Quote() + model.create(obj) + display new object as HTML, i.e.
        obj.HTML()</td>
    </tr>
    <tr>
      <td>Delete an object</td>
      <td>DELETE</td>
      <td>/uid</td>
      <td>model.delete(uid) + model.listall() + display entries as HTML</td>
    </tr>
    <tr>
      <td>Update an object</td>
      <td>GET </td>
      <td>/uid/HTML_update_form</td>
      <td>new: return uid's update_form(), i.e. obj = model.retrieve(uid) +
        return obj.HTML_update_form()</td>
    </tr>
    <tr>
      <td></td>
      <td>PUT</td>
      <td>/uid</td>
      <td>new_uid = model.update(uid, obj) followed by obj =
        model.retrieve(new_uid) + display as HTML, i.e. obj.HTML()</td>
    </tr>
  </tbody>
</table>

There are only three new methods in the rightmost column of this table:

-   `obj.HTML()` The `Quote` class will have to add an `HTML` method
    that returns an HTML representation of an object (similar to the way
    `__str__` returns a plain text representation).

-   something that returns an object creation form, i.e.
    `Quote.``object_creation_form()`

-   `obj.HTML_update_form()` which has to return an HTML form for an
    object that is suitable to use in updating it. This should be
    identical to the object creation form except with values filled in.
