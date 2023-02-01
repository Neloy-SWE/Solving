for i in range(int(input())):
    n = input()
    a = list(map(int, input().split()))
    ao = []
    ae = []

    for j in range(int(n)):
        if j%2==0:
            ao.append(a[j])
        else:
            ae.append(a[j])

    x = ao[0]%2
    y = ae[0]%2

    isX = True
    isY = True

    for j in range(len(ao)):
        if ao[j]%2!=x:
            isX=False
            break
    for j in range(len(ae)):
        if ae[j]%2!=y:
            isY=False
            break

    if isX and isY:
        print("YES")
    else:
        print("NO")