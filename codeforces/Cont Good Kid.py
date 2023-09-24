def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    indexMin = a.index(min(a))
    a[indexMin]+=1
    print(multiplyList(a))
