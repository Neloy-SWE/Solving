num1 = int(input())
for i in range(num1):
    num2 = int(input())
    list1 = list(map(int, input().split()))
    list2 = list(set(list1))
    a = 0
    b = 0
    for i in range(num2):
        if list2[0]==list1[i]:
            a+=1
    if(a>1):
        print(list1.index(list2[1])+1)
    else:
        print(list1.index(list2[0])+1)
