for i in range(int(input())):
    n,k = map(int, input().split())
    s=input()
    count = 0
    for j in range(k):
        if s[j]=="W":
            count+=1
    result = count
    for l in range(k, n):
        if s[l]=="W":
            count+=1
        if s[l-k]=="W":
            count-=1
            result = min(result,count)
    print(result)