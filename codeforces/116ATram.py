num1 = int(input())
num2 = 0
num3 = 0
for i in range(num1):
    a, b = map(int, input().split())
    num2 = abs(num2-a)+b
    if(num2>num3):
        num3 = num2
    else:
        continue
print(num3)