# Towards an object server: #4 Final steps

The object creation form now has to parse the query string a little
differently than when it came in as a post because the browser formats
them differently. When the query string is submitted by GET it has the
url, followed by a question mark, followed by key/value pairs
(e.g. /object_creation_form?obj_type=quote). The keys and values are
separated by equal signs (=) and the pairs are separated by ampersands
(&). What we want to do is pull the value of the quote and we can do
this using the split method. Once we have the object type then we know
which creation form to run. In our example it is a quote creation form,
but it will change depending what the user selects.

```python
# 3) GET /object_creation_form
        #    => return the form for creating objects.
        elif self.path.startswith('/object_creation_form'):
            # Parse query string (e.g. /object_creation_form?obj_type=quote)
            # to get value of obj_type.
            self.path, self.query_string = self.path.split('?', 1)
            dummy, obj_type = self.query_string.split('=', 1)
            # Build the output page:
            title = '%s creation form' % (obj_type)
            body = eval(obj_type + '.CREATION_FORM')
            # Inject the page body into the page template.
            page = HTML5_template % (title, body)
            
            # Send the response and any header lines.
            self.send_response(200)
            self.end_headers()
            
            # Return the page.
            self.wfile.write(page.encode('utf-8'))
```

This code will work if we `import hockey_player` as well as quote.