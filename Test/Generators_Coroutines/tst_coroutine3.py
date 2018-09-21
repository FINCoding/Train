import time

def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start

def follow(thefile, target):
    thefile.seek(0,2) # Go to the end of the file
    # print(thefile.readline())
    # [print(row) for row in thefile]
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1) # Sleep briefly
            continue
        target.send(line)

@coroutine
def printer():
    while True:
        line = (yield)
        print(line)

f = open('log.txt')
# print(f.readline())
follow(f, printer())