num1 = int(input())
for i in range(num1):
    a, b = map(int, input().split())
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    for j in range(b):
        max1 = max(list2)
        min1 = min(list1)
        if min1>=max1:
            break
        else:
            list1= sorted(list1)
            list2= sorted(list2)
            temp=list1[0]
            list1[0]=list2[len(list2)-1]
            list2[len(list2)-1]=temp
    print(sum(list1))