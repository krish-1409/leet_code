def getTime(piles,t):
    ans = 0
    for c in piles:
        ans += math.ceil(c/t) 
        
    return ans
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_rate = max(piles)
        min_rate = 1
        
        while(min_rate<max_rate):
            mid = (min_rate+max_rate)//2
            if h<getTime(piles,mid):
                min_rate = mid + 1
            else:
                max_rate = mid
                
        return max_rate