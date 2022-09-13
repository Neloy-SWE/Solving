def getMin(a):
    value = a[0]

    for i in a:
        if value>i:
            value=i
    return value

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    minA = getMin(a)
    count=0
    for j in a:
        count+=(j-minA)
    print(count)
