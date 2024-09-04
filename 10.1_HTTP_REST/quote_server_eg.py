# object_server.py
#
# We will modify BaseHTTPServer to create our custom server.
import http.server

class myHTTPHandler(http.server.BaseHTTPRequestHandler):
    # BaseHTTPRequestHandler will call do_XXX when receiving
    # a request specifying method XXX.
    #
    # The do_XXX methods do not take any arguments because
    # self contains all the request information in its instance attributes.

    def do_GET(self):
        # HTML forms will append a ? to the URL,
        # remove it when present to standardize URLs.
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
            # Open the datastore and get a list of all the objects in it.
            # Build the output page:            
            # Build a list of HTML representations of the objects.
            # Assemble the body of the page.
            # Inject the page body into the page template.
            # Send the response and any header lines.
            # Return the page.
        # 2) GET /object_creation_form
        #    => return the form for creating objects.
            # Build the output page:
            # Inject the page body into the page template.
            # Send the response and any header lines.
            # Return the page.
        # 3) GET /uid/HTML_update_form
        #    => return the update form for object uid.
        # 4) GET /uid
        #    => return HTML representation of object uid.
            # (The request may not be for /uid but we can safely assume it is
            # since if it isn't not such object will be found and we'll
            # just return an error.)

    def do_POST(self):
        pass
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
        # 1) Is it a genuine POST?
            # Check that it is posting to a credible URL,
            # i.e. one with form /create/obj_type,
            # i.e. one that at least begins with /create/
                # The type of object to create is given by the suffix after /create/
                # Now try to create the object, e.g. quote.HTML_factory(self.args)
                # If creation was successful:         
                    # Now return a view of the newly created object by redirecting
                    # to its URL.
                # Otherwise something went wrong.
            # Otherwise POSTing to a disallowed URL.         
        # 2) Is this POST tunneling a PUT?
        # 3) Is this POST tunneling a DELETE?
        # 4) Got a bogus method.
            
    def do_PUT(self):
        pass
        # Check if the query string has already been parsed
        # i.e. if this request was tunneled through a POST.
        # If it wasn't then parse it now.
        # Get the uid.  
        # Fetch the object.                   
        # Determine the object type...                        
        # ...and create a new object based on the updated attributes.                        
        # If creation was successful:
            # Store the new object in the model and delete the old one.
            # Now return a view of the newly created object by redirecting
            # to its URL.
        # Otherwise something went wrong.

    def do_DELETE(self):
        pass
        # Get the uid of the object to delete.
        # Access the datastore.
        # If we delete the object successfully...
            # ...redirect the browser to the home page.
        # Otherwise something went wrong.
        # In any event close the datastore.

if __name__ == '__main__':
    PORT = 80
    server_address= ('', PORT)
    httpd = http.server.HTTPServer(server_address, myHTTPHandler)
    print('Serving on port', PORT, '...')
    httpd.serve_forever()

