for i in range(int(input())):
    n, m, x = map(int, input().split())
    row = x%n
    if row == 0:
        row = n
    col = (x+n-1)//n
    print(((row-1)*m)+col)