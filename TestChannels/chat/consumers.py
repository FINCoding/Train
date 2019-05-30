import json
import time

from channels.channel import Group
from django.core.mail import send_mail

def ws_connect(message):
    Group('chat').add(message.reply_channel)
def ws_message(message):
    Group('chat').send({'text': json.dumps({'message': message.content['text'],
                                            'sender': message.reply_channel.name})})
def ws_disconnect(message):
    Group('chat').discard(message.reply_channel)

def send_email_consumer(message):
    time.sleep(30)
    payload = message.content['payload']
    send_mail(payload['subject'], payload['body'], 'root@localhost', [payload['email']],
              fail_silently=False)