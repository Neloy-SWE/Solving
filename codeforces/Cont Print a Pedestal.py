num1 = int(input())
for i in range(num1):
    k = int(input())
    c = (k-3)//3
    r = k-c
    if (r%2==0):
        a = (r+2)//2
        b = k-(a+c)
    else:
        b = (r-1)//2
        a = (r+1)//2
    print(b, a, c)