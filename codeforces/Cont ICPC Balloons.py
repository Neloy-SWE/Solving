for i in range(int(input())):
    n = int(input())
    s = input()
    lenS = len(s)
    set1 = set(s)
    lenSet1 = len(set1)
    ans = (lenSet1*2)+(lenS-lenSet1)
    print(ans)