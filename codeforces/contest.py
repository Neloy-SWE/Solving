# for i in range(int(input())):
#     n = int(input())
#     s = input()
#     a, b = map(int, input().split())
#     a, b, = map(str, input().split())
#     a = list(map(int, input().split()))






import math
 
 
for i in range(int(input())):
    x, y, k = map(int, input().split())
    output = math.ceil(x/k) + math.ceil(y/k)
    print(output)