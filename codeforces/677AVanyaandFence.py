a, b = map(int, input().split())
c = list(map(int, input().split()))
d=0
for i in range(a):
    if c[i]>b:
        d+=2
    else:
        d+=1
print(d)