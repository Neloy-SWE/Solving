num1 = int(input())
list1 = list(map(int, input().split()))

max = max(list1)
count = 0
for i in range(num1):
    count+=(max-list1[i])
print(count)