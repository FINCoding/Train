def divider(n):
    i =2
    j = 0
    a = []
    while i**2 <= n and j != 1:
        if n%i == 0:
            j = 1
        i += 1
    if j == 1:
        print("Это составное число")
    else:
        print("Это простое число")

n = int(input('введите число...'))
divider(n)