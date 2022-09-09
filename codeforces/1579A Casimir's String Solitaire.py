for i in range(int(input())):
    s = input()
    if len(s)%2!=0:
        print("NO")
    else:
        countB = 0
        for j in range (len(s)):
            if s[j]=="B":
                countB+=1
        if int(len(s)/2)==countB:
            print("YES")
        else:
            print("NO")