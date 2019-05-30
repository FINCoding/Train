n = 10

def main():
    sz = [1 for i in range(10)]
    lst = [i for i in range(10)]
    a = ''
    try:
        while True:
            a, b = map(int, input('Введите два числа через пробел...').split())
            while lst[a] != a: a = lst[lst[a]]
            while lst[b] != b: b = lst[lst[b]]
            if a == b: continue
            if sz[a] < sz[b]:
                lst[a] = b
                sz[b] += sz[a]
            else:
                lst[b] = a
                sz[a] += sz[b]
            print(lst)
    except EOFError:
        pass
    print(lst)

if __name__ == '__main__':
    main()