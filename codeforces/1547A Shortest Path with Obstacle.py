for i in range(int(input())):
    input()
    xa, ya = map(int, input().split())
    xb, yb = map(int, input().split())
    xf, yf = map(int, input().split())

    if xa==xf==xb:
        if ya<yf<yb or yb<yf<ya:
            print(abs(yb-ya)+2)
        else:
            print(abs(yb-ya)+abs(xb-xa))
    elif ya==yf==yb:
        if xa<xf<xb or xb<xf<xa:
            print(abs(xb-xa)+2)
        else:
            print(abs(yb-ya)+abs(xb-xa))
    else:
        print(abs(yb-ya)+abs(xb-xa))