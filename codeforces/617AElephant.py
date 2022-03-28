import math
num1 = int(input())
if(num1<=5):
    print(1)
elif(num1%5==0):
    print(int(num1/5))
else:
    print(int(math.floor(num1/5)+1))