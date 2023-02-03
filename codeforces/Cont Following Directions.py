for i in range(int(input())):
    x = 0
    y = 0
    a = input()
    b = input()
    flag = False
    for j in range(len(b)):
        if b[j]=="U":
            x+=1
        elif b[j]=="D":
            x-=1
        elif b[j]=="R":
            y+=1
        elif b[j]=="L":
            y-=1
        if x==1 and y==1:
            flag=True
    if flag:
        print("YES")
    else:
        print("NO")
