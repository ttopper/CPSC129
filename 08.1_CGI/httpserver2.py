# httpserver.py

# When run locally the script serves up HTML pages from the diretory it
# lives in or is launched from, and runsPython CGI scripts from the cgi-bin
# directory located there, i.e. HTML files are in the same directory as the
# script and CGI scripts are located in the cgi-bin subdirectory. To visit
# them use URLs like,
# http://localhost/somepage.html
# http://localhost/cgi-bin/somescript.py

webdir = '.'
port = 80

import os, sys
from BaseHTTPServer import HTTPServer
from CGIHTTPServer import CGIHTTPRequestHandler

print 'web directory "%s", port %s' % (webdir, port)

# Because Windows is brain dead ...
if sys.platform[:3] == 'win':
    CGIHTTPRequestHandler.have_popen2 = False
    CGIHTTPRequestHandler.have_popen3 = False
    sys.path.append('cgi-bin')

os.chdir(webdir)
serveraddr = ('',port)
server = HTTPServer( serveraddr, CGIHTTPRequestHandler)
server.serve_forever()