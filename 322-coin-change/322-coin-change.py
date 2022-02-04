class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [float('inf') for i in range(amount+1)]
        dp[0] = 0
        for i in range(amount+1):
            for j in range(n):
                if i-coins[j]>=0:
                    dp[i] = min(dp[i],dp[i-coins[j]]+1)
        if dp[amount]==float('inf'):
            return -1
        return dp[amount]
        