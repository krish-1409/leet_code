
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len(nums)
        count = [0 for _ in range(10001)]
        for i in range(n):
            count[nums[i]]+=1
        using = 0
        avoid = 0
        prev = -1
        print(sorted(nums))
        for i in range(1,10001):
            if count[i]>0:
                prev_using = using
                if prev==i-1:
                    using = avoid + i*count[i]
                    
                else:
                    prev_using = using
                    using = max(using,avoid) + i*count[i]
                avoid = max(prev_using,avoid)
                prev = i
                
        return max(using,avoid)
    

