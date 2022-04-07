num1=int(input())
while(1):
    num1+=1
    a = int(num1%10)
    b = int((num1/10)%10)
    c = int((num1/100)%10)
    d = int((num1/1000)%100)
    if(a !=b and a !=c and a !=d and c !=b and c !=d and d !=b):
        break
print(num1)
