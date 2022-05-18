num1, num2 = map(int, input().split())
 
list1 = list(map(int, input().split()))
 
list2=sorted(list1)
count = 0
 
for i in range(2, len(list2),3):
    if 5-list2[i]>=num2:
        count+=1
print(count)