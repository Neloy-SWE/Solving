for i in range(int(input())):
    k = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    minA = min(a)
    minB = min(b)
    count = 0
    for i in range(k):
        count+=max((a[i]-minA), (b[i]-minB))
    print(count)