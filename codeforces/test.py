# num1 = int(input())
# for i in range(num1):
#     k = int(input())
#     a = list(map(int, input().split()))


a = list(map(int, input().split()))
A = []
B = []

while(len(a)>0):
    maxa = max(a)
    B.append(maxa)
    a.remove(maxa)
    mina = min(a)
    A.append(mina)
    a.remove(mina)
c = max(A)-min(B)
print(c)

