num1 = int(input())
for i in range(num1):
    count=0
    flag =0
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if i%2!=a[i]%2:
            if (i%2==0):
                count+=1
            else:
                flag+=1
    if count == flag:
        print(count)
    else:
        print("-1")         

