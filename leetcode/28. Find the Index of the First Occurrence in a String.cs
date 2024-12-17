public class Solution {
    public int StrStr(string haystack, string needle) {
        int startIndex = -1;
        if(haystack.Contains(needle)){
            for (int j = 0; j<haystack.Length; j++){
                if (needle[0]==haystack[j]){
                    int k = j;
                    for (int i = 0; i<needle.Length; i++){
                        if (needle[i] != haystack[k]){
                            break;
                        }
                        k++;
                        
                    }
                    if (k-j==needle.Length){
                            startIndex=j;
                            break;
                        }
                }
            }
        }
        return startIndex;
    }
}