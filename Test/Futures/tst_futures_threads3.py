import inspect
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, Future

class Task(Future):
    def __init__(self, gen):
        super().__init__()
        self._gen = gen

    def step(self, value=None, exc=None):
        try:
            if exc:
                fut = self._gen.throw(exc)
            else:
                fut = self._gen.send(value)
            fut.add_done_callback(self._wakeup)
        except StopIteration as exc:
            self.set_result(exc.value)

    def _wakeup(self, fut):
        try:
            result = fut.result()
            self.step(result, None)
        except Exception as exc:
            self.step(None, exc)

def start_inline_future(fut):
    t = Task(fut)
    t.step()
    return t

def run_inline_future(fut):
    t = start_inline_future(fut)
    return t.result()

def inlined_future(func):
    assert inspect.isgeneratorfunction(func)
    return func

def fib(n):
    return 1 if n <= 2 else (fib(n-1) + fib(n-2))

@inlined_future
def compute_fibs(n):
    result = []
    for i in range(n):
        val = yield from pool.submit(fib, i)
        result.append(val)
    return result

########
def run_inline_thread(gen):
    value = None
    exc = None
    while True:
        try:
            if exc:
                fut = gen.throw(exc)
            else:
                fut = gen.send(value)
            try:
                value = fut.result()
                exc = None
            except Exception as e:
                exc = e
        except StopIteration as exc:
            return exc.value
########

pool = ProcessPoolExecutor(4)
tpool = ThreadPoolExecutor(8)
t1 = tpool.submit(run_inline_thread(compute_fibs(3)))
t2 = tpool.submit(run_inline_thread(compute_fibs(3)))
result1 = t1.result()
result2 = t2.result()

# result = run_inline_future(compute_fibs(2))
# run_inline_future(compute_fibs(2))
# run_inline_future(compute_fibs(2))
