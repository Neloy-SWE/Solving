listLength, scoreIndex = map(int, input().split())
a = list(map(int, input().split()))
count=0
for i in range(listLength):
    if(a[i]>=a[scoreIndex-1] and a[i]>0):
        count+=1
print(count)