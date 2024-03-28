for i in range(int(input())):
    s = input()
    n = int(s[:2])
    if (n==0):
        print("12"+s[2:]+" AM")
    elif n==12:
        print(s+" PM")
    elif n>12:
        a=n-12
        if len(str(a))==1:
            b="0"+str(a)
        else:
            b=str(a)
        print(b+s[2:]+" PM")
    else:
        print(s+" AM")