for i in range(int(input())):
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    maxC = max(c)
    sumMaxC = (maxC*(maxC+1))//2
    sumC = sum(c)
    p=sumMaxC-sumC
    if p==b:
        print("YES")
    elif p<b:
        difPB = b-p
        flag=True
        while(flag):
            maxC+=1
            difPB-=maxC
            if difPB==0:
                print("YES")
                break
            elif difPB>0:
                continue
            else:
                print("NO")
                break
    else:
        print("NO")