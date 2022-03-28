str1 = input()
up = 0
low = 0
for ch in str1:
    if(ord(ch)<91):
        up+=1
    else:
        low+=1
if(up<=low):
    print(str1.lower())
else:
    print(str1.upper())