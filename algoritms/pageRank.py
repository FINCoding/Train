inputDict = {
    'A': {'I':('B', 'C'), 'O':('B', 'C', 'D')},
    'B': {'I':('A', 'C', 'D'), 'O':('A', 'C')},
    'C': {'I':('A', 'B'), 'O':{'A', 'B'}},
    'D': {'I':('A'), 'O':{'B'}},
}
constKeyI = 'I'
constKeyO = 'O'
# inputDict = {
#     'Amzn': {'I':('Medm', 'Fb'), 'O':('Twtr', 'Medm')},
#     'Medm': {'I':('Amzn', 'Twtr'), 'O':('Amzn', 'Fb', 'Twtr', 'Mspc')},
#     'Mspc': {'I':('Medm',), 'O':{'Twtr',}},
#     'Fb': {'I':('Medm',), 'O':{'Amzn', 'Twtr'}},
#     'Twtr': {'I':('Amzn', 'Fb', 'Medm', 'Mspc'), 'O':{'Medm',}},
# }
def pageRank(inputDict=None):
    d = 0.85
    N = 1
    N = getCountElemOfDict(inputDict)
    rp = (1-d)/N
    me = 0.09
    firstCoeff = setFirstCoeff(inputDict, N)
    coeff = main(firstCoeff, d, N, rp, me)
    print(rp)
    print(firstCoeff)
    print(coeff)

def main(coeff, d, N, rp, me):
    conditionTrue = ''
    while True:
    #     pass
        new_coeff = changeCoeff(inputDict, coeff, d, N, rp)
        conditionTrue = checkRuleIsTrue(new_coeff, coeff, me)
        if conditionTrue:
            return new_coeff
        else:
            coeff = new_coeff

def changeCoeff(iDict, coeff, d, N, rp):
    newCoeff = {}
    for i in coeff.keys():
        inputList = iDict[i][constKeyI]
        resultExprInBrackets = calcExprInBrackets(inputList, coeff)
        newCoeff[i] = rp + d * (resultExprInBrackets)
    return newCoeff

def checkRuleIsTrue(new_coeff, coeff, me):
    for i in new_coeff.keys():
        if abs(new_coeff[i] - coeff[i]) > me: return False
    return True

def calcExprInBrackets(iList, coeff):
    sum = 0
    for j in iList:
        list = getList(j)
        countOfList = getCountElemOfList(list)
        sum += coeff[j] / countOfList
    return sum

def getList(key):
    return inputDict[key][constKeyO]

def getCountElemOfList(iList):
    count = 0
    for i in iList:
        count += 1
    if count == 0: count = 1
    return count

def setFirstCoeff(iDict, N):
    coef = {}
    for i in iDict.keys():
        coef[i] = 1/N
    return coef


def getCountElemOfDict(iDict):
    count = 0
    for i in iDict.keys():
        count += 1
    if count == 0: count = 1
    return count

pageRank(inputDict)