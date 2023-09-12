class Solution:
    def isValid(self, s: str) -> bool:
        ans = ""
        for i in s:
            if not ans:
                if (i==")" or i=="}" or i=="]"):
                    return False
            if (i=="(" or i=="{" or i=="["):
                ans+=i
            elif (ans[len(ans)-1]=="(" and i==")" or ans[len(ans)-1]=="{" and i=="}" or ans[len(ans)-1]=="[" and i=="]"):
                ans=ans[:-1]
            else:
                return False
        if not ans:
            return True
        else:
            return False