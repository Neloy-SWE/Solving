t = int(input())
for i in range(t):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    count=0
    for j in range(1,n):
        if(abs(a[j-1]-a[j])<=1):
            count+=1
    if(count==n-1):
        print("YES")
    else:
        print("NO")
