def func1 (A, B):
    def func2 (x, y, z):
         print (x, y, 'and', z)
    if A == 'key':
        return func2(*B)

func1('key', ('a', 'b', 'c'))