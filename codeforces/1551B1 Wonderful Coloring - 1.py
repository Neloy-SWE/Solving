for i in range(int(input())):
    s = list(input())
    n = set(s)
    count=0
    for j in range(len(s)):
        flag = False
        for k in range(1+j,len(s)):
            if s[k]==s[j] and s[k]!="0":
                s[k]="0"
                flag= True
        if flag:
            count+=1
    o=len(n)-count
    if o%2==0:
        print(int(o/2)+count)
    else:
        print(int((o-1)/2)+count)