def output(n):
    for i in range(2 * n):
        row = ''
        for j in range(2 * n):
            if (i // 2 + j // 2) % 2 == 0:
                row += '#'
            else:
                row += '.'
        print(row)
for i in range(int(input())):
    n = int(input())
    output(n)