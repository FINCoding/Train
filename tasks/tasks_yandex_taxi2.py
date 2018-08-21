inputData = open('input.txt')
con_arriv = 'arrival'
con_depar = 'departure'
arrivDepart = {}
onDay = int(input('input which day...'))

def fill_dict(sign, key, value):
    if sign  == con_arriv:
        try:
            arrivDepart[key] += int(value)
        except:
            arrivDepart[key] = int(value)
    else:
        try:
            arrivDepart[key] -= int(value)
        except:
            arrivDepart[key] = (-1) * int(value)

def calc(day):
    sum = 0
    for i in sorted(arrivDepart.keys()):
        if i > day: break
        sum += arrivDepart[i]
    return sum

for line in inputData:
    spl = line.split(None)
    fill_dict(spl[0], spl[1], spl[2])

k = 0
maxM = 0
MaxK = 0
lsum = 0
for k in sorted(arrivDepart.keys()):
    if int(k) > onDay: break
    lsum = calc(k)
    if int(k)%2 !=0:
        if lsum > maxM:
            maxM = lsum
    else:
        if lsum > MaxK:
            MaxK = lsum

print(maxM)
print(MaxK)
print(arrivDepart)

