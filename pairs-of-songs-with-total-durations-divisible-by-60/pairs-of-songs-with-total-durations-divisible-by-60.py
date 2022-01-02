class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        rem = [0] * 60
        for t in time:
            rem[t%60] += 1
        ans = 0
        ans += (rem[0]*(rem[0]-1))//2
        ans += (rem[30]*(rem[30]-1))//2
        for i in range(1,30):
            ans += rem[i]*rem[60-i]
        
        
        return ans