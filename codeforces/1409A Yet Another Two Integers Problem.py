num1 = int(input())
for i in range(num1):
    a, b = map(int, input().split())
    c=abs(a-b)
    if c ==0:
        print(0)
    elif(c<=10):
        print(1)
    elif(c%10==0):
        print(c//10)
    else:
        print((c//10)+1)