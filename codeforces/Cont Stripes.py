for i in range(int(input())):
    a = []
    count = 0
    input()
    for j in range(8):
        a.append(input())
    for j in range(8):
        if "B" in a[j]:
            count+=1
    if count==8:
        print("B")
    else:
        print("R")