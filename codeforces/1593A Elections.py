def getMax(a):
    maxValue = a[0]
    for i in a:
        if i>maxValue:
            maxValue = i
    return maxValue

for i in range(int(input())):
    a, b, c = map(int, input().split())
    print(getMax([a,b+1,c+1])-a, getMax([a+1,b,c+1])-b, getMax([a+1,b+1,c])-c)