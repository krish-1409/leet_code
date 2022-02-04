#User function Template for python3
class Solution:
	def maxSumIS(self, arr, n):
		dp = [arr[i] for i in range(n)]
		dp[0] = arr[0]
		ans = -float('inf')
		for i in range(n):
		    for j in range(i):
		        if arr[j]<arr[i]:
		            dp[i] = max(dp[j]+arr[i],dp[i])
		    ans = max(ans,dp[i])
# 		print(dp)
        return ans
    # 1 101 2 3 100    
    # 1 102 3 6 
    # 44 
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxSumIS(Arr,n)
		print(ans)

# } Driver Code Ends