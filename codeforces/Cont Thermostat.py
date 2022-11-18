for i in range(int(input())):
    l,r,x = map(int, input().split())
    a,b = map(int, input().split())
    sRA = abs(a-l)
    bRA = abs(r-a)
    sRB = abs(b-l)
    brB = abs(b-r)
    if(a==b):
        print(0)
    elif abs(a-b)>=x:
        print(1)
    elif (sRA<x and bRA<x) or (sRB<x and brB<x):
        print(-1)
    else:
        if (sRA<x):
            if (brB>=x):
                print(2)
            else:
                print(3)
        elif bRA<x:
            if (sRB>=x):
                print(2)
            else:
                print(3)
        else:
            print(2)