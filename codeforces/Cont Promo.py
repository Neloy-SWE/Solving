n, q = map(int, input().split())
product = sorted(list(map(int, input().split())), reverse=True)
xProduct = [0]
for i in range(1, n+1):
    xProduct.append(xProduct[i-1]+product[i-1])
for j in range(q):
    x, y = map(int, input().split())
    print(xProduct[x]-xProduct[x-y])