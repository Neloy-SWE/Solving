a, b = map(int, input().split())

for i in range(a):
    if(i+1)%2!=0 and (i+1)%4!=0:
        for j in range(b):
            print("#", end="")
        print()
    elif (i+1)%2==0 and (i+1)%4!=0:
        for j in range(b-1):
            print(".", end="")
        print("#")
    elif (i+1)%4==0:
        print("#", end="")
        for j in range(b-1):
            print(".", end="")
        print()