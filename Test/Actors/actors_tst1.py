import threading
from queue import Queue

_registry = {}

def send(name, msg):
    _registry[name].send(msg)

def actor(func):
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        _registry[func.__name__] = gen
    return wrapper

@actor
def printer():
    while True:
        msg = yield
        print('printer:', msg)

# printer()
# n = 10
# while n > 0:
#     send('printer', n)
#     n -= 1

###########
@actor
def ping():
    while True:
        n = yield
        print("ping %d" % n)
        send('pong', n+1)

@actor
def pong():
    while True:
        n = yield
        print("pong %d" % n)
        send('ping', n+1)

ping()
pong()
send('ping', 0)

####################2
class Actor(threading.Thread):
    def __init__(self, gen):
        super().__init__()
        self.deamon = True
        self.gen = gen
        self.mailbox = Queue()
        self.start()

    def send(self, msg):
        self.mailbox.put(msg)

    def run(self):
        while True:
            msg = self.mailbox.get()
            self.gen.send(msg)

############3




