for i in range(int(input())):
    a, b = map(str, input().split())
    if a == b:
        print("=")
    elif "S" in a:
        if "S" in b:
            if len(a)>len(b):
                print("<")
            else:
                print(">")
        else:
            print("<")
    elif "L" in a:
        if "L" in b:
            if len(a)>len(b):
                print(">")
            else:
                print("<")
        else:
            print(">")
    elif "M" in a:
        if "S" in b:
            print(">")
        else:
            print("<")