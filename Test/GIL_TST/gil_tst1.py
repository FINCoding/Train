import time
import threading

def countdown(n):
    while n > 0:
        n -= 1

t1 = time.time()
count = 1000000
countdown(count)
# countdown(count)
print('Sequential', time.time()-t1)

t1 = time.time()
th1 = threading.Thread(target=countdown, args = (count//2,) )
th2 = threading.Thread(target=countdown, args = (count//2,) )
th1.start(); th2.start()
th1.join(); th2.join()
print('Threaded', time.time()-t1)
