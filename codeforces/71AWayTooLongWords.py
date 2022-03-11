num = int(input())
list =[]
for i in range(num):
    list.append(str(input()))
    if(len(list[i])>10):
        print(list[i][0]+str(len(list[i])-2)+list[i][len(list[i])-1])
    else:
        print(list[i])