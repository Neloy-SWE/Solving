k = int(input())
a = sorted(list(map(int, input().split())))
S = []
D = []

i=0
while(len(a)>0):
    start = 0
    end = len(a)-1
    if len(a)==1:
        if i%2==0:
            S.append(a[0])
            a.pop(0)
        else:
            D.append(a[0])
            a.pop(0)
        i+=1
    else:
        maxk = max(a[start], a[end])
        if i%2==0:
            if maxk==a[start]:
                S.append(a[start])
                a.pop(start)
            else:
                S.append(a[end])
                a.pop(end)
        else:
            if maxk==a[start]:
                D.append(a[start])
                a.pop(start)
            else:
                D.append(a[end])
                a.pop(end)
        i+=1

print(sum(S), sum(D))