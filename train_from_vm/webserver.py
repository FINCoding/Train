import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'
print(webdir)
port = 9002

if len(sys.argv) > 1: webdir = sys.argv[1]
if len(sys.argv) > 2: port = int(sys.argv[2])
print('webdir "%s", port %s' % (webdir, port))
os.chdir(webdir)
srvraddr = ('172.30.0.142', port)
srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()