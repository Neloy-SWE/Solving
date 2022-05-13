num1 = int(input())
for i in range(num1):
    l1, r1, l2, r2 = map(int, input().split())
    if(l2>=l1 and l2<=r1):
        print(l2)
    elif(l1>=l2 and l1<=r2):
        print(l1)
    else:
        print(l2+l1)