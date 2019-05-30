def insertion_sort(arrayToSort):
    a = arrayToSort
    for i in range(len(a)):
        v = a[i]
        j = i
        while (a[j-1] > v) and (j > 0):
            a[j] = a[j-1]
            j = j - 1
        a[j] = v
        print(a)
    return a

# ary = [54,1,2,3,52,3,1,2,3,5,3,67,3,2,543]
ary = [54,3,2,1,52]
print(insertion_sort(ary))