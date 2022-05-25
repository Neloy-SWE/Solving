num1 = int(input())
for i in range(num1):
    count=0
    n = int(input())
    a = list(map(int, input().split()))
    i=1
    while(i<n):
        if a[i-1]>a[i]:
            count+=1
            i+=1
        i+=1
    print(count)
