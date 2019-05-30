n = int(input('ВВедите число n: '))
m = int(input('\n''ВВедите число m: '))
A = []
for i in range(1, n+1):
    A.append(i)
while len(A) >= m:
    print (len(A))
    del A[m-1]
print(A)    
