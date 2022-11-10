a, b = map(int, input().split())
rejectKid = 0
for i in range(a):
    c, d= map(str, input().split())
    if c=="+":
        b+=int(d)
    elif b-int(d)<0:
        rejectKid+=1
    else:
        b-=int(d)
print(b,rejectKid)