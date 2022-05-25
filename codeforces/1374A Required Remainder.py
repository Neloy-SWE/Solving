num1 = int(input())
for i in range(num1):
    x, y, n = map(int, input().split())
    if n%x==y:
        print(n)
    else:
        num2 = (n-y)//x
        print((num2*x)+y)