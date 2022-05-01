num1 = int(input())
count=0
while(num1>0):
    if(num1 == 1 or num1 == 5 or num1 == 10 or num1 == 20 or num1 ==100):
        count+=1
        break
    elif(num1>1 and num1<5):
        count+=num1
        break
    elif(num1>5 and num1<10):
        count=(num1-5)+1+count
        break
    elif(num1>10 and num1<20):
        num1=num1-10
        count+=1
        continue
    elif(num1>20 and num1<100):
        count=int(num1/20)+count
        num1=int(num1%20)
        continue
    else:
        count=int(num1/100)+count
        num1=int(num1%100)
        continue
print(count)

