num1 = int(input())
for i in range(num1):
    num2 =list(map(int,input()))
    if(len(num2)==2):
        print(num2[1])
    else:
        print(min(num2))