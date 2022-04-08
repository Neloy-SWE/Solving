
num1=int(input())
num2=int(input())
num3=int(input())
num4=int(input())
num5=int(input())
count=0
for i in range(1,num5+1):
    if(i%num1==0 or i%num2==0 or i%num3==0 or i%num4==0):
        count+=1
print(count)