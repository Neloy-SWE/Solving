for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    aFinal = []

    for i in range(n):
        if(i % 2 == 0):
            aFinal.append(a[0])
            a.pop(0)
        else:
            aFinal.append(a[len(a)-1])
            a.pop(len(a)-1)

    print(*aFinal)
