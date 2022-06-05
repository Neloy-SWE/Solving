num1 = int(input())
for i in range(num1):
    k = int(input())
    i=0
    while(k>0):
        i+=1
        if (i%3==0 or i%10==3):
            continue
        else:
            k-=1
       
    print(i)
