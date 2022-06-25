for i in range(int(input())):
    n = int(input())
    count=0
    for j in range(1, 10):
        sj = j
        while(sj<=n):
            count+=1
            sj=(sj*10)+j
    print(count)