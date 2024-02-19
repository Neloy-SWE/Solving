for i in range(int(input())):
    a = 0
    b = 0
    s = input()
    for i in s:
        if i=="A":
            a+=1
        else:
            b+=1
    if (a>b):
        print("A")
    else:
        print("B")