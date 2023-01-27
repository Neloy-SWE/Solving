def countV (a,b):
    count=0
    for i in range(len(a)):
        if a[i]==b:
            count+=1
    return count

for i in range(int(input())):
    a = int(input())
    b =[]
    v1 = []
    vMin = 0
    for j in range(a):
        c = list(map(int, input().split()))
        v1.append(c[0])
        b.append(c)
    vSetList = list(set(v1))
    v11 = countV(v1, vSetList[0])
    v12 = countV(v1, vSetList[1])
    if (a-v11)==1:
        print(vSetList[0], vSetList[1], end=" ")
        vMin = vSetList[1]
    else:
        print(vSetList[1], vSetList[0], end=" ")
        vMin = vSetList[0]
    v=[]
    e = 1
    while(e<a-1):
        for k in range(a):
            v.append(b[k][e])
        for l in range(len(v)):
            if v[l] !=vMin:
                print(v[l], end=" ")
                vMin = v[l]
                break
        v=[]
        e+=1
    print()