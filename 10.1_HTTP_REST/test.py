# object_server.py
#
# HTTP server that provides CRUD operations for Python objects.
#
# Version 1
#
# - Tidied up a bit.
#
# Version 0 (archived as object_server_0.py)
#
# - Initial roughing out to demonstrate HTTP concepts in practice.

HTML5_template = '''<!DOCTYPE HTML>
<!-- Minimal valid HTML5 document.
     Illustrates the necessary DOCTYPE declaration to be recognized as HTML5.
-->
<html>

<head>
    <title>%s</title>
</head>

<body>
    %s
</body>

</html>
'''

test_form = '''<!DOCTYPE HTML>
<html>

<head>
    <title>Test form</title>
</head>

<body>

    <form name="GET test" action="" method="GET">
        <fieldset><legend>GET</legend>
            UID: <input type="text" name="fname" value="123" /><br />
            <input type="submit" name="action" value="GET" />
        </fieldset>
    </form>

    <form name="POST test" action="" method="POST">
        <fieldset><legend>POST</legend>
            UID: <input type="text" name="fname" value="123" /><br />
            First name: <input type="text" name="fname" value="Mickey" /><br />
            Last name:<input type="text" name="lname" value="Mouse" /><br />
            <input type="submit" value="POST" />
        </fieldset>
    </form>

    <form name="PUT test" action="" method="PUT">
        <fieldset><legend>PUT</legend>
            UID: <input type="text" name="fname" value="123" /><br />
            First name: <input type="text" name="fname" value="Mickey" /><br />
            Last name:<input type="text" name="lname" value="Mouse" /><br />
            <input type="submit" value="PUT" />
        </fieldset>
    </form>

    <form name="DELETE test" action="" method="DELETE">
        <fieldset><legend>DELETE</legend>
            UID: <input type="text" name="fname" value="123" /><br />
            <input type="submit" value="DELETE" />
        </fieldset>
    </form>
</body>

</html>
'''

# This will not be a CGI app, but we will use the CGI module's
# facilities for parsing incoming form data.
import cgi

# We will modify http.server to create our server.
import http.server

class HTTPHandler(http.server.BaseHTTPRequestHandler):
    # BaseHTTPRequestHandler will call do_XXX when receiving
    # a request specifying method XXX.
    #
    # The do_XXX methods do not take any arguments because
    # self contains all the request information in its instance attributes.
    def do_GET(self):
        title = 'GET response'
        if self.path != '/':
            body = '<h1>Got a GET request.</h1><p>' + self.path + '</p>'
            self.wfile.write((HTML5_template % (title, body)).encode('utf-8'))
        else:
            self.wfile.write( test_form.encode('utf-8') )
            
    def do_POST(self):
        title = 'POST response'
        body = '<h1>Got a POST request.</h1>'
        self.wfile.write((HTML5_template % (title, body)).encode('utf-8'))
        
    def do_PUT(self):
        title = 'PUT response'
        body = '<h1>Got a PUT request.</h1>'
        self.wfile.write((HTML5_template % (title, body)).encode('utf-8'))
        
    def do_DELETE(self):
        title = 'DELETE response'
        body = '<h1>Got a DELETE request.</h1>'
        self.wfile.write((HTML5_template % (title, body)).encode('utf-8')) 
    
if __name__ == '__main__':
    server_address= ('', 80)
    httpd = http.server.HTTPServer(server_address, HTTPHandler)
    httpd.serve_forever()
