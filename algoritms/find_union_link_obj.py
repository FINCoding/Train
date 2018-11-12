n = 10

def main():
    lst = [i for i in range(10)]
    a = ''
    try:
        while True:
            a, b = map(int, input('Введите два числа через пробел...').split())
            while lst[a] != a: a = lst[a]
            while lst[b] != b: b = lst[b]
            if a == b: continue
            lst[a] = b
            print(lst)
    except EOFError:
        pass
    print(lst)

if __name__ == '__main__':
    main()