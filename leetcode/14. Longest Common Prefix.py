class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans = ""
        isContinue = True
        prefix = min(strs, key=len)
        strs.remove(prefix)
        for i in range(len(prefix)):
            for j in range(len(strs)):
                if (prefix[i]==strs[j][i]):
                    isContinue = True
                else:
                    isContinue= False
                    break
            if(isContinue):
                ans+=prefix[i]
            else:
                break
        return ans