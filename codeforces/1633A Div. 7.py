for i in range(int(input())):
    n = int(input())

    if n%7==0:
        print(n)
    else:
        n=(n//10)*10
        for i in range(n, n+9):
            if i%7==0:
                print(i)
                break