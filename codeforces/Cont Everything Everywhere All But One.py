num1 = int(input())
for i in range(num1):
    count=0
    n = int(input())
    a = list(map(int, input().split()))
    b = sum(a)/n
    for j in range(n):
        if a[j]==b:
           count+=1
    if count>0:
        print("YES")
    else:
        print("NO")
        