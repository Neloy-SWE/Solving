num1 = int(input())

for i in range(num1):
    str1=input()
    str2=str1[0]+str1[1]
    for j in range(3,len(str1),2):
        str2=str2+str1[j]
    print(str2)