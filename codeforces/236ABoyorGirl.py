str1 = input()
str2 =''.join(set(str1))
if(len(str2)%2==0):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")