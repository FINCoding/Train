def generator():
    item = yield
    value = item
    yield value



if __name__ == '__main__':
    g = generator()
    next(g)
    value = g.send('a')
    print(value)