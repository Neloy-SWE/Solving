for i in range(int(input())):
    n, m = map(int, input().split())
    length = list(map(int, input().split()))
    if(sum(length)<=m):
        print(0)
    else:
        print(sum(length)-m)