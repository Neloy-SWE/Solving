for i in range(int(input())):
    a, b, c = map(int, input().split())
    if a ==1:
        print(1)
    elif (b>c):
        b = b-1
        a = a-1
        if (b==a):
            print(3)
        elif(a>b):
            print(2)
        else:
            print(1)
    elif (b<c):
        b=c-b
        c = c-1
        a = a-1
        if (a>(b+c)):
            print(2)
        elif(a<(b+c)):
            print(1)
        else:
            print(3)   