for i in range(int(input())):
    a,b,c = map(int, input().split())
    maxValue = max(a,b,c)
    minValue = min(a,b,c)
    if (a+b+c)-maxValue==maxValue:
        print("YES")
    elif (a+b+c)-maxValue-minValue==maxValue and minValue%2==0:
        print("YES")
    elif (a+b+c)-maxValue-minValue==minValue and maxValue%2==0:
        print("YES")
    else:
        print("NO")