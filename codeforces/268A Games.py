num1 = int(input())
lista = []
listb = []
count = 0
for i in range(num1):
    a, b = map(int, input().split())
    lista.append(a)
    listb.append(b)
for i in range(num1):
    for j in range(num1):
        if lista[i]==listb[j]:
            count+=1
print(count)