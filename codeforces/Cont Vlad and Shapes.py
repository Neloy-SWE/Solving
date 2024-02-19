for i in range(int(input())):
    n = int(input())
    fi = 0
    li = 0
    sfi = 0
    sli = 0
    for j in range(n) :
        s = input()
        if "1" in s:
            if (fi == 0):
                fi = s.index("1")
            else:
                sfi = s.index("1")
            if (li ==0):
                li = list(reversed(s)).index("1")
            else:
                sli = list(reversed(s)).index("1")
    if (fi==sfi and li==sli):
        print("SQUARE")
    else:
        print("TRIANGLE")