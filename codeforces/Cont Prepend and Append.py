for i in range(int(input())):
    a = input()
    b = list(input())
    while(b[0]!=b[len(b)-1]):
        # if b[0]=="1" and b[len(b)-1]=="0":
        b=b[1:len(b)-1]
        if len(b)==0:
            break
        # elif b[0]=="0" and b[len(b)-1]=="1":
        #     del b[0]
        #     del b[len(b)-1]
    print(len(b))