def checkDivisible(a, b):
    if a==b or a%b==0:
        print(0)
    elif a<b:
        print(b-a)
    else:
        print(int(b-(a%b)))


num1 = int(input())

for i in range(num1):
    a, b = map(int, input().split())
    checkDivisible(a, b)