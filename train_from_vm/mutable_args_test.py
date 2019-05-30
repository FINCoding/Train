def f(val,a=None):
    if a is None:
        a = []
    print('before ', a)
    a.append(val)
    print(a)

f(1)
f(2)
f(3)