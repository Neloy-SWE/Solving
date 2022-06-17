n, m = map(int, input().split())
bw = 0
for i in range(n):
    color = list(map(str, input().split()))
    for i in range(m):
        if color[i] == "W" or color[i] == "B" or color[i] == "G":
            bw += 1
if bw < (n*m):
    print("#Color")
else:
    print("#Black&White")
