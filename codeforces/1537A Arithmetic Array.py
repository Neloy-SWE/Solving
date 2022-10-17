def calculateSum(a):
    sum = 0
    for i in a:
        sum+=i
    return sum

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    sum = calculateSum(a)

    if sum==n:
        print(0)
    elif sum>n:
        print(sum-n)
    else:
        print(1)