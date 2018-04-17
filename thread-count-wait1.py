import _thread as thread
stdoutmutex = thread.allocate_lock()
exitmutex = [thread.allocate_lock() for i in range(10)]

def counter(myId, count):
    for i in range(count):
        stdoutmutex.acquire()
        print('[%s] => %s' % (myId, i))
        stdoutmutex.release()
    exitmutex[myId].acquire()

for i in range(10):
    thread.start_new_thread(counter,(i,3))

for mutex in exitmutex:
    while not mutex.locked(): pass
print('Main thread exiting.')