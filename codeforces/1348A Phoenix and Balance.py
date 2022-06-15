for i in range(int(input())):
    n = int(input())
    if n ==2:
        print(2)
    else:
        pile1=0
        pile2=0
        for i in range(1, n+1):
            if i<n//2 or i==n:
                pile1+=(2**i)
            else:
                pile2+=(2**i)
        print(abs(pile1-pile2))