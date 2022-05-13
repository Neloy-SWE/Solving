list1 = list(map(int, input().split()))
list2=sorted(list1)
max = list2[3]
min = list2[0]
c=(max-min)
b=abs(list2[2]-c)
a=abs(list2[1]-c)
print(a,b,c)