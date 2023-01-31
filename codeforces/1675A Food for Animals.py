for i in range(int(input())):
    a,b,c,x,y = map(int, input().split())
    if a>=x and b>=y:
        print("YES")
    elif a+c<x:
        print("NO")
    elif b+c<y:
        print("NO")
    elif a<x:
        v=(a+c)-x
        if v+b>=y:
            print("YES")
        else:
            print("NO")
    else:
        v=(b+c)-y
        if v+a>=x:
            print("YES")
        else:
            print("NO")
