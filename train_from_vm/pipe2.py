import os, time

def child(pipeout):
    zzz = 0
    i = 0
    while i in range(5):
        time.sleep(zzz)
        msg = ('Spam %03d' % zzz).encode()
        os.write(pipeout, msg)
        zzz = (zzz+1) % 3
        i+=1

def parent():
    i = 0
    pipein,pipeout = os.pipe()
    if os.fork() == 0:
        os.close(pipein)
        child(pipeout)
        i+=1
    else:
        os.close(pipeout)
        pipein = os.fdopen(pipein)
        print(pipein.readline())
        print(pipein)
        # while True:
        #     line = (pipein.readline())[:-1]
        #     print(pipein.readline())
        #     print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))

parent()