class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = list(s.split())
        n = len(pattern)
        m = len(s)
        if n!=m:
            return False
        i = 0
        dic = {}
        vis = set()   #if there is a case with two equal words for different letters in pattern, In vis we store each words given in the string if in pattern the letter is matched to word in a string then we add to vis if the same word is matched to different letter in pattern then we can return false.
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
            