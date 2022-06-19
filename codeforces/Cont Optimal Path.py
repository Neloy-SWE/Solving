for i in range(int(input())):
    n, m = map(int, input().split())
    if min(n,m)==1:
        maxNM = max(n,m)
        maxNM = (maxNM*(maxNM+1))//2
        print(maxNM)
    else:
        totalN = (m*(m+1))//2
        # print(totalN)
        totalM = (m*n*(n+1))//2
        # print(totalM)
        ans = (totalM+totalN)-m
        print(ans)