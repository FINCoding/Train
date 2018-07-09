def f(lst=None):
    lst.append(len(lst))
    # print (lst)

x = []

f(x)
f(x)
print(x)
f(x)
print(x)