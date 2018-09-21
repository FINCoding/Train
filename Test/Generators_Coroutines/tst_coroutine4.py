def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start

@coroutine
def grep(pattern):
    print("Looking for %s" % pattern)
    try:
        while True:
            line = (yield)
            if pattern in line:
                print(line)
    except GeneratorExit:
        print('Finish')


g = grep("python")
g.send("A series of tubes")
g.send("Hello world")
g.send("python generators rock!")

