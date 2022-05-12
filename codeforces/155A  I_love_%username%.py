num1 = int(input())

fPoint = list(map(int,input().split()))

max = fPoint[0]
min = fPoint[0]
count = 0

for i in range(1,len(fPoint)):
    if(fPoint[i]>max):
        max=fPoint[i]
        count+=1
    elif(fPoint[i]<min):
         min=fPoint[i]
         count+=1

print(count)