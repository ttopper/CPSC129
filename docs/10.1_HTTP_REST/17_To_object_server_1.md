# Towards an object server: #1 Identify couplings to quote class

We would like to generalize our quote server to handle any type of
object. To do that we are going to walk through the quote server to
identify places where we have tightly coupled our code to the quote
object. If you search for the word quote in `quote_server_5.py` you will
find around a dozen places where the word quote is used. Many of these
are in the comments or the html, in these cases we can simply change the
word quote to the word object. We can also leave the `import` statement
alone, we still want to import our quote object, in the future we will
want to add other object types as well.

In the do_POST method we need to call the `HTML_factory` method for our
quote. This code already works for any object because it looks up the
object type based on the path, and then uses eval to call the
`HTML_factory` specific to that object type. As long as our new objects
have working HTML factories, this code is good to go.

```python
    # The type of object to create is given by the suffix after /create/
    obj_type = self.path[len('/create/'):]

    # Now try to create the object, e.g. quote.HTML_factory(self.args)
    obj = eval(obj_type + '.HTML_factory(self.args)')
```

The other change is related to the object creation form. Currently, when
you indicate that you want to make a new object it displays the
object_creation_form. This form is specific to quote objects, and won't
work for a general object server.

```python
    # 2) GET /object_creation_form
    #    => return the form for creating objects.
    elif self.path == '/object_creation_form':
           
        # Build the output page:
        title = 'Object creation form'
        body = quote.CREATION_FORM # Because at the moment we only have Quotes.
        # Inject the page body into the page template.
        page = HTML5_template % (title, body)
            
        # Send the response and any header lines.
        self.send_response(200)
        self.end_headers()
            
        # Return the page.
        self.wfile.write(page.encode('utf-8'))
```

In the future we will want that to display a drop down menu so that we
can pick which type of object we would like to add.