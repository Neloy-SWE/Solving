num1=int(input())

a = list(map(int, input().split()))
count=0
for i in range(num1):
    count+=a[i]

print("%.12f" %(count/num1))