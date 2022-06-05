multiple2 = 3
index = 1
sum = 0
while multiple2 < 1000:
    multiple2 = 3 * index
    if (multiple2 < 1000):
        sum = sum + multiple2
    index = index + 1
print (sum)