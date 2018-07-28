import sys, os, urllib.request, urllib.parse
showlines = 6
addr = 'learning-python.com'
try:
    servername, filename = sys.argv[1:3]
except:
    servername, filename = 'yandex.ru', '/index.html'

remoteaddr = 'http://%s%s' % (servername, filename)
if len(sys.argv) == 4:
    localname = sys.argv[3]
else:
    (scheme, server, path, parmsm, query, frag) = urllib.parse.urlparse(remoteaddr)
    localname = os.path.split(path)[1]

print(remoteaddr, localname)
urllib.request.urlretrieve(remoteaddr, localname)
remotedata = open(localname, 'rb').readlines()
for line in remotedata[:showlines]: print(line)


