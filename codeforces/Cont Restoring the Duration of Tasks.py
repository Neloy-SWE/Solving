num1 = int(input())
for i in range(num1):
    k = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    if k==1:
        c.append(abs(a[0]-b[0]))
    else:
        for i in range(k):
            if i==0:
                c.append(abs(a[i]-b[i]))
            else:
                maxab = max(a[i], b[i-1])
                c.append(abs(maxab-b[i]))
    print(*c)