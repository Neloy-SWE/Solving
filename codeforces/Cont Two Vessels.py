import math


for i in range(int(input())):
    a, b, c = map(int, input().split())
    print(math.ceil((((a+b)/2)-min(a, b))/c))
