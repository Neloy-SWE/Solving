num1 = int(input())
list1 = list(map(int, input().split()))

a = 0
b = 0
c = 0

lista = []
listb = []
listc = []

for i in range(num1):
    if list1[i]==1:
        lista.append(i)
        a+=1
    elif list1[i]==2:
        listb.append(i)
        b+=1
    if list1[i]==3:
        listc.append(i)
        c+=1
if(min(a,b,c)==0):
    print(0)
else:
    print(min(a,b,c))
    for i in range(min(a,b,c)):
        print(lista[i]+1,listb[i]+1,listc[i]+1)
    