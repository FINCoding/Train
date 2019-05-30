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
    # yield 1 if n <= 2 else (fib(n - 1) + fib(n - 2))

@inlined_future
def compute_fibs(n):
    result = []
    for i in range(n):
        val = yield from pool.submit(fib, i)
        result.append(val)
    return result

pool = ProcessPoolExecutor(4)
#result = run_inline_future(compute_fibs(2))

t1 = start_inline_future(compute_fibs(2))
t2 = start_inline_future(compute_fibs(2))

# run_inline_future(compute_fibs(2))
# run_inline_future(compute_fibs(2))
