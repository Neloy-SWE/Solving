for i in range(int(input())):
    a, b, c, n = map(int, input().split())
    allMax = max(a,b,c)
    a1=allMax-a
    b1=allMax-b
    c1=allMax-c
    all = (a1+b1+c1)
    n=n-all
    if n==0:
        print("YES")
    elif n>0 and n%3==0:
        print("YES")
    else:
        print("NO")