n,m = map(int,input().split())
a = 0
b = 0
ans = 0
while((a*a)<=n and a<=m):
    b = n-(a*a)
    if (a+(b*b)==m):
        ans+=1
    a+=1
print(ans)