import math


for i in range(int(input())):
    n, x = map(int, input().split())
    if(n<3):
        print(1)
    else:
        n=n-2
        x=math.ceil(n/x)
        print(x+1)