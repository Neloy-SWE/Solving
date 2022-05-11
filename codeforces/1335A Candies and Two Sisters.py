num1 = int(input())
list1=[]
result=0
for i in range(num1):
    list1.append(int(input()))
    if list1[i]>2:
        if list1[i]%2==1:
            result=(list1[i]-1)/2
        elif list1[i]%2==0:
            result=(list1[i]-2)/2
        print(int(result))
    else:
        print(0)