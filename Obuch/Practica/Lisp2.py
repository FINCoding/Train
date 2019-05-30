from random import randrange as rnd
a = [rnd(10) for x in range(15)]
print (a)
a = [x for x in a if x != 0]
print (a)
