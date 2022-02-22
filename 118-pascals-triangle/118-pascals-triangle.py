class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans = [[1],[1,1]]
        if n==1:
            return [[1]]
        if n==2:
            return ans
        for j in range(2,n):
            curr = [1]
            prev = ans[j-1]
            for i in range(1,len(prev)):
                curr.append(prev[i]+prev[i-1])
            curr.append(1)
            ans.append(curr)
        return ans