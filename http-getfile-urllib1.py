import sys
from urllib.request import urlopen
showline = 6
addr = 'learning-python.com'
try:
    servername, filename = sys.argv[1:]
except:
    servername, filename = 'yandex.ru', '/index.tmpl'

remoteaddr = 'http://%s%s' % (servername, filename)
print(remoteaddr)
remotefile = urlopen(remoteaddr)
remotedata = remotefile.readlines()
remotefile.close()
for line in remotedata[:showline]: print(line)