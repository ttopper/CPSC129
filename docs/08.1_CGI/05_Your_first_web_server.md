# Your first web server

Python has libraries that make it easy to create and run a simple web
server. This server is useful for testing and development, though not
robust or secure enough to run a large web site with significant
traffic. Still it’s pretty neat to be able to run a little web server
on your desktop. Here’s the code for the one we’ll use:

``` python
# httpserver.py
#
# When run locally the script serves up HTML pages from the directory it
# lives in or is launched from, and runs Python CGI scripts from the cgi-bin
# directory located there, i.e. HTML files are in the same directory as the
# script and CGI scripts are located in a subdirectory named cgi-bin. To visit
# them use URLs like,
# http://localhost/somepage.html
# http://localhost/cgi-bin/somescript.py
import os, sys
from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler

webdir = '.'
port = 8080

print(f'web directory "{webdir:s}", port {port:d}')

# Because Windows is brain dead ...
if sys.platform[:3] == 'win':
    CGIHTTPRequestHandler.have_popen2 = False
    CGIHTTPRequestHandler.have_popen3 = False
    sys.path.append('cgi-bin')

os.chdir(webdir)
serveraddr = ('', port)
server = HTTPServer( serveraddr, CGIHTTPRequestHandler)
server.serve_forever()
```

As you can see from the code it will serve over port 8080. Port numbers
less than 1024 require admin access, so they won't work well on the 
University's computers.
