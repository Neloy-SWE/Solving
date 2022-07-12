for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        key, value = map(str, input().split())
        for j in range(int(key)):
            if value[j]=="D":
                if a[i]==9:
                    a[i]=0
                else:
                    a[i]+=1
            else:
                if a[i]==0:
                    a[i]=9
                else:
                    a[i]-=1
    print(*a)