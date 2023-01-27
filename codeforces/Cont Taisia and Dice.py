for i in range(int(input())):
    n, s, r = map(int, input().split())
    rm = r%(n-1)
    m = r//(n-1)
    print(s-r, end=" ")
    for i in range(n-1):
        if rm>0:
            print(m+1, end=" ")
            rm-=1
        else:
            print(m, end=" ")
    print()