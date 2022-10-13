for i in range(int(input())):
    a, b, c = map(int, input().split())

    sum = a+b+c
    maxAll = max(a,b,c)
    if (sum-maxAll==maxAll):
        print("YES")
    else:
        print("NO")