import smtplib, sys, email.utils, mailconfig

mailserver = mailconfig.smtpservername

From = input('From? ').strip()
To = input('To? ').strip()
Tos = To.split(';')
Subj = input('Subj? ').strip()
Date = email.utils.formatdate()

text = ('From: %s\nTo: %s\nDate: %s\nSubject: %s\n\n' % (
    From, To, Date, Subj))
print('haha')
# while True:
#     line = sys.stdin.readline()
#     if not line:
#         break
#     text += line
text += 'Hello World!'
print('Connecting...')
server = smtplib.SMTP(mailserver)
failed = server.sendmail(From, Tos, text)
server.quit()
if failed:
    print('Failed ', failed)
else:
    print('No errors')
print('Bye')
