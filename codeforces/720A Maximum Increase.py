def countMax(a):
    currentMax = a[0]
    for i in a:
        if currentMax<i:
            currentMax=i
    return currentMax
n = int(input())
a = list(map(int, input().split()))
temp = 1
b =[]
for i in range(1,len(a)):
    if a[i-1]<a[i]:
        temp+=1
    else:
       b.append(temp)
       temp=1
b.append(temp)
print(countMax(b))