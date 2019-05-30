n = 10

def main():
    lst = [i for i in range(10)]
    a = ''
    try:
        while True:
            a, b = map(int, input('Введите два числа через пробел...').split())
            t = lst[a]
            if t == lst[b]: continue
            for i in range(len(lst)):
                if lst[i] == t: lst[i] = lst[b]
    except EOFError:
        pass
    print(lst)

if __name__ == '__main__':
    main()