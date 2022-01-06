class Solution:
    def maxSubArray(self, a: List[int]) -> int:
        curr_sum = a[0]
        max_now = a[0]
        
        for i in range(1,len(a)):
            curr_sum = max(a[i],curr_sum+a[i])
            max_now = max(max_now,curr_sum)
            
        return max_now
            
        