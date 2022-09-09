for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    countEven= 0
    countOdd = 0
    for j in range(len(a)):
        if a[j]%2==0:
            countEven+=1
        else:
            countOdd +=1
    if countEven>0 and countOdd>0:
            print("YES")
    elif sum(a)%2==1:
        print("YES")
    else:
        print("NO")