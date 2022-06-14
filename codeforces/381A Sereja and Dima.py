k = int(input())
a = list(map(int, input().split()))
S = 0
D = 0

i=0
start = 0
end = len(a)-1
while(start<=end):
    if i%2==0:
        if a[start]>a[end]:
            S+=a[start]
            start+=1
        else:
            S+=a[end]
            end-=1
    else:
        if a[start]>a[end]:
            D+=a[start]
            start+=1
        else:
            D+=a[end]
            end-=1
    i+=1
print(S,D)