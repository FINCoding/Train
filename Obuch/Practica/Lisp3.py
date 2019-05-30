from random import randrange as rnd
a = [rnd(10) for x in range(12)]
print(a)
s = 0
for x in range(len(a)):
    s += a[x]
print(s)
