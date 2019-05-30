from itertools import cycle

def make_looper(s):
    g = cycle(s)
    return lambda: next(g)

class make_looper2(cycle):

    def __call__(self):
        return self.__next__()

def make_looper3(string):
    def generator():
        while True:
            for char in string:
                yield char
    return generator().next

make_looper4=lambda s,c=__import__("itertools").cycle: c(s).__next__

if __name__ == '__main__':
    abc = make_looper('abc')
    # abc2 = make_looper2('abc')
    # abc3 = make_looper3('abc')
    # abc4 = make_looper4('abc')
    print(abc())
    print(abc())
    print(abc())
    print(abc())
