for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    minA = min(a)
    count=0
    for i in a:
        if i!=minA:
            count+=1
    print(count)