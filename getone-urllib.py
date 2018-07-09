#!/usr/local/bin/python

import os, getpass
from urllib.request import urlopen

filename = '1.html'
# password = getpass.getpass('Pswd?')

remoteaddr = 'https://yandex.ru/'
print('Downloading', remoteaddr)

remotefile = urlopen(remoteaddr)
localfile = open(filename, 'wb')
localfile.write(remotefile.read())
localfile.close()
remotefile.close()