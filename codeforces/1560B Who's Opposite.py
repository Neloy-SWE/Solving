for i in range(int(input())):
    a,b,c = map(int, input().split())

    minAb = min(a,b)
    maxAb = max(a,b)

    total = (maxAb+(maxAb-(minAb+1)))-(minAb-1)

    if abs(a-b)==1 or maxAb > total:
        print(-1)
    else:
        if c> total:
            print(-1)
        elif c==total:
            print(int(c/2))
        elif c == total/2:
            print(total)
        elif c < total/2:
            print(int(total-((total/2)-c)))
        elif c> total/2:
            print(int((total/2)-(total-c)))