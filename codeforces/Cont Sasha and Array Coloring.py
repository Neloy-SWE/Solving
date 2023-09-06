for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    value = 0
    while(len(a)>1):
        value+=abs(a[0]-a[len(a)-1])
        a.pop(0)
        a.pop(len(a)-1)
    print(value)