import dis
def a():
    x = [1,2,3,4,5]
    y = x[2]

def b():
    x = (1,2,3,4,5)
    y = x[2]

dis.dis(a)
print('_' * 100)
dis.dis(b)
