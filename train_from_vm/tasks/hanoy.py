def hanoy(n,fromP,toP,withP):
    if n == 0: return
    hanoy(n-1,fromP,withP,toP)
    print('Move disk %d from' % n, fromP, toP)
    hanoy(n-1,withP,toP,fromP)

if __name__ == '__main__':
    hanoy(4,1,3,2)