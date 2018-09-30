from concurrent.futures import ThreadPoolExecutor
import time

def func(x, y):
    import time
    time.sleep(2)
    return x+y

pool = ThreadPoolExecutor(max_workers = 8)
def run():
    fut = pool.submit(func, 2, 3)
    # fut = pool.submit(func, 2, 'Hello')
    fut.add_done_callback(result_handler)

def result_handler(fut):
    try:
        result = fut.result()
        print('Got:', result)
    except Exception as e:
        print('Failed: %s: %s' % (type(e).__name__, e))
###########2
class Task:
    def __init__(self, gen):
        self._gen = gen

    def step(self, value=None, exc=None):
        try:
            if exc:
                fut = self._gen.throw(exc)
            else:
                fut = self._gen.send(value)
            fut.add_done_callback(self._wakeup)
        except StopIteration as exc:
            pass

    def _wakeup(self, fut):
        try:
            result = fut.result()
            self.step(result, None)
        except Exception as exc:
            self.step(None, exc)

def do_func(x, y):
    result = yield pool.submit(func, x, y)
    print('Got:', result)

#######3
def after(delay, gen):
    yield pool.submit(time.sleep, delay)
    yield from gen

#######
if __name__ == '__main__':
    # run() #1
    # t = Task(do_func(2, 3)) #2
    # t.step()
    Task(after(1, do_func(2, 3))).step()