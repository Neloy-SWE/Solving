for i in range(int(input())):
    n = input()
    plusIndex = n.index("+")
    pre = int(n[:plusIndex])
    post = int(n[plusIndex+1:])
    print(pre+post)