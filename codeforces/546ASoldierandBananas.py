a,b,c = map(int, input().split())
num1=0
for i in range(1,c+1):
    num1=num1+(a*i)
if num1<=b:
    print(0)
else:
    print(num1-b)