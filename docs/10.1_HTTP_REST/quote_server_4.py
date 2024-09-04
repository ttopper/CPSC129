# object_server.py
#
# HTTP server that provides CRUD operations for Python objects.
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

# We will modify BaseHTTPServer to create our server.
import BaseHTTPServer

class myHTTPHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    # BaseHTTPRequestHandler will call do_XXX when receiving
    # a request specifying method XXX.
    #
    # The do_XXX methods do not take any arguments because
    # self contains all the request information in its instance attributes.
    def do_GET(self):
        print 'GET for', self.path # Debug
        # HTML forms will append a ? to the URL,
        # remove it when present to standardize URLs.
        self.path = self.path.rstrip('?')

        # There are four possible uses of GET we have to distinguish between.
        #   1) GET / => return a page displaying all objects in the datastore.
        #   2) GET /object_creation_form => return the form for creating objects.
        #   3) GET /uid/HTML_update_form => return the update form for object uid.
        #   4) GET /uid => return HTML representation of object uid.
        #
        # 1) GET / => return a page displaying all objects in the datastore.
        if self.path == '/':
            m = model.Model('test_model')
            obj_set = m.listall()
            m.close()
            obj_set_HTML = []
            for obj in obj_set:
                obj_set_HTML.append(obj.HTML())
            title = 'Quoteserver Home Page'
            title_block = '''
                <h1>QuoteServer Home Page</h1> 
                 
                <form method="GET" action="/object_creation_form"> 
                  <input type="submit" value="Add a new Quote" /> 
                </form> 
                 
                <h2>Current Quotes:</h2>
            '''
            body = '\n'.join([title_block,'\n'.join(obj_set_HTML)])
            self.send_response(200)
            self.end_headers()
            self.wfile.write( HTML5_template % (title, body) )
            
        # 2) GET /object_creation_form => return the form for creating objects.
        elif self.path == '/object_creation_form':
            self.send_response(200)
            self.end_headers()
            title = 'Quote creation form'
            body = quote.CREATION_FORM # Because at the moment we only have Quotes.
            self.wfile.write( HTML5_template % (title, body) )

        # 3) GET /uid/HTML_update_form => return the update form for object uid.
        elif self.path[-17:] == '/HTML_update_form':
            uid = self.path[1:-17]
            print '\t uid =', uid # Debug
            m = model.Model('test_model')
            obj = m.retrieve(uid)
            m.close()
            if obj:
                self.send_response(200)
                self.end_headers()
                title = 'Update form for object %s', 
                body = obj.HTML_update_form()
                self.wfile.write( HTML5_template % (title, body) )
            else:
                self.send_response(404) # Not found.
                self.end_headers()
                title = 'Error: Object %s not found!' % (uid) # ???
                body = '<h1>Error: Object %s not found!</h1>' % (uid)
                self.wfile.write( HTML5_template % (title, body) )
        
        # 4) GET /uid => return HTML representation of object uid.
        else:
            # (The request may not be for /uid but we can safely assume it is
            # since if it isn't not such object will be found and we'll
            # just return an error.)
            uid = self.path[1:] # Trim the leading / from the URL to get a uid.
            m = model.Model('test_model')            
            obj = m.retrieve(uid) # Retrieve the obejct from the datastore.
            m.close()
            if obj:
                self.send_response(200)
                self.end_headers()
                title = 'Object %s' % (uid)
                body = obj.HTML() # Call its HTML method.
                self.wfile.write( HTML5_template % (title, body) )
            else:
                self.send_response(404) # Not found.
                self.end_headers()
                title = 'Error: Object %s not found!' % (uid)
                body = '<h1>Error: Object %s not found!</h1>' % (uid)
                self.wfile.write( HTML5_template % (title, body) )
            
    def do_POST(self):
        print 'POST to', self.path # Debug
        # There are three legitimate possible uses of POST we have to
        # distinguish between.
        #
        # The first is the genuine POST:
        #
        #   1) POST /create/objtype =>
        #       Create an obj of class objtype, and
        #       return a page displaying the newly created object.
        #
        # The other two are when we tunnel PUT and DELETE through POST.
        #
        #   2) POST /uid with method field == 'PUT' =>
        #       Modify object uid, and
        #       return a page displaying the modified object.
        #
        #   3) POST /uid with method field == 'DELETE' =>
        #       Delete object uid, and
        #       redirect to the home page.
        #
        # We could detect the true POST by looking at the URL POSTed to,
        # but this would not extend to tunneled PUTs and DELETEs because they
        # use the same URL.
        #
        # Instead, for similarity of processing, we will test the hidden method
        # field in all three cases and react appropriately.
        #
        # Parse query string to get method field.
        # Parse the form arguments into a dictionary.
        self.query_string = self.rfile.read(int(self.headers['Content-Length']))
        self.args = dict(cgi.parse_qsl(self.query_string))
        
        # 1) Is it a genuine POST?
        if self.args['_method'] == 'POST':
            print 'Got a genuine POST'
            # Check that it is posting to a credible URL,
            # i.e. one with form /create/obj_type,
            # i.e. one that at least begins with /create/
            if self.path[:8] != '/create/':
                self.send_response(405) # Method not allowed by that resource.
                self.end_headers()
                title = 'Error: Can’t POST to %s!' % (self.path)
                body = '<h1>Error: Can’t POST to %s!</h1>' % (self.path)
                self.wfile.write( HTML5_template % (title, body) )
            else:
                # The type of object to create is given by the suffix after /create/
                obj_type = self.path[8:]
                # Now try to create the object, e.g. quote.HTML_factory(self.args)
                obj = eval(obj_type + '.HTML_factory(self.args)')
                if obj:
                    m = model.Model('test_model')
                    m.create(obj)
                    m.close()
                    # Now return a view of the newly created object by redirecting
                    # to its URL.
                    self.send_response(301)
                    self.send_header('Location', '/%s' % obj.uid)
                    self.end_headers()
                else:
                    self.send_response(500) # Internal server error.
                    self.end_headers()
                    title = 'Error: obj not created!'
                    body = '<h1>Error: obj not created!</h1>'
                    self.wfile.write( HTML5_template % (title, body) )
                    
        # 2) Is this POST tunneling a PUT?
        elif self.args['_method'] == 'PUT':
            print 'Got a PUT tunneled through a POST'
            self.do_PUT()
            
        # 3) Is this POST tunneling a DELETE?
        elif self.args['_method'] == 'DELETE':
            print 'Got a DELETE tunneled through a POST'
            self.do_DELETE()

        # 4) Got a bogus method.
        else:
            self.send_response(405) # Method not allowed.
            self.end_headers()
            title = 'Error: method %s not recognized!' % (self.args['_method'])
            body = '<h1>Error: method %s not recognized!</h1>' % (self.args['_method'])
            self.wfile.write( HTML5_template % (title, body) )
                    
    def do_PUT(self):
        print 'PUT to', self.path # Debug
        # Check if the query string has already been parsed
        # i.e. if this request was tunneled through a POST.
        # If it wasn't then parse it now.
        if not self.args:
            self.query_string = self.rfile.read(int(self.headers['Content-Length']))
            self.args = dict(cgi.parse_qsl(self.query_string))
            
        old_uid = self.path[1:]
        m = model.Model('test_model')
        old_obj = m.retrieve(old_uid)
        m.close()
        obj_type = old_obj.__module__
        new_obj = eval(obj_type + '.HTML_factory(self.args)')
        if new_obj:
            m = model.Model('test_model')
            new_uid = m.update(old_uid, new_obj)
            m.close()
            # Now return a view of the newly created object by redirecting
            # to its URL.
            self.send_response(301)
            self.send_header('Location', '/%s' % new_obj.uid)
            self.end_headers()
        else:
            self.send_response(500) # Internal server error.
            self.end_headers()
            title = 'UPDATE Error: obj not created!'
            body = '<h1>UPDATE Error: obj not created!</h1>'
            self.wfile.write( HTML5_template % (title, body) )
            
    def do_DELETE(self):
        print 'DELETE for', self.path # Debug
        uid = self.path[1:] # Trim the leading / from the URL to get a uid.
        m = model.Model('test_model')
        if m.delete(uid):
            self.send_response(301)
            self.send_header('Location', '/')
            self.end_headers()
        else:
            self.send_response(500) # Internal server error.
            self.end_headers()
            title = 'DELETE failed'
            body = '<h1>DELETE request for %s failed.</h1>' % (self.path)
            self.wfile.write( HTML5_template % (title, body))
        m.close()
      
if __name__ == '__main__':
    PORT = 80
    server_address= ('', PORT)
    httpd = BaseHTTPServer.HTTPServer(server_address, myHTTPHandler)
    print 'Serving on port', PORT, '...'
    httpd.serve_forever()
