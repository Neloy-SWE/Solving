for i in range(int(input())):
    a = list(map(int, input().split()))
    count=0
    for j in range(1,len(a)):
        if a[j]>a[0]:
            count+=1
    print(count)
