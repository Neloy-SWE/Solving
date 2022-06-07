num1 = int(input())
for i in range(num1):
    k = int(input())
    a = list(map(int, input().split()))
    maxa = max(a)
    mina = min(a)
    print(maxa-mina)