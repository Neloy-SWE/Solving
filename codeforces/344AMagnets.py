num1 = int(input())
list1 = []
for i in range(num1):
    list1.append(input())

temp=list1[0]
count=1
for i in range(1,num1):
    if list1[i]==temp:
        continue
    else:
        temp=list1[i]
        count+=1
print(count)