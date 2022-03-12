num = int(input())
count=0
for i in range(num):
    a, b, c = map(int,input().split(" "))
    if((a+b+c)>=2):
        count+=1
print(count)