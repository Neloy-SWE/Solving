for i in range(int(input())):
    n,m,k,H = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    for i in a:
        if i != H:
            dif = abs(H-i)
            temp = dif/k
            tempInt = int(temp)
            if (dif<m*k and temp==tempInt):
                count+=1
    print(count)