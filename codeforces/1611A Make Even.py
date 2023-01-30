for i in range(int(input())):
    n = input()
    if int(n)%2==0:
        print(0)
    elif int(n[0])%2==0:
        print(1)
    else:
        flag = False
        for i in n:
            if int(i)%2==0:
                flag = True
                break
        if flag:
            print(2)
        else:
            print(-1)