class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for i in range(n)]
        for i in range(n):
            j = i-1
            while j>=0:
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i],dp[j] + 1)
                    
                j-=1
        return max(dp)
            