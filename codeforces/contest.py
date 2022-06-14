for i in range(int(input())):
    a = []
    for n in range(9):
        a.append(input())
    a1 = 0
    b1 = 0
    for j in range(2,8):
        b = list(a[j])
        if b.count("#")==1 and b.index("#")!=0:
            a1=j
            b1 = b.index("#")
            break
    print(a1, b1+1)
