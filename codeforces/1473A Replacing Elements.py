def max1(a):
    value = a[0]
    for i in a:
        if value<i:
            value = i
    return value
for i in range(int(input())):
    n, d = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    if max1(a) <=d:
        print("YES")
    elif a[0]+a[1]<=d:
        print("YES")
    else:
        print("NO")