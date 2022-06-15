a, b = map(int, input().split())
maxAB = max(a,b)
if maxAB == 1: 
    print("1/1")
elif maxAB == 2:
    print("5/6")
elif maxAB == 3:
    print("2/3")
elif maxAB == 4:
    print("1/2")
elif maxAB == 5:
    print("1/3")
elif maxAB==6:
    print("1/6")