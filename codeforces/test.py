# for i in range(int(input())):
#     n = int(input())
#     s = input()
#     a, b = map(int, input().split())
#     a, b, = map(str, input().split())
#     a = list(map(int, input().split()))
#     a = list(map(str, input().split()))

n = input()
indexQ = n.index("Q")
n = n[indexQ:]
q1=0
a=0
q2=0
isq1 = True
for i in n:
    if i=="Q" and isq1:
        q1+=1
    elif i=="A":
        isq1 = False
        a+=1
    elif i=="Q":
        q2+=1
print(q1*q2*a)
