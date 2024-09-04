# Towards an object server: #3 Object creation menu Python code

The first change we want to make to our object server is that it needs
to detect when someone asks for an object creation menu and give them
the appropriate menu form. It also needs to detect, when it is asked for
the object creation form, what the value of that form variable object
type is. This will be added to our `do_GET` method. First I updated the
commenting to insert the menu as the second `elif`, this involved some
fiddly updating of the numbering in the comments too.

```python
        # There are five possible uses of GET we have to distinguish between.
        #   1) GET /
        #       => return a page displaying all objects in the datastore.
        #   2) GET /object_creation_menu
        #       => return the menu for selecting objects.
        #   3) GET /object_creation_form
        #       => return the form for creating objects.
        #   4) GET /uid/HTML_update_form
        #       => return the update form for object uid.
        #   5) GET /uid
        #       => return HTML representation of object uid.
```

Now it is time to start creating our menu. All I need to do is adjust
the path, change the title, and change the body. The body of the page is
no longer created by a function, instead we've replaced it with a static
variable called `CREATION_MENU`.


```python
    # 2) GET /object_creation_menu
    #    => return the menu for selecting object type to create.
    elif self.path == '/object_creation_menu':
           
        # Build the output page:
        title = 'Object creation menu'
        body = CREATION_MENU
        # Inject the page body into the page template.
        page = HTML5_template % (title, body)
            
        # Send the response and any header lines.
        self.send_response(200)
        self.end_headers()
            
        # Return the page.
        self.wfile.write(page.encode('utf-8'))
```

The next step is to write the html for the menu. The place for a static
variable is at the top of our code. It will be a triple quoted string
with the html page. The new element is the dropdown list, which we
haven't used before. The dropdown gets implemented using a select
object. This menu will send the user to the object creation form.

```python
CREATION_MENU = '''
<h1>Object Creation Menu</h1> 
 
<div> 
<p style="text-align: center;">Select the type of object you would like to
create:</p> 
 
<form method="get" action="http://localhost/object_creation_form"
style="text-align: center;"> 
 
  <select name="obj_type"> 
    <option value="quote" selected="selected">Quote</option> 
    <option value="hockey_player">Hockey Player</option> 
  </select> 
  <br /> 
 
  <input type="submit" value="Continue" />
</form> 
</div> 
'''
```

We also need to change the button to select an object to point to our
selection menu, instead of the quote creation form. This is in the title
block of the homepage, which is handled in the GET method.

```python
if self.path == '/':
            print('Handling /')
            # Open the datastore and get a list of all the objects in it.
            m = model.Model('test_model')
            obj_set = m.listall()
            m.close()
            
            # Build the output page:            
            title = 'Ojectserver Home Page'
            title_block = '''
                <h1>ObjectServer Home Page</h1> 
                 
                <form method="GET" action="/object_creation_menu"> #CHANGE to _menu
                  <input type="submit" value="Add a new Object" /> 
                </form> 
                 
                <h2>Current Objects:</h2>
            '''
            # Build a list of HTML representations of the objects.
            obj_set_HTML = []
            for obj in obj_set:
                obj_set_HTML.append(obj.HTML())
                
            # Assemble the body of the page.
            body = '\n'.join([title_block,'\n'.join(obj_set_HTML)])

            # Inject the page body into the page template.
            page = HTML5_template % (title, body)
            
            # Send the response and any header lines.
            self.send_response(200)
            self.end_headers()
            
            # Return the page.
            self.wfile.write(page.encode('utf-8'))
```

Next we need to object creation form to detect the object type.
