s = input()
t = input()
si = 0
count = 1
for i in range(len(t)):
    if t[i]==s[si]:
        si+=1
        count+=1
print(count)