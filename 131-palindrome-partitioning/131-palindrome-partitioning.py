def getPartition(s,temp=[]):
    if not s:
        getPartition.ans.append(temp)
        return
    for i in range(len(s)):
        if s[:i+1]==s[:i+1][::-1]:
            getPartition(s[i+1:],temp+[s[:i+1]])
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        getPartition.ans = []
        getPartition(s)
        return getPartition.ans
          