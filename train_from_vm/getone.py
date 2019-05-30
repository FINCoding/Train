#!/usr/local/bin/python

import os, sys
from getpass import getpass
from ftplib import FTP

nonpassive = False
filename = '13'
dirname = ''
sitename = 'localhost'
# userinfo = ('User', getpass('Pswd?'))
if len(sys.argv) > 1: filename = sys.argv[1]

print('Connecting...')
connection = FTP(sitename)
# connection.login(*userinfo)
connection.cwd(dirname)
if nonpassive:
    connection.set_pasv(False)

print('Downloading...')
localfile = open(filename, 'wb')
connection.retrbinary('RETR ' + filename, localfile.write, 1024)
connection.quit()
localfile.close()

# if input('Open file?') in ['Y', 'y']:
#     from playfile import playfile
#     playfile(filename)
