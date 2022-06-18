for i in range(int(input())):
    a, b, c, d = map(int, input().split())
    winAB = max(a,b)
    loseAB = min(a,b)
    winCD = max(c,d)
    loseCD = min(c,d)
    if winAB>loseCD and winCD>loseAB:
        print("YES")
    else:
        print("NO")