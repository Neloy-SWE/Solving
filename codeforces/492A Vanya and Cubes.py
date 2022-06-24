n = int(input())
i = 0
a = 0
b = 0
while(n>0):
    i+=1
    a = b+i
    b = a
    n = n-a
    if (n<0):
        i-=1
print(i)