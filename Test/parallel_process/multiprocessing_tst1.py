import multiprocessing as mp
import time

count = 1000000

def countdown(n, tp):
    while n > 0:
        n -= 1
    print(tp)

t1 = time.time()

p1 = mp.Process(target=countdown, args=(count//2, 'mp',))
p2 = mp.Process(target=countdown, args=(count//2, 'mp',))
p1.start(); p2.start()
print('mp', time.time()-t1)

t1 = time.time()
countdown(count, 'Sequential')
print('Sequential', time.time()-t1)
