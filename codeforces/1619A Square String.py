for i in range(int(input())):
    s = input()
    if(len(s)%2!=0):
        print("NO")
    else:
        s1 = s[:int((len(s))/2)]
        s2 = s[int(len(s)/2):]
        if(s1==s2):
            print("YES")
        
        else:
            print("NO")