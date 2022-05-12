a, b = map(int, input().split())

i = 1
j=1
while(i):
    if((a*j)%10==b or (a*j)%10==0):
        i=0
    else:
        j+=1
print(j)