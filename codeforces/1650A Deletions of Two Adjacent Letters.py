for i in range(int(input())):
    s = input()
    c = input()

    if c in s[::2]:
        print("YES")
    else:
        print("NO")