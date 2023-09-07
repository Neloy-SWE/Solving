for i in range(int(input())):
    n = int(input())
    d = []
    s = []
    room = 0
    finalRoom = 0
    for j in range(n):
        a, b = map(int, input().split())
        d.append(a)
        s.append(b)
    if(s[0] % 2 == 0):
        room = d[0] + ((s[0]-2)//2)
    else:
        room = d[0]+((s[0]-1)//2)
    if(n == 1):
        print(room)
    else:
        for k in range(1, len(d)):
            if (d[k] >= room):
                continue
            else:
                if(s[k] % 2 == 0):
                    finalRoom = d[k] + ((s[k]-2)//2)
                else:
                    finalRoom = d[k]+((s[k]-1)//2)
                if (finalRoom < room):
                    room = finalRoom
        print(room)
