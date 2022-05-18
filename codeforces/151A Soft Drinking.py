n, k, l, c, d, p, nl, np = map(int, input().split())

kl = (k*l)//nl
slice = c*d
salt = p//np

print(min(kl, slice, salt)//n)