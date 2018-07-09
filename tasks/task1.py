N = [1,2,3,4,5,6]
S = ['+', '-', '*', '/']

def f(ln, dict):
    ldict = dict
    lln = ln
    if ln == len(N) - 1:
        res=''
        ldict[N[ln]] = ''
        for b in ldict:
            res += '%d%s' % (b,dict[b])
        if eval(res) == 100:
            print(res)
    else:
        for i in S:
            dict[N[ln]] = i
            if ln < len(N):
                lln += 1
            f(ln=lln, dict=dict)
            lln = ln
        # lln = ln

def f_test(ln, dict):
    # ldict = []
    ldict = dict.copy()
    lln = ln
    if ln == len(N) - 1:
        res=''
        ldict[N[ln]] = ''
        for b in ldict:
            res += '%d%s' % (b,ldict[b])
        print(res)
    else:
        for i in S:
            dict[N[ln]] = i
            if ln < len(N):
                lln += 1
            f_test(ln=lln, dict=dict)
            lln = ln
        # lln = ln


dict={}

ln = 0
f(ln, dict)
# f_test(ln, dict)



