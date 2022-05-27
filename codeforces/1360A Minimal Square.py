num1 = int(input())
for i in range(num1):
    a, b = map(int, input().split())
    c = min(a,b)
    c*=2
    c = max(c,a,b)
    print(c*c)