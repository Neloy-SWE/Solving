for i in range(int(input())):
    n = input()
    a =list(map(int, input().split()))
    count = 0
    i=1
    while(i<len(a)):
        maxA = max(a[i-1], a[i])
        minA = min(a[i-1], a[i])
        while(maxA/minA>2):
            minA*=2
            count+=1
        i+=1
    print(count)