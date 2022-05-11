str1 = input()
str2 = input()
str3 = input()
if(len(str3)==len(str1)+len(str2)):
    str4=str1+str2
    list1 = list(str3)
    list2 = list(str4)
    for i in range(len(list2)):
        for j in range(len(list1)):
             if(list2[i]==list1[j]):
                  list1.remove(list1[j])
                  break
    if(len(list1)>0):
        print("NO")
    else:
        print("YES")
else:
    print("NO")

