def getTime(piles,t):
    ans = 0
    for c in piles:
        ans += math.ceil(c/t) 
        
    return ans
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        The min time to eat up all bananas willbe equal to no. of piles as each pile atleast 
        tskes an hour to complete. So at his min time the rate will be maximum which inturn \
        is equal to max height of the pile.
        we need to minimise rate acc to question
        Therefore we need to take rates from 1 to max_rate
        
        we take each rate and check we can optimize this using binary search.
        
        """
        max_rate = max(piles)
        min_rate = 1
        
        while(min_rate<max_rate):
            mid = (min_rate+max_rate)//2
            if h<getTime(piles,mid):
                min_rate = mid + 1
            else:
                max_rate = mid
                
        return max_rate