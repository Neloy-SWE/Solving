a = int(input())
if(a<4):
    print(1)
else:
    b = int(a/2)
    count = 0
    for i in range(1, b+1):
        if((a-i)%i==0):
            count+=1
    print(count)