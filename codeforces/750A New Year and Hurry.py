from itertools import count


a, b = map(int, input().split())
count =0
c = 0
time = (240-b)

for i in range(1, a+1):
    c+=i*5
    if(c <= time):
        count+=1
    else:
        break
print(count)