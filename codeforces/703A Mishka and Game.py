num1 = int(input())
win = 0
for i in range(num1):
    m, c = map(int, input().split())
    if m>c:
        win+=1
    elif m<c:
        win-=1
if (win>0):
    print("Mishka")
elif(win<0):
    print("Chris")
else:
    print("Friendship is magic!^^")