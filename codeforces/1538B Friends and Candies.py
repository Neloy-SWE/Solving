def avgList(a, n):
    sum = 0
    for i in a:
        sum+=i
    return sum/n

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    avg = avgList(a,n)
    if avg !=int(avg):
        print(-1)
    else:
        for j in a:
            if j>avg:
                count+=1
        print(count)