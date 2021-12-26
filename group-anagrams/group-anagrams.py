class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        freq = [[0 for _ in range(26)] for _ in range(n)]
        for i in range(n):
            for e in strs[i]:
                freq[i][ord(e)-ord('a')]+=1
        vis = [0]*n
        ans = []
        for i in range(n):
            if vis[i]==0:
                temp = [strs[i]]
                vis[i] = 1
                for j in range(i+1,n):
                    if freq[i] == freq[j]:
                        temp.append(strs[j])
                        vis[j] = 1
                ans.append(temp)
        return ans