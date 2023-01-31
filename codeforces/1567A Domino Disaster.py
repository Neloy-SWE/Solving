for i in range(int(input())):
    n = input()
    s = input()
    ans = ""
    for j in s:
        if j == "U":
            ans+="D"
        elif j == "D":
            ans+="U"
        else:
            ans+=j
    print(ans)