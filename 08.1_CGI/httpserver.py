# httpserver.py
#
# When run locally the script serves up HTML pages from the directory it
# lives in or is launched from, and runs Python CGI scripts from the cgi-bin
# directory located there, i.e. HTML files are in the same directory as the
# script and CGI scripts are located in a subdirectory named cgi-bin. To visit
# them use URLs like,
# http://localhost:8080/somepage.html
# http://localhost:8080/cgi-bin/somescript.py
import os, sys
from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler

webdir = '.'
port = 8080

print(f'web directory "{webdir}", port {port:d}')

# Because Windows is brain dead ...
if sys.platform[:3] == 'win':
    CGIHTTPRequestHandler.have_popen2 = False
    CGIHTTPRequestHandler.have_popen3 = False
    sys.path.append('cgi-bin')

os.chdir(webdir)
serveraddr = ('', port)
server = HTTPServer( serveraddr, CGIHTTPRequestHandler)
server.serve_forever()
