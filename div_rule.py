'''не рабочая хрень
'''

import math
def div_rul(m, l, r):
    if l == r: return m[l]
    n = math.ceil((l+r)/2)
    u = div_rul(m, l, n)
    v = div_rul(m, n+1, r)
    if u > v:
        return u
    else:
        return v

if __name__ == '__main__':
    import random
    list = []
    for i in range(random.randint(1, 10)):
        list.append(random.randint(1, 10))
    el = len(list)
    div_rul(list, 0, el)

