# for i in range(int(input())):
#     k = int(input())
#     a = list(map(int, input().split()))


for i in range(int(input())):
    k = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    minA = min(a)
    minB = min(b)
    count = 0
    for i in range(k):
        if a[i]>minA and b[i]>minB:
            count+=1
            a[i]=a[i]-1
            b[i]=b[i]-1
        elif a[i]>minA and b[i]==minB:
            count+=1
            a[i]=a[i]-1
        elif a[i]==minA and b[i]>minB:
            count+=1
            b[i]=b[i]-1
    print(count)

