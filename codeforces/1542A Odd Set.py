for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    countOdd = 0
    countEven = 0
    for i in a:
        if i%2==0:
            countEven+=1
        else:
            countOdd+=1
    if countOdd==countEven:
        print("YES")
    else:
        print("NO")