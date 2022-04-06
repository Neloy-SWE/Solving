str1 = input()
str3 = input()
str2=""
for i in str1:
    str2=i+str2
if str2==str3:
    print("YES")
else:
    print("NO")