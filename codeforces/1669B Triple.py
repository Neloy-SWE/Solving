for i in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    flag = -1
    for i in range(n-2):
        if a[i]==a[i+1] and a[i+1]==a[i+2]:
            flag=a[i]
            break
    print(flag)