##isn't solved
def last_digit(lst):
    if not lst: return 1
    ln = len(lst)-1
    for i in range(ln, 0, -1):
        a = degree(lst[i-1], lst[i])
        if a > 9:
            if a%10 != 0: lst[i-1] = a%10
            else: lst[i-1] = 10
        else: lst[i-1] = a
    return lst[0]

def degree(a,b):
    return a**b

if __name__ == '__main__':
    # ([], 1),
    # ([0, 0], 1),
    # ([0, 0, 0], 0),
    # ([1, 2], 1),
    # ([3, 4, 5], 1),
    # ([4, 3, 6], 4),
    # ([7, 6, 21], 1),
    # ([12, 30, 21], 6),
    # ([2, 2, 2, 0], 4),
    # ([937640, 767456, 981242], 0),
    # ([123232, 694022, 140249], 6),
    # ([499942, 898102, 846073], 6)
    lst = [7,6,21]
    print(last_digit(lst))

