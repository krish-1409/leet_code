class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n =  len(nums)
        dp = [False] * n
        dp[0] = True
        for i in range(1,n):
            j = i-1
            while j>=0 and not dp[i]:
                if i-j<=nums[j]:
                    dp[i] = dp[j]
                j-=1
        return dp[n-1]
            