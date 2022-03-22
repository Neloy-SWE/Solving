num1 = int(input())
str1 = input()
num2=0
for i in range (1,num1):
    if str1[i]==str1[i-1]:
        num2+=1
print(num2)