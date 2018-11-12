def expr(x,y):
    return x/y
f  = expr
with f(0,2) as a :
    print(2/0)

print('Hello')
