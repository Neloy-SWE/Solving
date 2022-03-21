str1 = input().replace("+", "")
str2 = sorted(str1)
print(("+".join(map(str,str2))))