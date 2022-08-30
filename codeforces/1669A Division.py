for i in range(int(input())):
    a = int(input())
    if a <= 1399:
        print("Division 4")
    elif a <= 1599 and a >= 1400:
        print("Division 3")
    elif a <= 1899 and a >= 1600:
        print("Division 2")
    else:
        print("Division 1")
