for i in range(int(input())):
    n = input()
    a = list(map(int, input().split()))
    b = sorted(a)
    sm = b[len(b)-2]
    m = max(a)
    for j in range(len(a)):
        if a[j]==m:
            print(m-sm, end=" ")
        else:
            print(a[j]-m, end=" ")
    print()