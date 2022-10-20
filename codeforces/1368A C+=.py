def getMin (a, b):
    if a<b:
        return a
    else:
        return b

def getMax (a, b):
    if a>b:
        return a
    else:
        return b

for i in range(int(input())):
    a, b, c = map(int, input().split())
    count = 0
    maxValue = getMax(a,b)
    minValue = getMin(a,b)
    while minValue<=c and maxValue<=c:
        minValue+=maxValue
        temp = minValue
        minValue = maxValue
        maxValue = temp
        count+=1
    print(count)