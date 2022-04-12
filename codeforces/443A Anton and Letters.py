a = list(map(str, input()))
set1=set()
for i in range(len(a)):
    if a[i]>="a" and a[i]<="z":
        set1.add(a[i])
 
print(len(set1))