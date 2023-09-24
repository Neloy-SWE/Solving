for i in range(int(input())):
    count=0
    for j in range (10):
        a = input()
        for k in range(len(a)):
            if a[k]=="X":
                if j==0 or j==9 or k==0 or k==9:
                    count+=1
                elif j==1 or j==8 or k==1 or k==8:
                    count+=2
                elif j==2 or j==7 or k==2 or k==7:
                    count+=3
                elif j==3 or j==6 or k==3 or k==6:
                    count+=4
                elif j==4 or j==5 or k==4 or k==5:
                    count+=5

    print(count)