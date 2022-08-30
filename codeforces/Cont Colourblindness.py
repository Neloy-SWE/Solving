for i in range(int(input())):
    n = int(input())
    count = 0
    r1 = input()
    r2 = input()
    for j in range(n):
        if (r1[j] == "R"):
            if (r2[j] == "R"):
                continue
            else:
                count += 1
                break
        elif(r2[j] == "R"):
            count += 1
            break
        else:
            continue
    if(count == 1):
        print("NO")
    else:
        print("YES")
