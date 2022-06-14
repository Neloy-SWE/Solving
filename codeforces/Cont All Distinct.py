for i in range(int(input())):
    length = int(input())
    a = list(map(int, input().split()))
    b = set(a)
    if(len(a)-len(b)==0):
        print(length)
    elif (len(a)-len(b))%2==0:
        print(len(b))
    else:
        print(len(b)-1)