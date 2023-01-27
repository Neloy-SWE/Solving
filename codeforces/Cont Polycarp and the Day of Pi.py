pai = "314159265358979323846264338327"
for i in range(int(input())):
    a = input()
    count=0
    b=pai[:len(a)]
    for j in range(len(b)):
        if(a[j]==b[j]):
            count+=1
        else:
            break
    print(count)