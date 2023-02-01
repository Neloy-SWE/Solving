a = []
flag = False
change = True
for i in range(int(input())):
    a.append(list(input()))
    if change:
        if a[i][0]=="O" and a[i][1]=="O":
            a[i][0]="+"
            a[i][1]="+"
            flag = True
            change = False
        elif a[i][3]=="O" and a[i][4]=="O":
            a[i][3]="+"
            a[i][4]="+"
            flag = True
            change = False

if not flag:
    print("NO")
else:
    print("YES")
    for i in range(len(a)):
        print("".join(a[i]))