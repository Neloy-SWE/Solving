# num1 = int(input())
# for i in range(num1):
#     k = int(input())
#     a = list(map(int, input().split()))

n, q = map(int, input().split())
product = sorted(list(map(int, input().split())))
for i in range(q):
    x, y = map(int, input().split())
    count=0
    for j in range(len(product)-x, len(product)-y+1):
        count+=product[j]
    print(count)





