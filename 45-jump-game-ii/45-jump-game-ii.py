"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0
        
        for i in range(1,n):
            j = i-1
            while j>=0:
                if i-j<=nums[j]:
                    dp[i] = min(dp[i],dp[j]+1)
                j-=1
        return dp[n-1]
                    
"""
def getJumps(nums,i,n,dp):
    if i>=n-1:
        return 0
    if dp[i]!=-1:
        return dp[i]
    ans = float('inf')
    for j in range(1,nums[i]+1):
        ans = min(ans,1 + getJumps(nums,i+j,n,dp))
    dp[i] = ans
    return dp[i]
        
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return 0
        dp = [-1] * n
        return getJumps(nums,0,n,dp)