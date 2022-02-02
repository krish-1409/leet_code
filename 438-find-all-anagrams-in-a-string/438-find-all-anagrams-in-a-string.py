class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dic = [0 for _ in range(26)]
        ref = [0 for _ in range(26)]
        n = len(p)
        m = len(s)
        if n>m:
            return []
        for i in range(n):
            ref[ord(p[i])-ord('a')]+=1
            dic[ord(s[i])-ord('a')]+=1
        print(ref)
        m = len(s)
        ans = []
        if dic==ref:
            ans.append(0)
        i=0
        j=n    
        while j<m:
            dic[ord(s[i])-ord('a')]-=1
            dic[ord(s[j])-ord('a')]+=1
            # print(dic,s[i],s[j])
            if dic==ref:
                ans.append(i+1)
            i+=1
            j+=1
        return ans
        