n, q = map(int, input().split())
product = sorted(list(map(int, input().split())), reverse=True)

xProduct = []
xProduct.append(product[0])
for i in range(1, n):
    xProduct.append(xProduct[i-1]+product[i])
for j in range(q):
    x, y = map(int, input().split())
    ans = 0
    ans = xProduct[x-1]-xProduct[x-q]+product[x-q]
    print(ans)