
def change_lst(a, b, lst,sz):
    try:
        while lst[a] != a: a = lst[lst[a]]
        while lst[b] != b: b = lst[lst[b]]
        if a != b:
            if sz[a] < sz[b]:
                lst[a] = b
                sz[b] += sz[a]
            else:
                lst[b] = a
                sz[a] += sz[b]
        # print(lst)
    except EOFError:
        pass
    print(lst)

def main_tst():
    sz = [1 for i in range(20)]
    lst = [i for i in range(20)]
    for i in range(0,len(lst)-1, 2):
        change_lst(i, i+1, lst, sz)
    print('1')
    for i in range(1, len(lst) - 1, 4):
        change_lst(i, i + 2, lst, sz)
    print('2')
    try:
        for i in range(3, len(lst) - 1, 4):
            change_lst(i, i + 4, lst, sz)
    except IndexError:
        pass
    print('3')

def main_tst2():
    sz = [1 for i in range(20)]
    lst = [i for i in range(20)]

if __name__ == '__main__':
    main_tst()