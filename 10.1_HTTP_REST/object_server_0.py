# object_server.py
#
# HTTP server that provides CRUD operations for Python objects.
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
            title = 'Ojectserver Home Page'
            title_block = '''
                <h1>ObjectServer Home Page</h1> 
                 
                <form method="GET" action="/object_creation_form"> 
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
                                 
                # Now try to create the object, e.g. objtype.HTML_factory(self.args)
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
