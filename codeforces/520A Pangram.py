num1 = int(input())
 
str1 = input().lower()
 
list1 = list(str1)
 
set1=set()
for i in range(len(list1)):
    if (list1[i] >= "a" and list1[i] <= "z") or (list1[i] >= "A" and list1[i] <= "Z"):
        set1.add(list1[i])
 
 
if len(set1)==26:
    print("YES")
else:
    print("NO")