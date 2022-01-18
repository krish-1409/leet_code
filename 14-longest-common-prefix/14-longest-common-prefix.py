class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        ans= ""
        i = 0
        while i<200:
            j = 0
            while j<n:
                
                try:
                    if strs[j][i] == strs[0][i]:
                        j+=1
                        continue
                    else:
                        return ans
                except:
                    return ans
                j+=1
            ans+=strs[0][i]
            i+=1
        return ans