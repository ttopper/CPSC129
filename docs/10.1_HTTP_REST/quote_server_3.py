# object_server.py
#
# HTTP server that provides CRUD operations for Python objects.
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

# Open datastore
m = model.Model('test_model')

class myHTTPHandler(http.server.BaseHTTPRequestHandler):
    # BaseHTTPRequestHandler will call do_XXX when receiving
    # a request specifying method XXX.
    #
    # The do_XXX methods do not take any arguments because
    # self contains all the request information in its instance attributes.
    def do_GET(self):
        print('GET for', self.path) # Debug
        self.path = self.path.rstrip('?')
        if self.path == '/':
            # return a page displaying all objects in the datastore.
            title = 'Quoteserver Home Page'
            obj_set = m.listall()
            obj_set_HTML = []
            for obj in obj_set:
                obj_set_HTML.append(obj.HTML())
            title_block = '''
                <h1>QuoteServer Home Page</h1> 
                 
                <form method="GET" action="/object_creation_form"> 
                  <input type="submit" value="Add a new Quote" /> 
                </form> 
                 
                <h2>Current Quotes:</h2>
               '''
            body = '\n'.join([title_block,'\n'.join(obj_set_HTML)])
            self.wfile.write((HTML5_template % (title, body)).encode('utf-8'))
            
        elif self.path == '/object_creation_form':
            # return the form for creating objects.
            title = 'Quote creation form'
            body = quote.CREATION_FORM
            self.wfile.write((HTML5_template % (title, body)).encode('utf-8'))

        elif self.path[-17:] == '/HTML_update_form':
            uid = self.path[1:-17]
            print('\t uid =', uid)
            # return the update form for the object.
            obj = m.retrieve(uid)
            if obj:
                title = 'Update form for object %s', 
                body = obj.HTML_update_form()
                self.wfile.write((HTML5_template % (title, body)).encode('utf-8'))
            else:
                title = 'Error: Object %s not found!' % (uid)
                body = '<h1>Error: Object %s not found!</h1>' % (uid)
                self.wfile.write((HTML5_template % (title, body)).encode('utf-8') )
        else:
            # Assume they have passed the uid for an object to be displayed.
            uid = self.path[1:] # Trim the leading /
            obj = m.retrieve(uid)
            if obj:
                title = 'Object %s' % (uid)
                body = obj.HTML()
                self.wfile.write((HTML5_template % (title, body)).encode('utf-8') )
            else:
                title = 'Error: Object %s not found!' % (uid)
                body = '<h1>Error: Object %s not found!</h1>' % (uid)
                self.wfile.write((HTML5_template % (title, body)).encode('utf-8'))
            
    def do_POST(self):
        print('POST to', self.path) # Debug
        print('\t', self.path[:8])
        if self.path[:8] != '/create/':
            title = 'Error: Can’t POST to %s!' % (self.path)
            body = '<h1>Error: Can’t POST to %s!</h1>' % (self.path)
            self.wfile.write((HTML5_template % (title, body)).encode('utf-8'))
        else:
            print('\t obj_type =', self.path[8:]) # Debug
            obj_type = self.path[8:]
            # Parse the form arguments into a dictionary.
            print('\t Reading query string') # Debug
            self.query_string = self.rfile.read(int(self.headers['Content-Length']))
            print('\t self.query_string =', self.query_string) # Debug
            print('\t Parsing query string') # Debug
            self.args = dict(urllib.parse.parse_qsl(self.query_string))
            print('\t', self.args) # Debug
            print('\t Calling', obj_type+'.HTML_factory(self.args)') # Debug
            obj = eval(obj_type+'.HTML_factory(self.args)') # e.g. quote.HTML_factory(self.args)
            if obj:
                print('\t obj =', obj) # Debug
                m.create(obj)
                # Now return a view of the newly created object.
                # (Should check it was successfully cretaed before doing this.)
                #title = 'Object %s' % (uid)
                #body = obj.HTML()
                #self.wfile.write( HTML5_template % (title, body) )
                self.send_response(301)
                self.send_header('Location', '/%s' % obj.uid)
                self.end_headers()
            else:
                title = 'Error: obj not created!'
                body = '<h1>Error: obj not created!</h1>'
                self.wfile.write((HTML5_template % (title, body)).encode('utf-8'))
            
            
        title = 'POST response'
        body = '<h1>Got a POST request to:</h1>'
        self.wfile.write((HTML5_template % (title, body)).encode('utf-8'))
        
    def do_PUT(self):
        print('PUT to', self.path) # Debug
        title = 'PUT response'
        body = '<h1>Got a PUT request to:</h1>'
        self.wfile.write( HTML5_template % (title, body))
        
    def do_DELETE(self):
        print('DELETE for', self.path) # Debug
        title = 'DELETE response'
        body = '<h1>Got a DELETE request for:</h1>'
        self.wfile.write((HTML5_template % (title, body)).encode('utf-8')) 
      
if __name__ == '__main__':
    PORT = 80
    server_address= ('', PORT)
    httpd = http.server.HTTPServer(server_address, myHTTPHandler)
    print('Serving on port', PORT, '...')
    httpd.serve_forever()
