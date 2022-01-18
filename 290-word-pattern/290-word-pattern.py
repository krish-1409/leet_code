class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = list(s.split())
        n = len(pattern)
        m = len(s)
        if n!=m:
            return False
        i = 0
        dic = {}
        vis = set()
        while i<n:
            if pattern[i] not in dic:
                if s[i] in vis:
                    return False
                dic[pattern[i]] = s[i]
                vis.add(s[i])
            else:
                if dic[pattern[i]] != s[i]:
                    return False
            i+=1
        return True
            