# for i in range(int(input())):
#     n = int(input())
#     s = input()
#     a, b = map(int, input().split())
#     a, b, = map(str, input().split())
#     a = list(map(int, input().split()))
#     a = list(map(str, input().split()))

import math

for i in range(int(input())):
    n = input()
    c=0
    f=0
    mn = int(n)
    if mn%7==0:
        print(n)
    else:
        o1=(math.ceil(mn/7))*7
        o2=(mn//7)*7
        so1=str(o1)
        so2=str(o2)
        for i in range(len(n)):
            if n[i]!=so1[i]:
                c+=1
            if n[i]!=so2[i]:
                f+=1
        if c==f or c<f:
            print(o1)
        else:
            print(o2)