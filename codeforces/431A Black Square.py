a = list(map(int, input().split()))
s = input()
sum = 0
for i in s:
    sum+=a[int(i)-1]
print(sum)