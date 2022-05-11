num1 = int(input())
result=0
for i in range(num1):
    num2=int(input())
    if num2>2:
        if num2%2==1:
            result=(num2-1)/2
        elif num2%2==0:
            result=(num2-2)/2
        print(int(result))
    else:
        print(0)