for i in range(int(input())):
    k = int(input())
    a = list(map(int, input().split()))
    oneG = a.count(1)
    twoG = a.count(2)
    if oneG>0:
        if oneG%2==0:
            print("YES")
        else:
            print("NO")
    else:
        if twoG%2==0:
            print("YES")
        else:
            print("NO")