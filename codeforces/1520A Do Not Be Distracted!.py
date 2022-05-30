num1 = int(input())
for i in range(num1):
    num2 = int(input())
    list1 = []
    a = input()
    a0 = a[0]
    for j in range(num2):
        if a0 == a[j]:
            continue
        else:
            list1.append(a0)
            a0=a[j]
    list1.append(a[len(a)-1])
    set1 = set(list1)
    if len(set1)==len(list1):
        print("YES")
    else:
        print("NO")
