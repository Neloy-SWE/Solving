for i in range(int(input())):
    a = int(input())
    p = list(map(int, input().split()))
    ans = []
    for i in range(len(p)):
        if(p[i] in ans):
            continue
        else:
            ans.append(p[i])
    print(*ans)