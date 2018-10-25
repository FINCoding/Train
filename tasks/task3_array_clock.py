# array = [[1,  2,  3,  4,  5],
#          [6,  7,  8,  9,  10],
#          [11, 12, 13, 14, 15],
#          [16, 17, 18, 19, 20],
#          [21, 22, 23, 24, 25]]

array = [[1, 2, 3, 4, 5, 6],
         [20, 21, 22, 23, 24, 7],
         [19, 32, 33, 34, 25, 8],
         [18, 31, 36, 35, 26, 9],
         [17, 30, 29, 28, 27, 10],
         [16, 15, 14, 13, 12, 11]]

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]

# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]

def snail(array):
    list = []
    if not array: return [[]]
    while True:
        l = len(array)
        forw_direct(array[0], list)
        if l > 2: last_elem(array[1:l-1], list)
        if l > 1: ret_direct(array[l-1], list)
        if l > 2: first_elem(array[1:l-1], list)
        cut_arr(array)
        if not array: return list

def forw_direct(array, list):
    for i in array:
        list.append(i)

def ret_direct(array, list):
    for i in range(len(array),0,-1):
        list.append(array[i-1])

def first_elem(array, list):
    for i in range(len(array),0,-1):
        list.append(array[i-1][0])

def last_elem(array, list):
    for ar in array:
        list.append(ar[len(ar)-1])

def cut_arr(array):
    del array[0]
    if len(array) > 1: del array[len(array)-1]
    for ar in array:
        del ar[0], ar[len(ar)-1]

if __name__ == "__main__":
    print(snail(array))