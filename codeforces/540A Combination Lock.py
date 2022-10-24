n = int(input())
s1 = input()
s2 = input()
sumMove=0
for i in range(n):
    total=abs(int(s1[i])-int(s2[i]))
    if total<=5:
        sumMove+=total
    else:
        sumMove+=(10-total)
print(sumMove)