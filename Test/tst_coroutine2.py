def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.next()
        return cr
    return start

@coroutine
def gen(num):
    for i in range(num):
        i = yield
        print(i)


gen(3)
