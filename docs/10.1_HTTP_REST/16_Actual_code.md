# Actual code

The code logic flows quite cleanly from the HTTP Method column. We can
see that ideally we only have any logic with GET requests (since four
actions use GET requests), but that with POST, PUT and DELETE we always
follow a single course of action.

I say ideally because the ugly truth about browsers means that POST will
actually correspond to three possibilities: a true POST, a tunneled
UPDATE, or a tunneled DELETE. This is handled by including a hidden
field in the input forms giving the actual intended method. This
requires modifications to the forms which are provided by quote.py (see
below).

``` python
# quote_server.py
#
# HTTP server that provides CRUD operations for Quote objects.
#
# Version 5
#
# - Tidied up substantially.
#
# Version 4
#
# - Implemented PUT and DELETE by tunneling them through POST.
#
# Version 3
#
# - Implement all GETs and POSTs pending decision on how to proceed
#   with PUTs and DELETEs.
#
# Version 1
#
# - Tidied up a bit.
#
# Version 0 (archived as object_server_0.py)
#
# - Initial roughing out to demonstrate HTTP concepts in practice.
# - Tries to send genuine PUT and DELETE.

import quote
import model # Was named MVC_model

HTML5_template = open('HTML5_template.html','r').read()

# We will modify http.server to create our server.
import http.server

# Needed to parse the arguments
import urllib.parse

class myHTTPHandler(http.server.BaseHTTPRequestHandler):
    # BaseHTTPRequestHandler will call do_XXX when receiving
    # a request specifying method XXX.
    #
    # The do_XXX methods do not take any arguments because
    # self contains all the request information in its instance attributes.
    
    def do_GET(self):
        print('GET for', self.path)
        # HTML forms will append a ? to the URL,
        # remove it when present to standardize URLs.
        self.path = self.path.rstrip('?')

        # There are four possible uses of GET we have to distinguish between.
        #   1) GET /
        #       => return a page displaying all objects in the datastore.
        #   2) GET /object_creation_form
        #       => return the form for creating objects.
        #   3) GET /uid/HTML_update_form
        #       => return the update form for object uid.
        #   4) GET /uid
        #       => return HTML representation of object uid.

        # 1) GET /
        #    => return a page displaying all objects in the datastore.
        if self.path == '/':
            print('Handling /')
            # Open the datastore and get a list of all the objects in it.
            m = model.Model('test_model')
            obj_set = m.listall()
            m.close()
            
            # Build the output page:            
            title = 'Quoteserver Home Page'
            title_block = '''
                <h1>QuoteServer Home Page</h1> 
                 
                <form method="GET" action="/object_creation_form"> 
                  <input type="submit" value="Add a new Quote" /> 
                </form> 
                 
                <h2>Current Quotes:</h2>
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
            
        # 2) GET /object_creation_form
        #    => return the form for creating objects.
        elif self.path == '/object_creation_form':
            
            # Build the output page:
            title = 'Quote creation form'
            body = quote.CREATION_FORM # Because at the moment we only have Quotes.
            # Inject the page body into the page template.
            page = HTML5_template % (title, body)
            
            # Send the response and any header lines.
            self.send_response(200)
            self.end_headers()
            
            # Return the page.
            self.wfile.write(page.encode('utf-8'))

        # 3) GET /uid/HTML_update_form
        #    => return the update form for object uid.
        elif self.path.endswith('/HTML_update_form'):
            uid = self.path[1:-len('/HTML_update_form')]
            
            m = model.Model('test_model')
            obj = m.retrieve(uid)
            m.close()
            
            if obj:
                title = 'Update form for object %s', 
                body = obj.HTML_update_form()
                page = HTML5_template % (title, body)
                
                self.send_response(200)
                self.end_headers()
                
                self.wfile.write(page.encode('utf-8'))
            else:
                self.send_response(404) # Not found.
                self.end_headers()                
                print('Error: Object %s not found!' % (uid))
        
        # 4) GET /uid
        #    => return HTML representation of object uid.
        else:
            # (The request may not be for /uid but we can safely assume it is
            # since if it isn't not such object will be found and we'll
            # just return an error.)
            uid = self.path[1:] # Trim the leading / from the URL to get a uid.
            
            m = model.Model('test_model')            
            obj = m.retrieve(uid) # Retrieve the obejct from the datastore.
            m.close()
            
            if obj:
                title = 'Object %s' % (uid)
                body = obj.HTML() # Call its HTML method.
                page = HTML5_template % (title, body)
                
                self.send_response(200)
                self.end_headers()
                
                self.wfile.write(page.encode('utf-8'))
            else:
                self.send_response(404) # Not found.
                self.end_headers()
                print('Error: Object %s not found!' % (uid))
            
    def do_POST(self):
        # There are three legitimate possible uses of POST we have to
        # distinguish between.
        #
        # The first is the genuine POST:
        #
        #   1) POST /create/objtype
        #      => Create an obj of class objtype, and
        #         return a page displaying the newly created object.
        #
        # The other two are when we tunnel PUT and DELETE through POST.
        #
        #   2) POST /uid with method field == 'PUT'
        #      => Modify object uid, and
        #         return a page displaying the modified object.
        #
        #   3) POST /uid with method field == 'DELETE'
        #      => Delete object uid, and
        #         redirect to the home page.
        #
        # We could detect the true POST by looking at the URL POSTed to,
        # but this would not extend to tunneled PUTs and DELETEs because they
        # both use the same URL.
        #
        # Instead, for similarity of processing, we will test the hidden method
        # field in all three cases and react appropriately.

        # Parse the query string to get method field which means first
        # parsing the form arguments into a dictionary.
        self.query_string = self.rfile.read(int(self.headers['Content-Length']))
        self.args = dict(urllib.parse.parse_qsl(self.query_string))
        
        # 1) Is it a genuine POST?
        if self.args[b'_method'] == b'POST':
            print('Got a genuine POST')
            # Check that it is posting to a credible URL,
            # i.e. one with form /create/obj_type,
            # i.e. one that at least begins with /create/
            if self.path.startswith('/create/'):
                # The type of object to create is given by the suffix after /create/
                obj_type = self.path[len('/create/'):]
                                 
                # Now try to create the object, e.g. quote.HTML_factory(self.args)
                obj = eval(obj_type + '.HTML_factory(self.args)')

                # If creation was successful:         
                if obj:
                    m = model.Model('test_model')
                    m.create(obj)
                    m.close()
                    # Now return a view of the newly created object by redirecting
                    # to its URL.
                    self.send_response(301)
                    self.send_header('Location', '/%s' % obj.uid)
                    self.end_headers()

                # Otherwise something went wrong.
                else:
                    self.send_response(500) # Internal server error.
                    self.end_headers()
                    print('POST Error: obj not created!')

            # Otherwise POSTing to a disallowed URL.         
            else:
                self.send_response(405) # Method not allowed by that resource.
                self.end_headers()
                print('Error: Tried to POST to %s!' % (self.path))
                    
        # 2) Is this POST tunneling a PUT?
        elif self.args[b'_method'] == b'PUT':
            self.do_PUT()
            
        # 3) Is this POST tunneling a DELETE?
        elif self.args[b'_method'] == b'DELETE':
            self.do_DELETE()

        # 4) Got a bogus method.
        else:
            self.send_response(405) # Method not allowed.
            self.end_headers()
            print('POST Error: method %s not recognized!' % (self.args[b'_method']))
                    
    def do_PUT(self):
        # Check if the query string has already been parsed
        # i.e. if this request was tunneled through a POST.
        # If it wasn't then parse it now.
        if not self.args:
            self.query_string = self.rfile.read(int(self.headers['Content-Length']))
            self.args = dict(urllib.parse.parse_qsl(self.query_string))
                                 
        # Get the uid.  
        old_uid = self.path[1:] # Ignore the initial /
                                 
        # Fetch the object.                   
        m = model.Model('test_model')
        old_obj = m.retrieve(old_uid)
        m.close()
                                 
        # Determine the object type...                        
        obj_type = old_obj.__module__
        # ...and create a new object based on the updated attributes.                        
        new_obj = eval(obj_type + '.HTML_factory(self.args)')

        # If creation was successful:
        if new_obj:
            # Store the new object in the model and delete the old one.
            m = model.Model('test_model')
            new_uid = m.update(old_uid, new_obj)
            m.close()
            # Now return a view of the newly created object by redirecting
            # to its URL.
            self.send_response(301)
            self.send_header('Location', '/%s' % new_obj.uid)
            self.end_headers()

        # Otherwise something went wrong.
        else:
            self.send_response(500) # Internal server error.
            self.end_headers()
            print('UPDATE Error: obj not created!')
            
    def do_DELETE(self):
        # Get the uid of the object to delete.
        uid = self.path[1:] # Trim the leading / from the URL to get a uid.
                                 
        # Access the datastore.
        m = model.Model('test_model')
                                 
        # If we delete the object successfully...
        if m.delete(uid):
            # ...redirect the browser to the home page.
            self.send_response(301)
            self.send_header('Location', '/')
            self.end_headers()
                                 
        # Otherwise something went wrong.
        else:
            self.send_response(500) # Internal server error.
            self.end_headers()
            print('DELETE failed')
        # In any event close the datastore.
        m.close()
      
if __name__ == '__main__':
    PORT = 80
    server_address= ('', PORT)
    httpd = http.server.HTTPServer(server_address, myHTTPHandler)
    print('Serving on port', PORT, '...')
    httpd.serve_forever()

```

``` python
# quote.py
#
# Version 3
#
# Changes:
#
# - Adding HTML methods.
# - Rename factory to be console_factory
# - Rename update to be console_update
#
# Version 2 (archived as quote_2.py)
#
# Changes:
#
# - Implemented Quote.update() method.
#
# Version 1 (archived as quote_1.py)
#
# Changes:
#
# - Changed naming convention to initial lower case to ease  importing.
#
# - Added creation method to be called from controller when new Quote
#   object is required.
#
# - Changed name of object creation routine from "create" to "factory"
#   to avoid confusion with Model.create and to follow common practice
#   of Factory patterns
#   (see e.g. http://en.wikipedia.org/wiki/Factory_method_pattern).
#
# Version 0 (archived as Quote_0.py)
#
# - Initial roughing out.

def console_factory():
    '''Handles console interaction required to create a new Quote object.'''
    author = input('Who is the author of the quote? ')
    text = input('What did they say or write? ')
    return Quote(author, text)

def HTML_factory(form_dict):
    '''Builds a Quote from the data returned in the form
    CREATION_FORM.'''
    author = form_dict[b'author'].decode('utf-8')
    text = form_dict[b'text'].decode('utf-8')
    return Quote(author, text)

# Use this template for both creation via POST and update via PUT.
CREATION_FORM = '''
<h1>Create form</h1>

<div> 
    <form method="POST" action="http://localhost/create/quote">
        <input type="hidden" name="_method" value="POST" />
        <label
for="text">Text:</label><textarea id="text" name="text" rows="3"

        cols="50">Enter the quote here...</textarea><br /> 
        <label for="author">Author:</label><input type="text" id="author"

        name="author" size="50" /><br /> 
        <label for="method">&nbsp;</label> 
        <input type="submit" value="Create" />
    </form> 
</div> 
'''

UPDATE_TEMPLATE = '''
<h1>Update form</h1>

<div>
    <form method="POST" action="http://localhost/%s">
        <input type="hidden" name="_method" value="PUT" />
        <label
for="text">Text:</label><textarea id="text" name="text" rows="3"

        cols="50">%s</textarea><br /> 
        <label for="author">Author:</label><input type="text" id="author"

        name="author" size="50" value="%s"/><br /> 
        <label for="method">&nbsp;</label> 
        <input type="submit" value="Update" />
    </form> 
</div> 
'''

HTML_TEMPLATE = '''
<div> 
    <blockquote> 
      <p><span class="quote-text">%s</span> ~
      <span class="quote-author">%s</span></p> 
    </blockquote> 

    <!-- View this quote alone. -->
    <form method="GET" action="http://localhost/%s" class="view"> 
      <input type="submit" value="View" />
    </form>

    <!-- Request the update form for this quote. -->
    <form method="GET" action="http://localhost/%s/HTML_update_form" class="update">
      <input type="submit" value="Update" />
    </form>

    <!-- Delete this quote. -->
    <form method="POST" action="http://localhost/%s" class="delete">
      <input type="hidden" name="_method" value="DELETE" />
      <input type="submit" value="Delete" /> 
    </form> 
</div>
'''

class Quote:
    def __init__(self, author='', text=''):
        self.author = author
        self.text = text
        self.uid = str(hash('Quote' + self.author + self.text))

    def __str__(self):
        return '[%s] %s said "%s"' % (self.uid, self.author, self.text)

    def HTML(self):
        return HTML_TEMPLATE % (self.text, self.author, self.uid, self.uid, self.uid)

    def HTML_update_form(self):
        return UPDATE_TEMPLATE % (self.uid, self.text, self.author)

    def console_update(self):
        '''Handles the console interaction required to modify a Quote object.'''
        
        print('The current author is:', self.author)
        change = input('Modify author (y/n)? ')
        if change in ['y', 'Y']:
            self.author = input('Enter modified author: ')
        print('The current text is:', self.text)
        change = input('Modify text (y/n)? ')
        if change in ['y', 'Y']:
            self.text = input('Enter modified text: ')
        self.uid = str(hash('Quote' + self.author + self.text))        

if __name__ == '__main__':
    def bordered(s):
        return len(s)*'='+'\n'+s+'\n'+len(s)*'-'
    
    print(bordered('Testing __init__() and __str__()'))
    q = Quote( 'Kent Beck', 'Optimism is an occupational hazard of programming: testing is the treatment.')
    r = Quote( 'Brian Kernighan', 'Controlling complexity is the essence of computer programming.')
    print('The Quote q is:')
    print('\t', q)
    print('The Quote r is:')
    print('\t', r)
    print()

    print(bordered('Testing HTML()'))
    print('Here’s the HTMl representation of q:')
    print(q.HTML())

##    print(bordered('Testing console_factory()'))
##    s = console_factory()
##    print('Here’s the new Quote object:')
##    print('\t', s)
##    print('Did factory create a Quote object?',)
##    print(type(s) == type(q)) # Checks that factory is returning a Quote object.
##    print()
##
##    print(bordered('Testing console_update()'))
##    print('The Quote q before:')
##    print('\t', q)
##    print()
##    print('Calling console_update():')
##    print()
##    q.console_update()
##    print()
##    print('The Quote q after:')
##    print('\t', q)
##    print()
```
