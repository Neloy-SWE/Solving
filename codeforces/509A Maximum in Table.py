n = int(input())
a = []
b = []
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0:
            b.append(1)
        else:
            b.append(a[i-1][j]+b[j-1])
    a.append(b)
    b=[]

print(a[n-1][n-1])