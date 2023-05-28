for i in range(int(input())):
    n = input()
    a = list(map(int, input().split()))
    even = 0
    odd = 0
    for j in a:
        if j%2==1:
            odd+=j
        else:
            even+=j
    if (even>odd):
        print("YES")
    else:
        print("NO")