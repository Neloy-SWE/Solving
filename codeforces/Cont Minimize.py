for i in range(int(input())):
    a, b = map(int, input().split())
    c = int((a+b)/2)
    d = (c-a)+(b-c)
    print(d)