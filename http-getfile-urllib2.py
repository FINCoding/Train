import sys, os, urllib.request, urllib.parse
from PP4E.Internet.Email.html2text import *
import sys, tkinter
showlines = 10
addr = 'learning-python.com'
try:
    servername, filename = sys.argv[1:3]
except:
    servername, filename = addr, '/index.html'

remoteaddr = 'http://%s%s' % (servername, filename)
if len(sys.argv) == 4:
    localname = sys.argv[3]
else:
    (scheme, server, path, parmsm, query, frag) = urllib.parse.urlparse(remoteaddr)
    localname = os.path.split(path)[1]

print(remoteaddr, localname)
urllib.request.urlretrieve(remoteaddr, localname)
text = open(localname, 'rb').read()
# remotedata = open(localname, 'rb').readlines()
text = html2text(text)
t = tkinter.Text()
t.insert('1.0', text)
t.pack()
t.mainloop()
# for line in remotedata[:showlines]:
#     print(line)


