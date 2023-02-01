for i in range(int(input())):
    n = int(input())
    j = 1
    set1 = set()
    while( j*j<=n):
        set1.add(j*j)
        j+=1
    j = 1
    while( j*j*j<=n):
        set1.add(j*j*j)
        j+=1
    print(len(set1))