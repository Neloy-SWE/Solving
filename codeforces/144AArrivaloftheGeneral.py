def minIndex(index):
    x = index[0]
    y =0
    for i in range(len(index)):
        if(index[i]<=x):
            x=index[i]
            y=i
    return y+1

def maxIndex(index):
    x=0
    y=0
    for i in range(len(index)-1, -1, -1):
        if(index[i]>=x):
            x=index[i]
            y=i
    return y+1

num1 = int(input())
list1 = list(map(int, input().split()))
a=minIndex(list1)
b=maxIndex(list1)

if a>b:
    print((num1-a)+(b-1))
else:
    print((num1-a)+(b-2))


