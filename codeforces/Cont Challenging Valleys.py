for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    ans = "YES"
    for j in range(n-1):
        if a[j]<a[j+1]:
            count=1
        elif a[j]>a[j+1] and count>0:
            ans = "NO"
            break
    print(ans)