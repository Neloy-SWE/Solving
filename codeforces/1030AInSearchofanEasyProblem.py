num1 = int(input())

a = list(map(int, input().split()))
count =0
for i in range(num1):
    if a[i]==1:
        count+=1
        break
if count>0:
    print("HARD")
else:
    print("EASY")