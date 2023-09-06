class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X":10, "L":50, "C": 100, "D": 500, "M": 1000}
        sum=0
        i=len(s)-1
        check = ""
        while(i>0):
            if(roman[s[i]]>roman[s[i-1]]):
                sum+=(roman[s[i]]-roman[s[i-1]])
                check = s[i-1]+s[i]+check
                i-=2
            else:
                sum+=roman[s[i]]
                check=s[i]+check
                i-=1
        if (len(check)<len(s)):
            sum+=roman[s[0]]
        return sum