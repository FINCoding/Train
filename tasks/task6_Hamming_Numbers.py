from itertools import groupby

# def hamming(n):
#     if n == 1: return 1
#     i = 1
#     num = 1
#     while i < n:
#         num += 1
#         if (is_hamming(num)) == True: i += 1
#     return num
#
# def is_hamming(n):
#     while n % 2 == 0: n /= 2
#     while n % 3 == 0: n /= 3
#     while n % 5 == 0: n /= 5
#     return n == 1
#**********************
# def hamming_2(n):
#     if n == 1: return 1
#     lst = [1]
#     while len(lst) < n:
#         seq = get_sequence(lst)
#         # seq = get_sequence_mod(lst)
#         lst.append(next_hamm(lst,seq))
#     return lst[len(lst)-1]
#
# def next_hamm(lst, seq):
#     return min(seq)
#
# def get_sequence_mod(lst):
#     import threading
#     seq = []
#     t1 = threading.Thread(target=f, args=(2,lst,seq))
#     t2 = threading.Thread(target=f, args=(3,lst,seq))
#     t3 = threading.Thread(target=f, args=(5,lst,seq))
#     t1.daemon = True
#     t2.daemon = True
#     t3.daemon = True
#     t1.start(), t2.start(), t3.start()
#     return seq
#
# def f( n, lst, seq):
#     for i in lst:
#         if i * n not in lst: seq.append(i * n)
#
# def get_sequence(lst):
#     seq = []
#     for i in lst:
#         if i * 2 not in lst: seq.append(i * 2)
#         if i * 3 not in lst: seq.append(i * 3)
#         if i * 5 not in lst: seq.append(i * 5)
#     return seq
#**************************************
# def hamming_3(n):
#     if n == 1: return 1
#     lst = [1]
#     new_x = []
#     while len(lst) < n:
#         seq2 = get_sequence2(lst,2)
#         seq3 = get_sequence2(lst,3)
#         seq5 = get_sequence2(lst,5)
#         lst = lst + seq2 + seq3 + seq5
#         lst.sort()
#         new_x = [el for el, _ in groupby(lst)]
#     return lst[len(lst)-1]
#
# def modif_lst(lst, seq2, seq3, seq5):
#     for x, y, z in seq2, seq3, seq5:
#
#
# def get_sequence2(lst,n):
#     seq = []
#     for i in lst:
#         if i * n not in lst: seq.append(i * n)
#     return seq
#**************************************
def hamming4(n):
    if n == 1: return 1
    lst = [1]
    while len(lst) < n:
        seq = get_sequence4(lst)
        lst.append(next_hamm4(lst,seq))
    return lst[len(lst)-1]

def next_hamm4(lst, seq):
    return min(seq)

def get_sequence4(lst):
    seq = []
    lv2 = False
    lv3 = False
    lv5 = False
    for i in lst:
        if i * 2 not in lst and lv2 == False: seq.append(i * 2); lv2 = True
        if i * 3 not in lst and lv3 == False: seq.append(i * 3); lv3 = True
        if i * 5 not in lst and lv5 == False: seq.append(i * 5); lv5 = True
        if lv2 == True and lv3 == True and lv5 == True: break
    return seq
#*******************

def hamming5(n):
    if n == 1: return 1
    lst = [1]
    while len(lst) < n:
        seq = get_sequence5(n, lst)
        lst.append(next_hamm5(lst,seq))
    return lst[len(lst)-1]

def next_hamm5(lst, seq):
    return min(seq)

def get_sequence5(n, lst):
    seq = []
    lv2 = False
    lv3 = False
    lv5 = False
    if n > 3000:
        j = len(lst) // 2
    elif n > 2000:
        j = len(lst) // 2
    elif n > 1000:
        j = len(lst) // 2
    # elif n > 100:
    #     j = len(lst) // 3
    # elif n > 500:
    #     j = len(lst) // 2
    else:
        j = len(lst) // 5
    for i in range(j,len(lst),1):
        if lst[i] * 2 not in lst and lv2 == False: seq.append(lst[i] * 2); lv2 = True
        if lst[i] * 3 not in lst and lv3 == False: seq.append(lst[i] * 3); lv3 = True
        if lst[i] * 5 not in lst and lv5 == False: seq.append(lst[i] * 5); lv5 = True
        if lv2 == True and lv3 == True and lv5 == True: break
    return seq

def hamming_solution(n):
    bases = [2, 3, 5]
    expos = [0, 0, 0]
    hamms = [1]
    for _ in range(1, n):
        next_hamms = [bases[i] * hamms[expos[i]] for i in range(3)]
        next_hamm = min(next_hamms)
        hamms.append(next_hamm)
        for i in range(3):
            expos[i] += int(next_hamms[i] == next_hamm)
    return hamms[-1]

# We don't need to recalculate next_hamms on each iteration.
# Recalculating only the changed values results in some 35% performance improvement.
def hamming_solution2(n):
    bases = [2, 3, 5]
    expos = [0, 0, 0]
    hamms = [1]
    next_hamms = [2, 3, 5]
    for _ in range(1, n):
        next_hamm = min(next_hamms)
        hamms.append(next_hamm)
        for i in range(3):
            if next_hamms[i] == next_hamm:
                expos[i] += 1
                next_hamms[i] = bases[i] * hamms[expos[i]]
    return hamms[-1]

def hamming_solution3(n):
    num = [1]
    i, j, k = 0, 0, 0
    if n == 1:
      return 1
    else:
      for e in range(1, n):
        x = min(2*num[i], 3*num[j], 5*num[k])
        num.append(x)
        if 2*num[i] <= x: i += 1
        if 3*num[j] <= x: j += 1
        if 5*num[k] <= x: k += 1
    return num[len(num) - 1]

def hamming_solution4(n):
    bag = {1}
    for _ in range(n - 1):
        head = min(bag)
        bag.remove(head)
        bag |= {head*2, head*3, head*5}
    return min(bag)
########

def hamming_my(n):
    if n == 1: return 1
    lst = [1]
    i = 1
    min = 0
    while i < n:
        seq = get_sequence(lst, min)
        min = next_hamm(lst, seq)
        lst.append(min)
        i += 1
    return lst[len(lst) - 1]


def next_hamm(lst, seq):
    return min(seq)


def get_sequence(lst, min):
    seq = []
    for i in lst:
        if i * 2 > min: seq.append(i * 2)
        if i * 3 > min: seq.append(i * 3)
        if i * 5 > min: seq.append(i * 5)
    return seq

if __name__ == '__main__':
    import time
    # t1 = time.time()
    # print(hamming(1000))
    # print(time.time()-t1)
    # print(next_hamm([1,2,3]))
    # t1 = time.time()
    # print(hamming_2(5000))
    # print(time.time() - t1)
    # t1 = time.time()
    # print(hamming_3(10))
    # print(time.time() - t1)
    # t1 = time.time()
    # print(hamming4(2999)) ##2999 за 193.65199422836304 sec
    # print(time.time() - t1)
    # t1 = time.time()
    # print(hamming5(2999))
    # print(time.time() - t1) ##192.87666726112366 #192.2461130619049 #
    # t1 = time.time()
    # print(hamming_solution(5000))
    # print(time.time() - t1)
    #
    # t1 = time.time()
    # print(hamming_solution2(5000))
    # print(time.time() - t1) ##192.87666726112366 #192.2461130619049 #
    #
    # t1 = time.time()
    # print(hamming_solution3(5000))
    # print(time.time() - t1) ##192.87666726112366 #192.2461130619049 #

    t1 = time.time()
    print(hamming_solution4(6))
    print(time.time() - t1) ##192.87666726112366 #192.2461130619049 #

    t1 = time.time()
    print(hamming_my(5000))
    print(time.time() - t1) ##1