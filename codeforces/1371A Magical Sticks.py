for i in range(int(input())):
    n = int(input())
    if n<3:
        print(1)
    elif n%2==0:
        print(n//2)
    else:
        print((n//2)+1)