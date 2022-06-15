s = input()
i=1
ans = ""
while(i<=len(s)):
    if s[i-1]==".":
        ans+="0"
        i+=1
    elif s[i-1]=="-" and s[i]==".":
        ans+="1"
        i+=2
    elif s[i-1]=="-" and s[i]=="-":
        ans+="2"
        i+=2
print(ans)