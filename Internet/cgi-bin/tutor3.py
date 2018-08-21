#!/usr/bin/python
import cgi
form = cgi.FieldStorage()
print('Content-type: text/html')

html = '''
<TITLE>tutor3.py</TITLE>
<HR>
<P>%s</P>
<HR>
'''
if not 'user' in form:
    print(html % 'Who are you')
else:
    print(html % ('Hello, %s' % form['user'].value))