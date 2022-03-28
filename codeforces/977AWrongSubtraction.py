a, b = map(int, input().split())
num1=0
for i in range(b):
    if(a%10>0):
        num1=a-1
        a=num1
    else:
        num1=a/10
        a=num1

print(int(num1))
