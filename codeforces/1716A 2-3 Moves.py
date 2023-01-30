for i in range(int(input())):
    n=abs(int(input()))
    if(n==1):
        print(2)
    else:
        if(n%3==0):
            print(int(n/3))
        elif((n+2)%3==0):
            print(int((n+2)/3))
        elif((n+1)%3==0):
            print(int((n+1)/3))