a, b = map(int, input().split())
c = abs(a-b)
if(a>b):
    print(b, int(c/2))
else:
    print(a, int(c/2))