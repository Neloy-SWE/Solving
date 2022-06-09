num1 = int(input())
for i in range(num1):
    indexa = int(input())
    a = list(map(int, input().split()))

    seta = set(a)
    if (len(a)!=len(seta)):
        print(0)
    else:
        sorta = sorted(a)
        ans = max(a)
        for i in range(1, len(a)):
            if(sorta[i]-sorta[i-1]<ans):
                ans = sorta[i]-sorta[i-1]
        print(ans)