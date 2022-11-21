# for i in range(int(input())):
#     n = int(input())
#     s = input()
#     a, b = map(int, input().split())
#     a, b, = map(str, input().split())
#     a = list(map(int, input().split()))

def countMin(a, minValue):
    count = 0
    for i in a:
        if i==minValue:
            count+=1
    return count
for i in range(int(input())):
    n = input()
    a = list(map(int, input().split()))
    minA = min(a)
    o = countMin(a, minA)
    flag = False
    if o==1:
        print("YES")
    else:
        mi = a.index(minA)
        for j in range(mi, mi+o):
            if a[j]==minA:
                flag=True
            else:
                flag=False
        if(flag):
            print("YES")
        else:
            print("NO")
    