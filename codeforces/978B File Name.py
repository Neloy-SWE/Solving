n = int(input())
s = input()
count=0
for i in range(2, len(s)):
    if s[i-2]=="x" and s[i-1]=="x" and s[i]=="x":
        count+=1
print(count)
