for i in range(int(input())):
    s = input()
    a = list(map(int, input().split()))
    intdex1 = 0
    lastIndex1 = 0
    for j in range(int(s)):
        if a[j]==1:
            intdex1=j
            break
    for j in range(int(s)-1,0,-1):
        if a[j]==1:
            lastIndex1=j
            break

    a=a[intdex1:lastIndex1+1]
    count = 0
    for j in a:
        if j==0:
            count+=1
    print(count)