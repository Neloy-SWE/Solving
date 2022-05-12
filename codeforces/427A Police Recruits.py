num1 = int(input())
list1 = list(map(int, input().split()))

police = 0
untreated=0
for i in list1:
    if i==-1:
        if police>0:
            police-=1
        else:
            untreated+=1
    else:
        police+=i
print(untreated)