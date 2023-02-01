def fact(a):
    if a<2:
        return a
    else:
        return a*fact(a-1)
a,b = map(int, input().split())
print(fact(min(a,b)))