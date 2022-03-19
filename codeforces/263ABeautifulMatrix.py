n = 0
m = 0
mat = [list(map(int,input().split())) for i in range(5)]

for i in range(5):
    for j in range(5):
        if(mat[i][j]==1):
            n = i+1
            m = j+1
            break
print((abs(m-3)+abs(n-3)))
