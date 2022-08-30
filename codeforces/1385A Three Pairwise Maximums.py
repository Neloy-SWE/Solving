for i in range(int(input())):
    list1 = list(map(int, input().split()))
    maxList = max(list1)
    if list1.count(maxList) > 1:
        print("YES")
        print(f"{maxList} {min(list1)} {min(list1)}")
    else:
        print("NO")
