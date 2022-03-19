num = int(input())
count = 0
for i in range(num):
    bit = str(input())
    if (bit == "++X" or bit == "X++"):
        count += 1
    else:
        count -= 1
print(count)