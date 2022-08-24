a, b = map(int, input().split())
if b<4:
    print("YES")
else:
    count=0
    isPrime = False
    for i in range(a+1, b+1):
        for j in range(2, i):
            if (i%j==0):
                isPrime=False
                break
            else:
                isPrime=True
        if isPrime:
            count=i
            break
        else:
            continue
    if count==b:
        print("YES")
    else:
        print("NO")