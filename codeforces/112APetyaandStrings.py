str1 = input().lower()
str2 = input().lower()
num = 0
for i in range(len(str1)):
    if ord(str1[i]) > ord(str2[i]):
        num=1
        break
    elif ord(str1[i]) < ord(str2[i]):
        num=-1
        break
    else:
        continue
print(num)