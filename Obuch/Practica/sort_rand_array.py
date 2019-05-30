from random import randrange as rnd
i = 1
a = []
while i < 11:
    a.append(rnd(1, 10, 1))
    i = i + 1
print(a)    
n = len(a)
i = 1
while i < n:
    j = 1
    x = ''
    for j in range(1, n):
        if a[j] < a[j-1]:          
            a[j-1], a[j] = a[j], a[j-1]
            x = 'x'
    if x == 'x':
        print(a)
    else:
        i+=1    
       
