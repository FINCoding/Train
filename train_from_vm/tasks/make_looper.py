def make_looper(string):
    def myfunc():
        return looper.loop(string)
    return myfunc

class looper:
    i = 0
    cl_string = ''
    def loop(string):
        if string != looper.cl_string: looper.i = 0; looper.cl_string = string
        k = looper.i
        if looper.i == len(string)-1: looper.i = 0
        else: looper.i += 1
        return string[k]

def func_you( lambdafunc1, lambdafunc2, lambdafunc3, lambdafunc4):
    return lambda x: lambdafunc1(x) * lambdafunc2(x) * lambdafunc3(x) * lambdafunc4(x)



if __name__ == '__main__':
    abc = make_looper('abc')
    print(abc())
    print(abc())
    print(abc())
    print(abc())
    abc = make_looper('defg')
    print(abc())
    # abc()
    # f = func_you(sum, min, max, sum)
    # f=([1,2])
