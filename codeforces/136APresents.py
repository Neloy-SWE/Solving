num1 = int(input())

a = list(map(int, input().split()))

for i in range (1, num1+1):
    for j in range (num1):
        if a[j]==i:
            print(j+1,end=" ")