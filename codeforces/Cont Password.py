for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    m = 10-n
    print((m*(m-1))*3)