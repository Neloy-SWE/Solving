for i in range(int(input())):
    a = []
    for n in range(9):
        a.append(list(input()))
    a1 = 0
    b1 = 0
    for j in range(2,8):
        c1 = a[j-1]
        c2 = a[j]
        c3 = a[j+1]
        if c1.count("#")==2 and c2.count("#")==1 and c3.count("#")==2:
            a1=j
            b1 = c2.index("#")
            break
    print(a1, b1+1)
