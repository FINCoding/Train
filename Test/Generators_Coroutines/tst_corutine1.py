def countdown(n):
    while n > 0:
        yield n
        n -= 1

[print(i) for i in countdown(10)]
x = countdown(10)
print(x)
