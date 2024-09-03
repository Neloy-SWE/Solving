for i in range(int(input())):
    n = int(input())
    a = []
    for j in range(n):
        s = input()
        a.append(s.index('#')+1)
    a.reverse()
    print(*a)